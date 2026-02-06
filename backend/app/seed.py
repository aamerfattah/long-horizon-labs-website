import json
from .core.database import SessionLocal, engine
from .models.models import Base, TechnologyDomain, SubTheme, InvestmentLens, ScientificPrinciple, Citation, AustraliaCase, AustraliaMetric, ResearchEntry, BriefAudit, InterrogationHistory, PortfolioProfile, CyberRisk, EcosystemCompany

def seed_data(drop_tables: bool = False):
    logs = []
    if drop_tables:
        # Force schema refresh to propagate column additions (like 'sources')
        print("Dropping existing tables for schema refresh...")
        Base.metadata.drop_all(bind=engine)
        print("Creating tables with updated schema...")
        Base.metadata.create_all(bind=engine)
    else:
        print("Ensuring tables exist (without dropping)...")
        Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    print("Seeding Technology Domains...")
    topics = [
        {
            "id": "ai-infra",
            "number": 1,
            "name": "AI Infrastructure",
            "icon": "Cloud",
            "category": "CORE",
            "type": "TOPIC",
            "whyItMatters": "AI returns accrue disproportionately to infrastructure owners, not model builders.",
        "subThemes": [
            {
                "title": "Compute",
                "description": "GPUs, accelerators, ASICs",
                "explainer": "The foundational layer of AI, focused on the specialized hardware required for training and inference. Value is currently concentrated in high-performance GPU clusters, but shifting toward inference-optimized ASICs as models reach deployment scale.",
                "technologies": ["H100/B200 GPUs", "TPUs", "Neuromorphic Chips", "Optical Interconnects"]
            },
            {
                "title": "AI Data Centres",
                "description": "Power intensity and cooling",
                "explainer": "Physical infrastructure is facing a power wall. Next-gen data centers require liquid cooling and gigawatt-scale power connections, increasingly co-located with nuclear or renewable baseloads to meet sustainability mandates.",
                "technologies": ["Liquid Immersion Cooling", "Rear-door Heat Exchangers", "Modular Data Centers", "HVDC Power Distribution"]
            },
            {
                "title": "Edge AI",
                "description": "Cloud vs on-device inference",
                "explainer": "Pushing inference to the device level to reduce latency and bandwidth costs. This requires effectively distilling massive models into efficient, quantised versions that can run on consumer hardware without significant accuracy loss.",
                "technologies": ["TinyML", "NPU Integration", "Model Distillation", "Federated Learning"]
            },
            {
                "title": "Sovereign AI",
                "description": "National computing stacks",
                "explainer": "The geopolitical imperative for nations to control their own AI destiny. This involves building domestic compute capacity and training foundation models on local datasets to ensure cultural and strategic alignment.",
                "technologies": ["National Cloud Stacks", "Sovereign Foundation Models", "Local Language Datasets", "Export-Controlled Compute"]
            }
        ],
        "investmentLenses": [
            { "title": "Capex Intensity", "details": "Infrastructure leads development" },
            { "title": "Power Constraints", "details": "Grid availability is the bottleneck" },
            { "title": "Supply Chains", "details": "Geopolitical exposure for chips" }
        ],
        "scientificPrinciples": [
            { "title": "Dennard Scaling", "details": "Breakdown of power density scaling at <5nm nodes." },
            { "title": "Von Neumann Bottleneck", "details": "Memory bandwidth limiting logic utilization." },
            { "title": "Amdahl's Law", "details": "Parallelization limits in massive training runs." }
        ],
        "reliabilityScore": 9.2,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "Gartner", "label": "AI Infra Maturity 2024", "url": "#" },
            { "source": "IEA", "label": "Electricity 2024 Analysis", "url": "#" }
        ],
        "scientificRationale": "The optimization of Von Neumann architectures and the transition to optical interconnects represent the fundamental physical limits of current semiconductor logic. Scientific interest is shifting toward neuromorphic and non-volatile memory-centric designs to bypass the memory wall.",
        "investorRationale": "Value in the AI stack is migrating from the 'Model Layer' to the 'Compute Layer' due to the scarcity of high-performance GPUs and the massive CapEx requirements for power-dense data centers. Infrastructure provides the most resilient proxy for AI growth.",
        "criticalQuestions": [
            {"question": "How does power availability constrain scaling?", "answer": "Grid capacity is the new GPU. 2026 mandates co-location with small modular reactors or dedicated baseload to ensure sub-10ms latency."},
            {"question": "Is interest rate cyclicality a risk?", "answer": "Yes, but sovereign subsidies (CHIPS Act 2.0) provide a floor for ROI on domestic data center builds."}
        ],
        "trl": 7,
        "yearsToScale": 3,
    },
    {
        "id": "semis",
        "number": 2,
        "name": "Semiconductors",
        "icon": "Cpu",
        "category": "CORE",
        "type": "TOPIC",
        "whyItMatters": "Semis are the choke point of modern economies.",
        "subThemes": [
            {
                "title": "Logic & Memory",
                "description": "Advanced node logic and HBM",
                "explainer": "The race for transistor density and memory bandwidth. Gate-all-around (GAA) architectures are essential for 2nm nodes, while High Bandwidth Memory (HBM) is now the critical bottleneck for AI workload performance.",
                "technologies": ["GAAFET Transistors", "HBM3e / HBM4", "3D NAND", "DRAM Stacking"]
            },
            {
                "title": "Compound Semis",
                "description": "GaN and SiC for power",
                "explainer": "Wide-bandgap semiconductors that handle higher voltages and temperatures than silicon. Critical for EV inverters and renewables, offering higher efficiency and enabling smaller form factors for power electronics.",
                "technologies": ["Silicon Carbide (SiC)", "Gallium Nitride (GaN)", "Diamond Substrates", "Vertical GaN"]
            },
            {
                "title": "Lithography",
                "description": "Fabrication tools and EUV",
                "explainer": "The physics of printing smaller features. High-NA EUV is the next frontier, enabling single-patterning at angstrom scales, but requiring massive re-engineering of the photoresist and mask infrastructure.",
                "technologies": ["High-NA EUV", "Directed Self-Assembly", "Nanoimprint Lithography", "E-beam Inspection"]
            },
            {
                "title": "Packaging",
                "description": "Chiplets and advanced interconnects",
                "explainer": "Moore's Law is slowing alone, so packaging is the new scaling vector. 2.5D and 3D stacking allow heterogeneous integration, combining different logic and memory dies into a single high-performance package.",
                "technologies": ["CoWoS (Chip on Wafer)", "Hybrid Bonding", "Silicon Interposers", "Glass Substrates"]
            }
        ],
        "investmentLenses": [
            { "title": "Sovereign Risk", "details": "National security imperatives" },
            { "title": "Industrial Policy", "details": "CHIPS Act and global subsidies" },
            { "title": "Cyclicality", "details": "Secular demand vs market cycles" }
        ],
        "scientificPrinciples": [
            { "title": "Quantum Tunneling", "details": "Leakage currents at atomic-scale gate lengths." },
            { "title": "Electromigration", "details": "Material degradation in high-density copper interconnects." },
            { "title": "Rayleigh Criterion", "details": "Diffraction limits in optical lithography resolution." }
        ],
        "reliabilityScore": 9.8,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "TSMC", "label": "Annual Report 2023", "url": "#" },
            { "source": "CSIS", "label": "Semiconductor Geopolitics", "url": "#" }
        ],
        "scientificRationale": "As Moore's Law hits atomic limits, the physics of High-NA EUV and GAAFET architectures become the primary drivers of performance. We are monitoring the transition from silicon to compound semiconductors (GaN/SiC) for high-frequency and power applications.",
        "investorRationale": "Semiconductors are the 'new oil'. Sovereign risk and supply chain regionalization are driving multi-billion dollar industrial policies, creating asymmetric opportunities for equipment providers (ASML, etc.) over fabless designers.",
        "criticalQuestions": [
            {"question": "When will 2nm GAAFET hit volume?", "answer": "Expect late 2025 for mobile and early 2026 for high-performance compute, pending yield stabilization at 12-inch wafers."},
            {"question": "How exposed is the supply chain to Taiwan?", "answer": "Extremely. 92% of <7nm logic remains concentrated in Hsinchu. 'China+1' strategies take 5-7 years to reach scale."}
        ],
        "trl": 9,
        "yearsToScale": 2,
    },
    {
        "id": "quantum",
        "number": 3,
        "name": "Quantum Tech",
        "icon": "Zap",
        "category": "CORE",
        "type": "TOPIC",
        "whyItMatters": "Optionality + asymmetric payoff + sovereign backing.",
        "subThemes": [
            {
                "title": "Quantum Computing",
                "description": "Gate-based and annealing systems",
                "explainer": "Harnessing superposition and entanglement for exponential speedups in specific problem sets. Returns will first appear in annealing for optimization, followed by error-corrected logical qubits for chemical simulation.",
                "technologies": ["Superconducting Qubits", "Trapped Ions", "Neutral Atoms", "Photonic QC"]
            },
            {
                "title": "Quantum Sensing",
                "description": "Precision metrology and navigation",
                "explainer": "Using quantum states to measure physical properties with unprecedented sensitivity. Key for GPS-denied navigation (PNT), subterranean mapping, and early disease detection via magnetic field sensing.",
                "technologies": ["Atomic Clocks", "Gravimeters", "Magnetometers", "NV Centers in Diamond"]
            },
            {
                "title": "Quantum Comms",
                "description": "Encryption and entanglement",
                "explainer": "Securing communications against harvest-now-decrypt-later attacks. QKD offers physically unbreakable key distribution, while quantum repeaters are the holy grail for a future quantum internet.",
                "technologies": ["QKD (Key Distribution)", "Quantum Repeaters", "Entanglement Swapping", "Satellite QKD"]
            },
            {
                "title": "Hybrid Systems",
                "description": "Quantum-classical orchestration",
                "explainer": "The practical near-term reality. Orchestrating workflows where quantum processors act as accelerators for specific subroutines within massive classical high-performance computing (HPC) environments.",
                "technologies": ["Quantum-Classical Bridge", "Variational Algorithms", "Error Mitigation Layer", "Cloud Access Models"]
            }
        ],
        "investmentLenses": [
            { "title": "Timing", "details": "Expected 2028-2030 for chemical simulation breakthroughs." },
            { "title": "Monetization", "details": "Cloud-hybrid orchestration layers capture value first." },
            { "title": "Hype vs Reality", "details": "NISQ era refocusing on sensing before universal QC." }
        ],
        "scientificPrinciples": [
            { "title": "Superposition", "details": "Qubits existing in multiple states simultaneously." },
            { "title": "Entanglement", "details": "Non-local correlation between particle states." },
            { "title": "Decoherence", "details": "Loss of quantum state due to environmental noise." }
        ],
        "reliabilityScore": 4.5,
        "evidenceLevel": "SPECULATIVE",
        "citations": [
            { "source": "Nature", "label": "Quantum Error Correction 2024", "url": "#" },
            { "source": "McKinsey", "label": "Quantum Computing Value", "url": "#" }
        ],
        "scientificRationale": "Quantum advantage requires stabilizing entanglement against thermal noise. Cryogenic engineering and error-correction algorithms (Surface Codes) are the current scientific frontiers. Photonic paths offer scalability but face significant loss hurdles.",
        "investorRationale": "Quantum is a 'long-vol' play with zero-knowledge payoffs. The first commercial returns will likely come from sensing and metrology (navigation) before universal gate-based computation reaches chemical simulation scale.",
        "criticalQuestions": [
            {"question": "When does it matter for chemical simulation?", "answer": "Our modelling suggests a 1,000 logical qubit threshold by 2028-2030, unlocking $100B+ in pharmaceutical IP value."},
            {"question": "Who captures value first in the stack?", "answer": "The 'Quantum-Classical Cloud' providers who can orchestrate hybrid workflows effectively today."}
        ],
        "trl": 4,
        "yearsToScale": 12,
    },
    {
        "id": "energy",
        "number": 4,
        "name": "Energy Transition",
        "icon": "Power",
        "category": "CORE",
        "type": "TOPIC",
        "whyItMatters": "Super funds are already exposed, but often unknowingly.",
        "subThemes": [
            {
                "title": "Grid Storage",
                "description": "Beyond lithium technologies",
                "explainer": "Lithium-ion is insufficient for grid-scale buffering. Alternative chemistries like Sodium-ion offer lower energy density but dramatically lower cost and higher safety profiles for stationary storage applications.",
                "technologies": ["Sodium-Ion", "Flow Batteries", "Solid State Batteries", "Metal-Air Chemistries"]
            },
            {
                "title": "LDES",
                "description": "Long-duration energy storage",
                "explainer": "Solving the 'dunkelflaute' (dark doldrums) problem. Technologies capable of storing energy for days or weeks (10h-100h+) to bridge prolonged renewable generation gaps, moving beyond pumped hydro geographic constraints.",
                "technologies": ["Thermal Storage", "Compressed Air", "Gravity Storage", "Hydrogen Electrolysis"]
            },
            {
                "title": "Advanced Nuclear",
                "description": "SMRs and Gen IV reactors",
                "explainer": "Reinventing nuclear for safety and modularity. Small Modular Reactors (SMRs) reduce upfront capex risk, while Gen IV designs utilize waste as fuel and offer passive shut-down safety features.",
                "technologies": ["SMRs (Light Water)", "Molten Salt Reactors", "High Temp Gas", "Micro-reactors"]
            },
            {
                "title": "Grid Optimization",
                "description": "Power electronics & software",
                "explainer": "Making the grid smarter to handle bidirectional flows. Advanced power electronics and AI-driven load balancing are essential to integrate distributed energy resources (DERs) without destabilizing frequency.",
                "technologies": ["Smart Inverters", "Virtual Power Plants", "Dynamic Line Rating", "Grid-Forming Controls"]
            }
        ],
        "investmentLenses": [
            { "title": "Infra-like Returns", "details": "Stable yields with tech alpha" },
            { "title": "Regulation", "details": "Decarbonization mandates" }
        ],
        "scientificPrinciples": [
            { "title": "Thermodynamics 2nd Law", "details": "Entropy limits in conversion efficiency." },
            { "title": "Electrochemistry", "details": "Ion transport limitations in battery cathodes." },
            { "title": "Grid Inertia", "details": "Frequency stability in inverter-based grids." }
        ],
        "reliabilityScore": 8.5,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "IRENA", "label": "World Energy Transitions 2023", "url": "#" },
            { "source": "BNEF", "label": "Energy Storage Outlook 2024", "url": "#" }
        ],
        "insight": "Energy transition is a deep tech problem disguised as infrastructure.",
        "trl": 6,
        "yearsToScale": 8,
    },
    {
        "id": "materials",
        "number": 5,
        "name": "Advanced Materials",
        "icon": "Box",
        "category": "ADJACENT",
        "type": "TOPIC",
        "whyItMatters": "Almost every breakthrough depends on materials.",
        "subThemes": [
            {
                "title": "Nanomaterials",
                "description": "Scaling atomic-level properties",
                "explainer": "Engineered materials with unique properties at the nanoscale. Graphene and Carbon Nanotubes offer immense strength-to-weight ratios and conductivity, now finally moving from lab curiosity to niche industrial applications.",
                "technologies": ["Graphene", "Carbon Nanotubes", "MOFs", "Quantum Dots"]
            },
            {
                "title": "Metamaterials",
                "description": "Engineered wave interaction",
                "explainer": "Materials structured to manipulate electromagnetic waves in unnatural ways. Key unlocking unlock flat lenses, advanced radar cloaking, and next-gen antennas for satellite communications.",
                "technologies": ["Negative Index Materials", "Flat Optics / Metalenses", "Reconfigurable Surfaces", "Acoustic Metamaterials"]
            },
            {
                "title": "Composites",
                "description": "High-performance structures",
                "explainer": "Lightweighting for aerospace and automotive efficiency. Thermoplastic composites allow for faster manufacturing cycles and recyclability compared to traditional thermoset epoxies.",
                "technologies": ["Thermoplastic Composites", "Ceramic Matrix Composites", "Bio-composites", "Continuous Fiber Printing"]
            },
            {
                "title": "Rare Earths",
                "description": "Substitutes and scaling",
                "explainer": "Reducing dependence on geopolitical chokepoints. R&D is focused on magnet alternatives that eliminate Neodymium/Dysprosium, or new bio-leaching extraction methods to make varied deposits viable.",
                "technologies": ["Magnet Recycling", "Iron-Nitride Magnets", "Bio-leaching", "Direct Separation"]
            }
        ],
        "investmentLenses": [
            { "title": "Comm Risk", "details": "The Valley of Death in scaling" },
            { "title": "IP Defensibility", "details": "Process vs composition patents" }
        ],
        "reliabilityScore": 7.2,
        "evidenceLevel": "MODERATE",
        "citations": [
            { "source": "Science Daily", "label": "Material Breakthroughs", "url": "#" },
            { "source": "MIT", "label": "Nanomaterials scaling", "url": "#" }
        ],
        "trl": 5,
        "yearsToScale": 10,
    },
    {
        "id": "synbio",
        "number": 6,
        "name": "Synthetic Biology",
        "icon": "Microscope",
        "category": "ADJACENT",
        "type": "TOPIC",
        "whyItMatters": "Biology is becoming programmable.",
        "subThemes": [
            {
                "title": "Fermentation",
                "description": "Precision bio-manufacturing",
                "explainer": "Using microbes as factories. Precision fermentation reprograms yeast or bacteria to produce complex proteins, fats, or materials identical to their natural counterparts, decoupling production from agriculture.",
                "technologies": ["Precision Fermentation", "Gas Fermentation", "Strain Engineering", "Bioreactor Design"]
            },
            {
                "title": "Lab-grown",
                "description": "Materials and food scaling",
                "explainer": "Cultivating cells directly to create tissues or materials. Whether for cultivated meat or bio-leather, the challenge has shifted from 'can we do it' to 'can we achieve cost parity' via media cost reduction.",
                "technologies": ["Cellular Agriculture", "Scaffold Tech", "Serum-free Media", "Bio-fabrication"]
            },
            {
                "title": "Enzymes",
                "description": "Engineering biocatalysts",
                "explainer": "Designing enzymes for robust industrial use. These biological catalysts operate at lower energies than chemical equivalents, transforming plastic recycling, textile manufacturing, and carbon capture processes.",
                "technologies": ["Protein Design AI", "Directed Evolution", "Immobilized Enzymes", "Plastic-eating Enzymes"]
            },
            {
                "title": "Bio-chemicals",
                "description": "Petrochemical alternatives",
                "explainer": "Replacing the barrel of oil. Bio-derived platform chemicals provide a drop-in sustainable route for plastics, solvents, and fuels, leveraging synthetic biology to optimize metabolic pathways.",
                "technologies": ["Bio-polymers (PHA/PLA)", "Bio-nylon", "Sustainable Aviation Fuel", "Algae Platforms"]
            }
        ],
        "investmentLenses": [
            { "title": "Time-to-scale", "details": "Bioreactor capacity bottlenecks" },
            { "title": "Unit Economics", "details": "Parity with traditional methods" }
        ],
        "reliabilityScore": 6.8,
        "evidenceLevel": "MODERATE",
        "citations": [
            { "source": "SynBioBeta", "label": "Industry Report 2024", "url": "#" },
            { "source": "Nature Bio", "label": "Programmable Biology", "url": "#" }
        ],
        "trl": 5,
        "yearsToScale": 10,
    },
    {
        "id": "robotics",
        "number": 7,
        "name": "Robotics & Autonomy",
        "icon": "Factory",
        "category": "ADJACENT",
        "type": "TOPIC",
        "whyItMatters": "Labour scarcity meets capital productivity.",
        "subThemes": [
            {
                "title": "Industrial Robotics",
                "description": "Next-gen automation",
                "explainer": "Moving from caged to collaborative. Cobots with advanced force-sensing and vision systems can work safely alongside humans, unlocking automation for high-mix, low-volume manufacturing tasks.",
                "technologies": ["Cobots", "Vision-Guidance", "Adaptive Grippers", "Force Torque Sensors"]
            },
            {
                "title": "Autonomous Logistics",
                "description": "Automated supply chains",
                "explainer": "The backbone of modern commerce. AMRs (Autonomous Mobile Robots) navigate dynamic warehouse environments without infrastructure, while drone delivery addresses the expensive efficiency gap of the last mile.",
                "technologies": ["AMRs", "SLAM Navigation", "Drone Delivery", "Warehouse Swarms"]
            },
            {
                "title": "Dual-use Systems",
                "description": "Defence and commercial",
                "explainer": "Robotics bred for conflict, applied to industry. Durable, all-terrain platforms developed for battlefield logistics or reconnaissance are finding commercial use in mining, forestry, and disaster response.",
                "technologies": ["Unmanned Ground Vehicles", "Quadruped Robots", "Exoskeletons", "Loitering Munitions"]
            },
            {
                "title": "HMI",
                "description": "Human-machine collaboration",
                "explainer": "Bridging the intent gap. Teleoperation and brain-computer interfaces (BCI) allow intuitive control of complex robotic systems, essential for hazardous environments or remote surgical procedures.",
                "technologies": ["Telepresence", "Haptic Feedback", "Brain-Computer Interface", "Gesture Control"]
            }
        ],
        "investmentLenses": [
            { "title": "Opex to Capex", "details": "Labor cost substitution" },
            { "title": "Adoption Curves", "details": "Industry-specific bottlenecks" }
        ],
        "reliabilityScore": 8.9,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "IFR", "label": "World Robotics 2023", "url": "#" },
            { "source": "ARK Invest", "label": "Automation Forecast", "url": "#" }
        ],
        "trl": 8,
        "yearsToScale": 4,
    },
    {
        "id": "space",
        "number": 8,
        "name": "Space Tech",
        "icon": "Rocket",
        "category": "ADJACENT",
        "type": "TOPIC",
        "whyItMatters": "Space is now an enabler, not a destination.",
        "subThemes": [
            {
                "title": "Earth Observation",
                "description": "Data layers for agriculture/finance",
                "explainer": "The eyes of the new space economy. Hyperspectral and SAR (Synthetic Aperture Radar) satellites provide continuous, all-weather monitoring of supply chains, crop health, and methane leaks.",
                "technologies": ["Hyperspectral Imaging", "SAR Satellites", "Edge Computing in Orbit", "Inter-satellite Links"]
            },
            {
                "title": "Launch Economics",
                "description": "Cost per kg to orbit",
                "explainer": "The race to the bottom for access. Reusability has decimated launch costs, enabling mega-constellations. The next phase focuses on rapid cadence and heavy-lift capacities for orbital infrastructure.",
                "technologies": ["Reusable Boosters", "3D Printed Engines", "Methalox Propellants", "Air Launch"]
            },
            {
                "title": "Space Comms",
                "description": "Leo constellations",
                "explainer": "Internet from the sky. LEO mega-constellations offer low-latency global broadband, challenging terrestrial fiber and 5G models, particularly for maritime, aviation, and defence applications.",
                "technologies": ["LEO Constellations", "Laser/Optical Comms", "Phased Array Antennas", "Software Defined Radio"]
            },
            {
                "title": "SSA",
                "description": "Space situational awareness",
                "explainer": "Traffic control for orbit. As space gets crowded, tracking debris and managing collision avoidance becomes mission-critical, creating a market for ground-based radar and orbital mapping services.",
                "technologies": ["Ground Radar Tracking", "Space-based Surveillance", "Collision Avoidance AI", "Debris Removal"]
            }
        ],
        "investmentLenses": [
            { "title": "Value Capture", "details": "Launch is an enabler, not the end" }
        ],
        "reliabilityScore": 7.5,
        "evidenceLevel": "MODERATE",
        "citations": [
            { "source": "Euroconsult", "label": "Launch Market Trends", "url": "#" },
            { "source": "SpaceNews", "label": "SSA Growth Analysis", "url": "#" }
        ],
        "insight": "Launch ≠ value capture",
        "trl": 7,
        "yearsToScale": 6,
    },
    {
        "id": "fusion",
        "number": 9,
        "name": "Fusion Energy",
        "icon": "Flame",
        "category": "FRONTIER",
        "type": "TOPIC",
        "whyItMatters": "Zero-carbon baseload optionality.",
        "subThemes": [
            {
                "title": "Confinement",
                "description": "Magnetic vs inertial",
                "explainer": "The two main paths to ignition. Tokamaks use massive magnets to contain plasma for long durations, while Inertial Confinement uses high-power lasers to implode fuel pellets for pulsed energy release.",
                "technologies": ["Tokamaks", "Stellarators", "Laser Inertial Fusion", "Field-Reversed Config"]
            },
            {
                "title": "Supply Chain",
                "description": "Tritium and superconductors",
                "explainer": "The hidden hurdles. Fusion requires rare fuel isotopes like Tritium (currently scarce) and HTS (High Temperature Superconducting) tapes at scales that far exceed current global production capacity.",
                "technologies": ["Tritium Breeding", "HTS Tape Manuf.", "Fusion Materials", "Cryogenics"]
            },
            {
                "title": "Funding Models",
                "description": "Public-private partnerships",
                "explainer": "Capitalizing the long haul. Fusion is too capital intensive for pure VC. Successful ventures blend government grants (for basic science) with private equity (for engineering / commercialization velocity).",
                "technologies": ["Cost-Share Programs", "Milestone-based Funding", "Sovereign Wealth Backing", "Corporate R&D"]
            }
        ],
        "investmentLenses": [
            { "title": "Engagement Timing", "details": "Milestone-based entry at ignition proof-points." }
        ],
        "reliabilityScore": 3.2,
        "evidenceLevel": "SPECULATIVE",
        "citations": [
            { "source": "IAEA", "label": "Fusion Energy Progress", "url": "#" },
            { "source": "FIA", "label": "Global Fusion Report", "url": "#" }
        ],
        "trl": 2,
        "yearsToScale": 20,
    },
    {
        "id": "nuclear-adv",
        "number": 10,
        "name": "Advanced Nuclear",
        "icon": "Activity",
        "category": "FRONTIER",
        "type": "TOPIC",
        "whyItMatters": "Baseload without intermittency.",
        "subThemes": [
            {
                "title": "SMRs",
                "description": "Small modular reactors",
                "explainer": "Factory-built nuclear. By standardizing designs and reducing size (<300MW), SMRs aim to reduce construction risk, enable incremental capacity addition, and fit into coal plant legacy footprints.",
                "technologies": ["Light Water SMRs", "Molten Salt Reactors", "Factory Fabrication", "Passive Safety Systems"]
            },
            {
                "title": "Fuel Cycles",
                "description": "Closed-loop and recycling",
                "explainer": "Maximizing energy extraction. Advanced fuel cycles (TRISO, HALEU) and reprocessing technologies can extract up to 100x more energy from uranium while drastically reducing long-lived waste volume.",
                "technologies": ["TRISO Fuel", "HALEU Enrichment", "Pyroprocessing", "MOX Fuel"]
            },
            {
                "title": "Waste Handling",
                "description": "Innovations in storage",
                "explainer": "Not just burying it. Deep borehole disposal and transmutation (using fast reactors to break down long-lived isotopes) offer permanent solutions to the political bottleneck of high-level waste.",
                "technologies": ["Deep Boreholes", "Dry Cask Storage", "Transmutation", "Geological Repositories"]
            }
        ],
        "investmentLenses": [
            { "title": "Political Risk", "details": "Regulatory path and public perception" }
        ],
        "reliabilityScore": 6.5,
        "evidenceLevel": "MODERATE",
        "citations": [
            { "source": "NEA", "label": "SMR Roadmap", "url": "#" },
            { "source": "WNA", "label": "Advanced Reactor Status", "url": "#" }
        ],
        "trl": 5,
        "yearsToScale": 15,
    },
    {
        "id": "climate-adapt",
        "number": 11,
        "name": "Climate Adaptation",
        "icon": "Waves",
        "category": "THEME",
        "type": "THEME",
        "whyItMatters": "Mitigation alone won’t be enough.",
        "subThemes": [
            {
                "title": "Water Security",
                "description": "Desal and purification",
                "explainer": "Decoupling fresh water from rainfall. Solar-thermal desalination and graphene-oxide membranes are lowering the energy cost of purified water, essential for regions facing chronic drought.",
                "technologies": ["Solar Desalination", "Graphene Membranes", "Atmospheric Water Gen", "Wastewater Recycling"]
            },
            {
                "title": "Resilience",
                "description": "Flood and fire tech",
                "explainer": "Defending the built environment. AI-driven wildfire detection networks and dynamic flood barriers are moving adaptation from passive insurance models to active risk mitigation.",
                "technologies": ["Satellite Fire Tracking", "Smart Levees", "Permeable Pavement", "Early Warning AI"]
            },
            {
                "title": "Ag Adaptation",
                "description": "Climate-resilient crops",
                "explainer": "Feeding a hotter world. Gene-editing (CRISPR) is being used to rapidly develop crop varieties that can tolerate high heat, salinity, and drought without the multi-decade timeline of traditional breeding.",
                "technologies": ["CRISPR Breeding", "Vertical Farming", "Saline Agriculture", "Precision Irrigation"]
            },
            {
                "title": "Infrastructure",
                "description": "Resilient building materials",
                "explainer": "Hardening assets. Self-healing concrete and high-albedo (reflective) coatings are extending asset life and reducing urban heat island effects in increasingly hostile climates.",
                "technologies": ["Self-healing Concrete", "Cool Roofs/Pavements", "Retrofit Analytics", "Coastal Armoring"]
            }
        ],
        "investmentLenses": [
            { "title": "Undercapitalization", "details": "High alpha in overlooked resilience markets" }
        ],
        "reliabilityScore": 5.8,
        "evidenceLevel": "SPECULATIVE",
        "citations": [
            { "source": "IPCC", "label": "Adaptation Report 2024", "url": "#" },
            { "source": "UNEP", "label": "Adaptation Gap 2023", "url": "#" }
        ],
        "insight": "Adaptation spend is inevitable and undercapitalised.",
        "trl": 4,
        "yearsToScale": 12,
    },
    {
        "id": "cyber-phys",
        "number": 12,
        "name": "Cyber-Physical Sec",
        "icon": "ShieldAlert",
        "category": "THEME",
        "type": "THEME",
        "whyItMatters": "Digital trust underpins all assets.",
        "subThemes": [
            {
                "title": "Post-Quantum Crypto",
                "description": "Securing data for the next decade",
                "explainer": "The Y2Q defence. As quantum computers threaten RSA/ECC encryption, new lattice-based cryptographic standards are being finalized to secure government and financial data before 'Q-Day'.",
                "technologies": ["Lattice Cryptography", "Hash-based Signatures", "Crypto-agility", "Quantum RNG"]
            },
            {
                "title": "Infra Security",
                "description": "SCADA and IoT protection",
                "explainer": "Protecting the kinetical world. Operational Technology (OT) networks controlling power plants and factories are legacy-heavy and air-gapped; connecting them requires specialized, non-intrusive monitoring.",
                "technologies": ["Unidirectional Gateways", "OT Network Monitoring", "Micro-segmentation", "Zero Trust for IoT"]
            },
            {
                "title": "Hardware Security",
                "description": "Root of trust at chip level",
                "explainer": "Trust starts at the silicon. Physics Unclonable Functions (PUFs) and secure enclaves ensure that identity and boot integrity are verified by unique physical imperfections in the chip itself.",
                "technologies": ["PUFs", "Secure Enclaves", "Supply Chain Provenance", "Side-channel Defence"]
            }
        ],
        "investmentLenses": [
            { "title": "Systemic Risk", "details": "Mitigating portfolio-wide contagion" }
        ],
        "reliabilityScore": 8.2,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "NIST", "label": "PQC Standards 2024", "url": "#" },
            { "source": "CISA", "label": "Critical Infra Shield", "url": "#" }
        ],
        "trl": 8,
        "yearsToScale": 5,
    },
    {
        "id": "sovereign",
        "number": 13,
        "name": "Sovereign Policy",
        "icon": "Globe2",
        "category": "THEME",
        "type": "THEME",
        "whyItMatters": "Government funding flywheels drive deep tech.",
        "subThemes": [
            {
                "title": "Funding Flywheels",
                "description": "Grants and debt financing",
                "explainer": "The new capital stack. Systematic tracking of non-dilutive government capital (SBIR, Horizon Europe) acts as a signal for technical due diligence and a de-risking lever for private equity.",
                "technologies": ["Non-dilutive Grants", "Loan Guarantees", "Offtake Agreements", "R&D Tax Credits"]
            },
            {
                "title": "Defence Innovation",
                "description": "Dual-use funding streams",
                "explainer": "Silicon Valley meets the Pentagon. Organizations like DIU and OTAN DIANA are creating fast-track procurement pathways for commercial tech to enter defence programs of record.",
                "technologies": ["Dual-use Ventures", "Fast-track Procurement", "Classified R&D", "Battlefield Testing"]
            },
            {
                "title": "Capability Agendas",
                "description": "National technological moats",
                "explainer": "Technology as statecraft. Identifying which 10 critical technologies a nation has decided are vital for its sovereignty, directing subsidies and talent visas into those specific verticals.",
                "technologies": ["Sovereign Wealth Funds", "National Strategies", "Export Controls", "Talent Visas"]
            }
        ],
        "investmentLenses": [],
        "reliabilityScore": 9.5,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "White House", "label": "Critical Emerging Tech", "url": "#" },
            { "source": "OECD", "label": "R&D Industry Policy", "url": "#" }
        ],
        "trl": 9,
        "yearsToScale": 1,
    },
    {
        "id": "supply-chain",
        "number": 14,
        "name": "Supply Chain",
        "icon": "Truck",
        "category": "THEME",
        "type": "THEME",
        "whyItMatters": "Resilience is the new efficiency.",
        "subThemes": [
            {
                "title": "Critical Minerals",
                "description": "Processing and traceability",
                "explainer": "The new oil. Securing the supply of Lithium, Cobalt, and Rare Earths is shifting from raw extraction to mid-stream processing capacity, with blockchain traceability ensuring ESG compliance.",
                "technologies": ["Mineral Tracking", "Direct Lithium Extraction", "Battery Recycling", "Supply Chain Digital Twins"]
            },
            {
                "title": "Onshoring",
                "description": "Automated fabrication",
                "explainer": "Bringing it home. Re-industrialization in high-cost labor markets is only viable through high levels of automation and robotics, reducing the unit-cost gap with offshore manufacturing.",
                "technologies": ["Smart Factories", "Additive Manufacturing", "Robotic Assembly", "Digital Quality Control"]
            },
            {
                "title": "Logistics Auto",
                "description": "AI-driven orchestration",
                "explainer": "Predictive movement. AI models that optimize complex intermodal freight networks, predicting bottlenecks and rerouting shipments in real-time to build resilience against shocks.",
                "technologies": ["Predictive Logistics", "Autonomous Freight", "Port Automation", "Route Optimization AI"]
            }
        ],
        "investmentLenses": [],
        "reliabilityScore": 8.7,
        "evidenceLevel": "HIGH",
        "citations": [
            { "source": "World Bank", "label": "Minerals for Climate Action", "url": "#" },
            { "source": "IEA", "label": "Critical Minerals Outlook", "url": "#" }
        ],
        "trl": 7,
        "yearsToScale": 5,
    },
    {
        "id": "impact-mapping",
        "number": 15,
        "name": "Impact Mapping",
        "icon": "Timer",
        "category": "THEME",
        "type": "THEME",
        "whyItMatters": "Scientific maturity vs commercial viability.",
        "subThemes": [
            {
                "title": "TRL Frameworks",
                "description": "Technology Readiness Levels",
                "explainer": "The standard yardstick. Originally from NASA, TRLs provide a common language to assess maturity from basic principles (TRL 1) to flight-proven systems (TRL 9), crucial for consistent portfolio benchmarking.",
                "technologies": ["TRL Assessment", "MRL (Manufacturing)", "IRL (Integration)", "CRL (Commercial)"]
            },
            {
                "title": "Maturity Curves",
                "description": "Prototyping to mass adoption",
                "explainer": "Mapping the S-curve. Understanding where a specific technology sits on the adoption curve allows investors to time their entry, avoiding the hype cycle peak and deploying capital during the slope of enlightenment.",
                "technologies": ["S-Curve Modeling", "Hype Cycle Analysis", "Adoption Diffusion", "Market Sizing"]
            },
            {
                "title": "Valuation Delta",
                "description": "Risk-adjusted growth",
                "explainer": "Pricing the risk. As technical risk is retired through milestones (e.g. valid prototype), the valuation multiple expands. Deep tech investing is arbitrage on this capability-to-valuation lag.",
                "technologies": ["Risk-Adjusted NAV", "Milestone Valuation", "Option Pricing", "Tech-Econ Modeling"]
            }
        ],
        "investmentLenses": [],
        "reliabilityScore": 7.8,
        "evidenceLevel": "MODERATE",
        "citations": [
            { "source": "NASA", "label": "TRL Definitions", "url": "#" },
            { "source": "HBR", "label": "Commercializing Deep Tech", "url": "#" }
        ],
        "trl": 9,
        "yearsToScale": 1,
    }
    ]

    # Clear existing data to ensure clean seed
    print("Clearing existing data...")
    db.query(ResearchEntry).delete()
    db.query(InterrogationHistory).delete()
    db.query(CyberRisk).delete()
    db.query(PortfolioProfile).delete()
    db.query(AustraliaMetric).delete()
    db.query(AustraliaCase).delete()
    db.query(Citation).delete()
    db.query(ScientificPrinciple).delete()
    db.query(InvestmentLens).delete()
    db.query(SubTheme).delete()
    db.query(BriefAudit).delete()
    db.query(TechnologyDomain).delete()
    db.commit()

    print("Seeding Technology Domains...")
    for topic_data in topics:
        domain = TechnologyDomain(
            topic_id=topic_data["id"],
            number=topic_data["number"],
            name=topic_data["name"],
            icon=topic_data["icon"],
            why_it_matters=topic_data["whyItMatters"],
            insight=topic_data.get("insight"),
            category=topic_data["category"],
            type=topic_data["type"],
            reliability_score=topic_data["reliabilityScore"],
            evidence_level=topic_data["evidenceLevel"],
            trl=topic_data["trl"],
            years_to_scale=topic_data["yearsToScale"],
            critical_questions=topic_data.get("criticalQuestions"),
            scientific_rationale=topic_data.get("scientificRationale"),
            investor_rationale=topic_data.get("investorRationale")
        )
        db.add(domain)
        db.flush() # Get domain id

        for st in topic_data["subThemes"]:
            db.add(SubTheme(
                domain_id=domain.id,
                title=st["title"],
                description=st["description"],
                explainer=st.get("explainer"),
                technologies=st.get("technologies")
            ))

        for il in topic_data["investmentLenses"]:
            db.add(InvestmentLens(
                domain_id=domain.id,
                title=il["title"],
                details=il["details"]
            ))

        for sp in topic_data.get("scientificPrinciples", []):
            db.add(ScientificPrinciple(
                domain_id=domain.id,
                title=sp["title"],
                details=sp["details"]
            ))

        for cit in topic_data["citations"]:
            db.add(Citation(
                domain_id=domain.id,
                source=cit["source"],
                url=cit["url"],
                label=cit["label"]
            ))

    db.commit()
    print("Database seeded successfully with all 15 domains.")

    # Seed Australia Data
    print("Seeding Australia Cases...")
    australian_cases = [
        {
            "name": "Quantum Computing Hub (NSW)",
            "sector": "Infrastructure",
            "model_type": "Sovereign Cloud",
            "revenue_status": "Contracted-Pre",
            "investor_mix": "Gov / Super",
            "horizon": "10+ Years",
            "risk_profile": "Implementation",
            "city": "Sydney",
            "efficiency_metric": "85% Gov Backed"
        },
        {
            "name": "Defence Sensing Lab",
            "sector": "Defence",
            "model_type": "Component OEM",
            "revenue_status": "B2B Recurring",
            "investor_mix": "VC / Infra",
            "horizon": "5-7 Years",
            "risk_profile": "Market Adoption",
            "city": "Adelaide",
            "efficiency_metric": "A$50M+ Pipeline"
        },
        {
            "name": "Resources Optimization Suite",
            "sector": "Mining",
            "model_type": "SaaS",
            "revenue_status": "B2B Piloting",
            "investor_mix": "Corporate VC",
            "horizon": "3-5 Years",
            "risk_profile": "Technical Fidelity",
            "city": "Perth",
            "efficiency_metric": "4 Tier-1 Clients"
        },
        {
            "name": "Bio-Manufacturing Precinct",
            "sector": "BioTech",
            "model_type": "Platform-as-a-Service",
            "revenue_status": "Service Revenue",
            "investor_mix": "State Gov / PE",
            "horizon": "7-10 Years",
            "risk_profile": "Regulatory",
            "city": "Brisbane",
            "efficiency_metric": "A$120M Export Goal"
        }
    ]
    for case in australian_cases:
        db.add(AustraliaCase(**case))

    print("Seeding Australia Metrics...")
    metrics = [
        {"category": "Efficiency", "label": "Defence", "value": 8.4, "color_hex": "#2563EB"},
        {"category": "Efficiency", "label": "Mining", "value": 7.2, "color_hex": "#06B6D4"},
        {"category": "Efficiency", "label": "BioTech", "value": 6.8, "color_hex": "#7C3AED"},
        {"category": "Efficiency", "label": "Quantum", "value": 9.1, "color_hex": "#10B981"},
        {"category": "Composition", "label": "Sovereign/Gov", "value": 45.0, "color_hex": "#2563EB"},
        {"category": "Composition", "label": "Superannuation", "value": 30.0, "color_hex": "#06B6D4"},
        {"category": "Composition", "label": "VC/Private", "value": 20.0, "color_hex": "#7C3AED"},
        {"category": "Composition", "label": "Corporate", "value": 5.0, "color_hex": "#94A3B8"}
    ]
    for metric in metrics:
        db.add(AustraliaMetric(**metric))

    print("Seeding Research Entries...")
    research_data = [
        {
            "topic_id": "quantum",
            "title": "Quantum Error Correction: A Path to Logical Qubits",
            "summary": "Analyzing recent breakthroughs in surface code logic and its implications for 2029 deployment benchmarks.",
            "content": """### Technical Analysis: Transition to Logical Qubits

The research community has reached a critical inflection point in **Quantum Error Correction (QEC)**. While 2024 focused on physical qubit counts, 2026 is defined by the suppression of physical errors through topological surface codes.

#### Strategic Implications
Recent data from several hardware providers indicate that the 'error floor' required for logical qubit preservation has been reached. This allows for the orchestration of logical units that can survive for orders of magnitude longer than their constituent physical qubits.

#### IC Takeaway
Investors should pivot their focus from hardware manufacturers to the 'Software and Middleware Layer' of the quantum stack. Companies providing the error suppression algorithms and cryogenic orchestration will capture the majority of the value in the next 36 months.""",
            "author": "DeepTechIQ Research Team",
            "category": "technical-insight",
            "status": "published",
            "sources": [
                {"source": "Nature Physics", "label": "Logical Qubit Demonstration", "url": "https://www.nature.com/nphys/"},
                {"source": "IBM Quantum Research", "label": "2026 Roadmap Update", "url": "https://www.research.ibm.com/quantum-computing"}
            ],
            "quant_data": [
                {"label": "Physical-to-Logical Ratio", "value": "1000:1", "unit": "Ratio"},
                {"label": "Gate Fidelity", "value": "99.98", "unit": "%"},
                {"label": "Logical Life-time", "value": "1.2", "unit": "ms"}
            ],
            "modelling": "Our 'Quantum Horizon' model suggests that at current error suppression rates, we will reach 100 logical qubits by Q3 2028. This triggers the 'Quantum Advantage' scenario for material science simulations, potentially disrupting a $40B addressable market in electrolyte design."
        },
        {
            "topic_id": "ai-infra",
            "title": "The GPU Shortage: Supply Chain Analysis Q1 2026",
            "summary": "Critical yields in HBM4 production are creating a secondary bottleneck for next-gen AI accelerator rollouts.",
            "content": """### Market Signal: Chip-let Architectures and HBM4 Yields

The dominance of monolithic GPU designs is being challenged by the rapid adoption of chip-let based accelerators. However, our supply chain analysis shows that **HBM4 (High Bandwidth Memory)** yield rates are currently 15% below the necessary threshold for wide-scale 2026 deployment.

#### Key Bottlenecks
- **Thermal Management**: The power density of 2nm nodes is exceeding previous liquid cooling benchmarks.
- **Interconnect Latency**: Photonic interconnects are becoming the primary cost driver for massive-scale cluster deployments.

#### Strategic Recommendation
We advise a 'Hold' on pure-play GPU designers while significantly increasing exposure to 'Advanced Packaging' and 'Interconnect' specialists. The value is migrating from the core compute die to the physical orchestration of the cluster.""",
            "author": "DeepTechIQ Research Team",
            "category": "market-report",
            "status": "published",
            "sources": [
                {"source": "TSMC", "label": "Fab 18 Analysis", "url": "https://www.tsmc.com"},
                {"source": "JEDEC / HBM", "label": "2026 Generation Standard", "url": "https://www.jedec.org/standards-documents/focus/hbm"}
            ],
            "quant_data": [
                {"label": "HBM4 Yield Rate", "value": "62", "unit": "%"},
                {"label": "Interconnect Bandwidth", "value": "2.4", "unit": "TB/s"},
                {"label": "Power Density", "value": "450", "unit": "W/cm²"}
            ],
            "modelling": "Monte Carlo simulations across 12-inch wafer production lines indicate that unless yields hit 75%, AI accelerator cost-of-goods (COGS) will remain 20% above the 2024 pricing ceiling. This creates a margin squeeze for smaller hyperscalers while favoring vertically integrated incumbents."
        }
    ]
    for entry in research_data:
        db.add(ResearchEntry(**entry))

    print("Seeding Ecosystem Companies...")
    ecosystem_data = [
        # Global Leaders
        {
            "name": "IonQ",
            "category": "Hardware",
            "sub_category": "Trapped Ion",
            "description": "Public leader in trapped-ion quantum computing, providing rack-mounted systems via cloud.",
            "website": "https://ionq.com",
            "location": "USA",
            "headquarters": "College Park, MD",
            "latitude": 38.9897, "longitude": -76.9378,
            "funding_stage": "Public",
            "strategic_relevance": 9,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "IonQ expansion in Seattle for manufacturing facility", "date": "2024-03-12", "url": "https://ionq.com/news"},
                {"title": "Strategic partnership with Air Force Research Lab", "date": "2024-02-15", "url": "https://ionq.com/news"}
            ]
        },
        {
            "name": "PsiQuantum",
            "category": "Hardware",
            "sub_category": "Photonics",
            "description": "Building a utility-scale quantum computer using silicon photonics and standard fab processes.",
            "website": "https://psiquantum.com",
            "location": "USA/Australia",
            "headquarters": "Palo Alto / Brisbane",
            "latitude": -27.4705, "longitude": 153.0260, # Primary focus for the map is their Brisbane hub
            "funding_stage": "Series D",
            "strategic_relevance": 10,
            "trl": 5,
            "is_australian": 1,
            "latest_news": [
                {"title": "PsiQuantum to build world-first fault-tolerant quantum computer in Brisbane", "date": "2024-04-30", "url": "https://psiquantum.com/news"},
                {"title": "Joint investment from Australian and Queensland Governments", "date": "2024-04-30", "url": "https://psiquantum.com/news"}
            ]
        },
        {
            "name": "Rigetti",
            "category": "Hardware",
            "sub_category": "Superconducting",
            "description": "Full-stack quantum computing company specializing in superconducting processors.",
            "website": "https://rigetti.com",
            "location": "USA",
            "headquarters": "Berkeley, CA",
            "latitude": 37.8715, "longitude": -122.2730,
            "funding_stage": "Public",
            "strategic_relevance": 8,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "Rigetti launches 84-qubit Ankaa-2 system", "date": "2024-01-20", "url": "https://rigetti.com/news"}
            ]
        },
        {
            "name": "Xanadu",
            "category": "Hardware",
            "sub_category": "Photonics",
            "description": "Leading photonic quantum computing company and developer of PennyLane software.",
            "website": "https://xanadu.ai",
            "location": "Canada",
            "headquarters": "Toronto, ON",
            "latitude": 43.6532, "longitude": -79.3832,
            "funding_stage": "Series C",
            "strategic_relevance": 9,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "Xanadu and BMW Group simulate battery chemistry", "date": "2024-02-28", "url": "https://xanadu.ai/news"}
            ]
        },
        {
            "name": "Quantinuum",
            "category": "Hardware",
            "sub_category": "Trapped Ion",
            "description": "The world's largest integrated quantum computing company, formed by Honeywell and Cambridge Quantum.",
            "website": "https://quantinuum.com",
            "location": "USA/UK",
            "headquarters": "Broomfield, CO",
            "latitude": 39.9205, "longitude": -105.0867,
            "funding_stage": "Late Stage",
            "strategic_relevance": 10,
            "trl": 7,
            "is_australian": 0,
            "latest_news": [
                {"title": "Quantinuum achieves major fidelity milestone for trapped-ion qubits", "date": "2024-03-05", "url": "https://quantinuum.com/news"}
            ]
        },
        {
            "name": "Alice & Bob",
            "category": "Hardware",
            "sub_category": "Superconducting",
            "description": "Developing self-correcting superconducting quantum bits called Cat Qubits.",
            "website": "https://alice-bob.com",
            "location": "France",
            "headquarters": "Paris",
            "latitude": 48.8566, "longitude": 2.3522,
            "funding_stage": "Series B",
            "strategic_relevance": 9,
            "trl": 4,
            "is_australian": 0,
            "latest_news": [
                {"title": "Alice & Bob unveil roadmap for 100 logical qubits", "date": "2024-03-20", "url": "https://alice-bob.com"}
            ]
        },
        {
            "name": "Pasqal",
            "category": "Hardware",
            "sub_category": "Neutral Atom",
            "description": "European leader in neutral atom quantum computing.",
            "website": "https://pasqal.com",
            "location": "France",
            "headquarters": "Massy",
            "latitude": 48.7308, "longitude": 2.2713,
            "funding_stage": "Series B",
            "strategic_relevance": 9,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "Pasqal delivers first quantum processor to HPC center", "date": "2024-01-15", "url": "https://pasqal.com"}
            ]
        },
        {
            "name": "IQM",
            "category": "Hardware",
            "sub_category": "Superconducting",
            "description": "Pan-European leader in superconducting quantum hardware.",
            "website": "https://meetiqm.com",
            "location": "Finland",
            "headquarters": "Espoo",
            "latitude": 60.2055, "longitude": 24.6559,
            "funding_stage": "Series B",
            "strategic_relevance": 9,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "IQM expands presence in APAC with new office", "date": "2024-02-12", "url": "https://meetiqm.com"}
            ]
        },

        # Australian Ecosystem
        {
            "name": "Silicon Quantum Computing",
            "category": "Hardware",
            "sub_category": "Silicon Spin",
            "description": "Developing atomic-scale quantum integrated circuits in silicon.",
            "website": "https://sqc.com.au",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.9173, "longitude": 151.2313,
            "funding_stage": "Late Stage",
            "strategic_relevance": 10,
            "trl": 4,
            "is_australian": 1,
            "latest_news": [
                {"title": "SQC opens new world-class hardware manufacturing facility", "date": "2024-05-15", "url": "https://sqc.com.au"}
            ]
        },
        {
            "name": "Diraq",
            "category": "Hardware",
            "sub_category": "Silicon Spin",
            "description": "CMOS-compatible silicon spin qubits leveraging standard semiconductor manufacturing.",
            "website": "https://diraq.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.9160, "longitude": 151.2300,
            "funding_stage": "Series A+",
            "strategic_relevance": 9,
            "trl": 4,
            "is_australian": 1,
            "latest_news": [
                {"title": "Diraq raises $15M to accelerate hardware roadmap", "date": "2024-02-20", "url": "https://diraq.com"}
            ]
        },
        {
            "name": "Quantum Brilliance",
            "category": "Hardware",
            "sub_category": "Diamond NV",
            "description": "Room-temperature quantum computing using nitrogen-vacancy centers in diamonds.",
            "website": "https://quantumbrilliance.com",
            "location": "Australia/Germany",
            "headquarters": "Canberra, ACT",
            "latitude": -35.2809, "longitude": 149.1300,
            "funding_stage": "Series A",
            "strategic_relevance": 8,
            "trl": 5,
            "is_australian": 1,
            "latest_news": [
                {"title": "Quantum Brilliance mini-computer named TIME Best Invention 2025", "date": "2025-10-30", "url": "https://quantumbrilliance.com"}
            ]
        },
        {
            "name": "Q-CTRL",
            "category": "Software",
            "sub_category": "Control Systems",
            "description": "The quantum infrastructure software company, specializing in error suppression and performance.",
            "website": "https://q-ctrl.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8688, "longitude": 151.2093,
            "funding_stage": "Series B+",
            "strategic_relevance": 10,
            "trl": 7,
            "is_australian": 1,
            "latest_news": [
                {"title": "Q-CTRL raises $166M in record-setting funding round", "date": "2024-10-15", "url": "https://q-ctrl.com"}
            ]
        },
        {
            "name": "QuantX Labs",
            "category": "Sensing",
            "sub_category": "Metrology",
            "description": "Precision timing and sensing solutions, including the Cryoclock.",
            "website": "https://quantxlabs.com",
            "location": "Australia",
            "headquarters": "Adelaide, SA",
            "latitude": -34.9285, "longitude": 138.6007,
            "funding_stage": "Late Stage",
            "strategic_relevance": 9,
            "trl": 7,
            "is_australian": 1,
            "latest_news": [
                {"title": "QuantX Labs secures defense contract for precision timing", "date": "2024-03-10", "url": "https://quantxlabs.com"}
            ]
        },
        {
            "name": "Nomad Atomics",
            "category": "Sensing",
            "sub_category": "Metrology",
            "description": "Quantum gravimetry and inertial sensing for resource management.",
            "website": "https://nomadatomics.com",
            "location": "Australia",
            "headquarters": "Canberra, ACT",
            "latitude": -35.2400, "longitude": 149.1000,
            "funding_stage": "Series A",
            "strategic_relevance": 7,
            "trl": 5,
            "is_australian": 1,
            "latest_news": [
                {"title": "Nomad Atomics field-tests gravimeter in mining environment", "date": "2024-02-15", "url": "https://nomadatomics.com"}
            ]
        },
        {
            "name": "Advanced Navigation",
            "category": "Sensing",
            "sub_category": "PNT",
            "description": "Inertial navigation systems utilizing quantum-enhanced sensing.",
            "website": "https://advancednavigation.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8000, "longitude": 151.1000,
            "funding_stage": "Late Stage",
            "strategic_relevance": 9,
            "trl": 7,
            "is_australian": 1,
            "latest_news": [
                {"title": "Advanced Navigation expands manufacturing in NSW", "date": "2024-01-20", "url": "https://advancednavigation.com"}
            ]
        },
        {
            "name": "Archer Materials",
            "category": "Hardware",
            "sub_category": "Bio-sensing",
            "description": "Developing 12CQ chip for mobile quantum computing and bio-sensing applications.",
            "website": "https://archerx.com.au",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8500, "longitude": 151.2000,
            "funding_stage": "Public",
            "strategic_relevance": 8,
            "trl": 4,
            "is_australian": 1,
            "latest_news": [
                {"title": "Archer achieves breakthrough in chip fabrication", "date": "2024-03-05", "url": "https://archerx.com.au"}
            ]
        },
        {
            "name": "QuintessenceLabs",
            "category": "Comms",
            "sub_category": "Cybersecurity",
            "description": "Quantum-safe encryption and key distribution (QKD) market leader.",
            "website": "https://quintessencelabs.com",
            "location": "Australia",
            "headquarters": "Canberra, ACT",
            "latitude": -35.3000, "longitude": 149.1500,
            "funding_stage": "Late Stage",
            "strategic_relevance": 9,
            "trl": 8,
            "is_australian": 1,
            "latest_news": [
                {"title": "QuintessenceLabs partners with global defense prime", "date": "2024-02-25", "url": "https://quintessencelabs.com"}
            ]
        },
        {
            "name": "Redback Systems",
            "category": "Software",
            "sub_category": "Spectral Analysis",
            "description": "High-precision spectroscopic instruments and quantum hardware tools.",
            "website": "https://redbacksystems.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.9100, "longitude": 151.2100,
            "funding_stage": "Venture",
            "strategic_relevance": 7,
            "trl": 6,
            "is_australian": 1,
            "latest_news": [
                {"title": "Redback Systems launches new spectroscopic platform", "date": "2024-03-12", "url": "https://redbacksystems.com"}
            ]
        },
        {
            "name": "Liquid Instruments",
            "category": "Sensing",
            "sub_category": "Test & Measurement",
            "description": "FPGA-based reconfigurable test equipment for quantum labs.",
            "website": "https://liquidinstruments.com",
            "location": "Australia/USA",
            "headquarters": "Canberra, ACT",
            "latitude": -35.2500, "longitude": 149.0500,
            "funding_stage": "Series B",
            "strategic_relevance": 8,
            "trl": 8,
            "is_australian": 1,
            "latest_news": [
                {"title": "Liquid Instruments raises $28M for Moku platform expansion", "date": "2024-01-30", "url": "https://liquidinstruments.com"}
            ]
        },
        {
            "name": "CatQ",
            "category": "Software",
            "sub_category": "Error Correction",
            "description": "Specializing in photonic quantum error correction codes.",
            "website": "https://catq.ai",
            "location": "Australia",
            "headquarters": "Melbourne, VIC",
            "latitude": -37.8136, "longitude": 144.9631,
            "funding_stage": "Seed",
            "strategic_relevance": 8,
            "trl": 3,
            "is_australian": 1,
            "latest_news": [
                {"title": "CatQ joins Quantum Australia accelerator", "date": "2024-02-10", "url": "https://catq.ai"}
            ]
        },
        {
            "name": "Eigensystems",
            "category": "Software",
            "sub_category": "Education",
            "description": "Quantum education and simulation platforms for industry training.",
            "website": "https://eigensystems.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8700, "longitude": 151.2000,
            "funding_stage": "Venture",
            "strategic_relevance": 6,
            "trl": 7,
            "is_australian": 1,
            "latest_news": [
                {"title": "Eigensystems announces national quantum workforce initiative", "date": "2024-03-15", "url": "https://eigensystems.com"}
            ]
        },
        {
            "name": "Deteqt",
            "category": "Sensing",
            "sub_category": "Navigation",
            "description": "Compact quantum sensors for GPS-denied navigation.",
            "website": "https://deteqt.au",
            "location": "Australia",
            "headquarters": "Melborne, VIC",
            "latitude": -37.8200, "longitude": 144.9500,
            "funding_stage": "Seed",
            "strategic_relevance": 8,
            "trl": 4,
            "is_australian": 1,
            "latest_news": [
                {"title": "Deteqt wins Air Force innovation challenge", "date": "2024-04-05", "url": "https://deteqt.au"}
            ]
        },
        {
            "name": "Chromos Labs",
            "category": "Sensing",
            "sub_category": "Imaging",
            "description": "Next-generation quantum imaging systems for biomedical and industrial use.",
            "website": "https://chromoslabs.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.9000, "longitude": 151.1500,
            "funding_stage": "Venture",
            "strategic_relevance": 7,
            "trl": 5,
            "is_australian": 1,
            "latest_news": [
                {"title": "Chromos Labs secures research funding for medical imaging", "date": "2024-02-18", "url": "https://chromoslabs.com"}
            ]
        },
        {
            "name": "Elemental Instruments",
            "category": "Software",
            "sub_category": "Simulation",
            "description": "Advanced modeling and simulation for quantum materials discovery.",
            "website": "https://elementalinstruments.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8800, "longitude": 151.2200,
            "funding_stage": "Seed",
            "strategic_relevance": 7,
            "trl": 4,
            "is_australian": 1,
            "latest_news": [
                {"title": "Elemental Instruments launches materials discovery suite", "date": "2024-03-25", "url": "https://elementalinstruments.com"}
            ]
        },
        {
            "name": "BluGlass",
            "category": "Comms",
            "sub_category": "Photonics",
            "description": "Semiconductor laser technology for quantum communications and sensing.",
            "website": "https://bluglass.com.au",
            "location": "Australia",
            "headquarters": "Silverwater, NSW",
            "latitude": -33.8341, "longitude": 151.0560,
            "funding_stage": "Public",
            "strategic_relevance": 8,
            "trl": 8,
            "is_australian": 1,
            "latest_news": [
                {"title": "BluGlass receives first commercial orders for quantum lasers", "date": "2024-02-10", "url": "https://bluglass.com.au"}
            ]
        },
        {
            "name": "Silanna Group",
            "category": "Comms",
            "sub_category": "Semiconductors",
            "description": "Supplying critical semiconductor components for quantum-enabling systems.",
            "website": "https://silanna.com",
            "location": "Australia",
            "headquarters": "Brisbane, QLD",
            "latitude": -27.4700, "longitude": 153.0200,
            "funding_stage": "Private",
            "strategic_relevance": 8,
            "trl": 9,
            "is_australian": 1,
            "latest_news": [
                {"title": "Silanna expands production capacity for UV emitters", "date": "2024-01-15", "url": "https://silanna.com"}
            ]
        },
        {
            "name": "Endo Axiom",
            "category": "Sensing",
            "sub_category": "Bio-tech",
            "description": "Quantum dot nanoparticles for oral insulin delivery.",
            "website": "https://endoaxiom.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8900, "longitude": 151.1800,
            "funding_stage": "Seed",
            "strategic_relevance": 6,
            "trl": 3,
            "is_australian": 1,
            "latest_news": [
                {"title": "Endo Axiom spinout from USYD attracts healthcare VC", "date": "2024-02-28", "url": "https://endoaxiom.com"}
            ]
        },
        {
            "name": "Iceberg Quantum",
            "category": "Hardware",
            "sub_category": "Cryogenics",
            "description": "Specializing in cryostat components and enabling systems for quantum processors.",
            "website": "https://icebergquantum.com",
            "location": "Australia",
            "headquarters": "Melbourne, VIC",
            "latitude": -37.8300, "longitude": 144.9700,
            "funding_stage": "Venture",
            "strategic_relevance": 7,
            "trl": 5,
            "is_australian": 1,
            "latest_news": [
                {"title": "Iceberg Quantum completes new low-vibration dilution fridge test", "date": "2024-03-22", "url": "https://icebergquantum.com"}
            ]
        },
        {
            "name": "Emergence Quantum",
            "category": "Hardware",
            "sub_category": "Components",
            "description": "Scalable quantum processor platforms and enabling components.",
            "website": "https://emergencequantum.com",
            "location": "Australia",
            "headquarters": "Sydney, NSW",
            "latitude": -33.8600, "longitude": 151.1900,
            "funding_stage": "Seed",
            "strategic_relevance": 7,
            "trl": 4,
            "is_australian": 1,
            "latest_news": [
                {"title": "Emergence Quantum announces seed round for platform development", "date": "2024-04-12", "url": "https://emergencequantum.com"}
            ]
        },
        {
            "name": "IBM Quantum",
            "category": "Hardware",
            "sub_category": "Superconducting",
            "description": "Global leader in utility-scale quantum computing with the IBM Quantum System Two.",
            "website": "https://ibm.com/quantum",
            "location": "USA",
            "headquarters": "Yorktown Heights, NY",
            "latitude": 41.2081, "longitude": -73.7149,
            "funding_stage": "Public",
            "strategic_relevance": 10,
            "trl": 7,
            "is_australian": 0,
            "latest_news": [
                {"title": "IBM Quantum System Two now operational in NY", "date": "2024-01-10", "url": "https://ibm.com/quantum"}
            ]
        },
        {
            "name": "Google Quantum AI",
            "category": "Hardware",
            "sub_category": "Superconducting",
            "description": "Developing error-corrected quantum computers using Sycamore processors.",
            "website": "https://quantumai.google",
            "location": "USA",
            "headquarters": "Santa Barbara, CA",
            "latitude": 34.4208, "longitude": -119.6982,
            "funding_stage": "Public",
            "strategic_relevance": 10,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "Google Quantum AI publishes result on error correction scaling", "date": "2024-02-22", "url": "https://quantumai.google"}
            ]
        },
        {
            "name": "Microsoft Azure Quantum",
            "category": "Software",
            "sub_category": "Cloud Platform",
            "description": "Providing a comprehensive cloud-based ecosystem for quantum development and simulation.",
            "website": "https://azure.microsoft.com/quantum",
            "location": "USA",
            "headquarters": "Redmond, WA",
            "latitude": 47.6740, "longitude": -122.1215,
            "funding_stage": "Public",
            "strategic_relevance": 10,
            "trl": 7,
            "is_australian": 0,
            "latest_news": [
                {"title": "Microsoft and Quantinuum demonstrate logical qubits on Azure", "date": "2024-04-03", "url": "https://microsoft.com"}
            ]
        },
        {
            "name": "Bluefors",
            "category": "Hardware",
            "sub_category": "Cryogenics",
            "description": "World leader in ultra-low temperature cooling systems for quantum technology.",
            "website": "https://bluefors.com",
            "location": "Finland",
            "headquarters": "Helsinki",
            "latitude": 60.1699, "longitude": 24.9384,
            "funding_stage": "Private",
            "strategic_relevance": 10,
            "trl": 9,
            "is_australian": 0,
            "latest_news": [
                {"title": "Bluefors opens new R&D center for next-gen dilution refrigerators", "date": "2024-02-15", "url": "https://bluefors.com"}
            ]
        },
        {
            "name": "Riverlane",
            "category": "Software",
            "sub_category": "Error Correction",
            "description": "Building the Operating System for error-corrected quantum computers.",
            "website": "https://riverlane.com",
            "location": "UK",
            "headquarters": "Cambridge",
            "latitude": 52.2053, "longitude": 0.1218,
            "funding_stage": "Series B",
            "strategic_relevance": 9,
            "trl": 5,
            "is_australian": 0,
            "latest_news": [
                {"title": "Riverlane partners with Rigetti on error correction implementation", "date": "2024-03-12", "url": "https://riverlane.com"}
            ]
        },
        {
            "name": "Multiverse Computing",
            "category": "Software",
            "sub_category": "Finance",
            "description": "Specializing in quantum and quantum-inspired algorithms for finance and industry.",
            "website": "https://multiversecomputing.com",
            "location": "Spain",
            "headquarters": "San Sebastian",
            "latitude": 43.3183, "longitude": -1.9812,
            "funding_stage": "Series A",
            "strategic_relevance": 8,
            "trl": 6,
            "is_australian": 0,
            "latest_news": [
                {"title": "Multiverse Computing named one of the fastest-growing startups in Europe", "date": "2024-03-25", "url": "https://multiversecomputing.com"}
            ]
        },
        {
            "name": "Nordic Quantum Computing Group",
            "category": "Hardware",
            "sub_category": "Consulting",
            "description": "Advisory and software development for the Nordic quantum ecosystem.",
            "website": "https://nqcg.com",
            "location": "Norway",
            "headquarters": "Oslo",
            "latitude": 59.9139, "longitude": 10.7522,
            "funding_stage": "Venture",
            "strategic_relevance": 6,
            "trl": 5,
            "is_australian": 0,
            "latest_news": [
                {"title": "NQCG enters partnership for regional quantum infrastructure", "date": "2024-02-05", "url": "https://nqcg.com"}
            ]
        }
    ]
    for company in ecosystem_data:
        db.add(EcosystemCompany(**company))

    db.commit()
    print("Regional data seeded successfully.")
    db.close()

if __name__ == "__main__":
    seed_data()
