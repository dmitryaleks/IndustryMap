# Chapter 2: How a Chip Is Made

> Understanding the semiconductor manufacturing process -- from raw silicon to packaged IC -- is essential to understanding why certain companies hold chokepoint positions in the supply chain.

## Introduction

Before we can map the companies that dominate the semiconductor supply chain, we need to understand what they actually do. This chapter walks through the entire chip manufacturing process, from a handful of purified sand to a finished integrated circuit ready to be soldered onto a circuit board. No company names appear here -- those come later. The goal is purely conceptual: to build a mental model of the dozens of interlocking process steps, to understand why each one matters, and to see why failures at any single stage can cascade into billions of dollars in lost production.

A modern semiconductor fabrication facility -- a "fab" -- is arguably the most complex manufacturing environment ever constructed by humans. The products it creates have features measured in nanometers, a scale where individual atoms become relevant. The air inside a fab is thousands of times cleaner than a hospital operating room. The water it uses is purer than anything found in nature. And the sequence of chemical, thermal, optical, and mechanical processes that transforms a blank silicon disc into a functioning processor can involve more than a thousand individual steps executed over the course of two to three months.

This chapter is the vocabulary lesson. Every technical term introduced here -- lithography, deposition, etching, CMP, dicing -- will reappear throughout the rest of this book, attached to specific companies and specific competitive dynamics. Consider this your reference map for the territory we are about to explore.

## From Sand to Silicon

### Purifying Silicon

Silicon is the second most abundant element in the Earth's crust, exceeded only by oxygen. It is found everywhere as silicon dioxide -- silica -- the principal component of ordinary sand. But the silicon used in semiconductor manufacturing is not ordinary. It must be purified to a level of 99.999999999% (eleven nines) purity, meaning fewer than one foreign atom per hundred billion silicon atoms.

The purification process begins with metallurgical-grade silicon, produced by reducing quartz (SiO2) in an electric arc furnace with carbon at temperatures exceeding 1,800 degrees Celsius. This material is roughly 98-99% pure -- adequate for making steel alloys, but many orders of magnitude too dirty for semiconductors.

The next step converts this crude silicon into trichlorosilane (SiHCl3), a liquid that can be fractionally distilled to remove impurities. The purified trichlorosilane is then decomposed in a process called the Siemens method, depositing ultra-high-purity polycrystalline silicon ("polysilicon") onto heated silicon rods. This polysilicon feedstock is the starting material for wafer production.

### Crystal Growth and Wafer Preparation

Semiconductor devices require not just pure silicon, but silicon arranged in a perfect single-crystal lattice -- a uniform, unbroken grid of atoms extending across the entire wafer. This is achieved through the Czochralski (CZ) process, named after the Polish chemist who invented it in 1916.

In the CZ process, polysilicon is melted in a quartz crucible at approximately 1,425 degrees Celsius, just above silicon's melting point. A small seed crystal -- itself a perfect single crystal -- is dipped into the melt and slowly withdrawn while rotating. As it rises, molten silicon solidifies onto the seed, extending the crystal structure. Over a period of several days, this produces a cylindrical ingot (or "boule") of single-crystal silicon, typically 300 millimeters (about 12 inches) in diameter and up to two meters long, weighing several hundred kilograms.

The ingot is then sliced into thin, circular wafers using diamond-edged wire saws. Each wafer is approximately 775 micrometers thick -- roughly the thickness of three or four sheets of paper. The wafers are lapped, etched, and polished to an extraordinary degree of flatness. The final surface must be smooth to within a few angstroms (tenths of a nanometer) -- a level of flatness so extreme that if a 300mm wafer were scaled up to the size of a football pitch, the largest bump on its surface would be less than a millimeter tall.

These polished, mirror-finish wafers are the blank canvases upon which all semiconductor devices are built.

## Front-End Processing: Wafer Fabrication

Front-end processing is where the transistors, interconnects, and other circuit elements are created on the wafer surface. This is the most technologically demanding phase of chip manufacturing, typically accounting for 60-70% of the total cost. A single 300mm wafer may carry hundreds of individual chips (called "dies"), and the entire wafer is processed simultaneously -- every die receiving the same sequence of treatments.

The fundamental approach is subtractive and additive in alternation: deposit a layer of material, pattern it using light, remove the unwanted portions, and repeat. A leading-edge logic chip at the 3-nanometer node requires more than 80 lithography layers and well over a thousand total process steps, built up over eight to twelve weeks of continuous fabrication.

### Oxidation

Silicon has a remarkable property: when exposed to oxygen or steam at high temperatures (800-1,200 degrees Celsius), it grows a thin, stable, electrically insulating layer of silicon dioxide (SiO2) on its surface. This thermal oxide is one of the key reasons silicon became the dominant semiconductor material -- no other semiconductor grows such a high-quality native insulator.

Thermal oxidation is used to create gate oxides for transistors, isolation layers between devices, and protective passivation layers. The thickness of these oxide layers must be controlled with sub-nanometer precision. A gate oxide at advanced nodes may be only a few atoms thick -- roughly 1-2 nanometers -- and variations of even a single atomic layer can alter a transistor's electrical characteristics.

### Lithography: Printing the Circuit

Lithography is the defining process step in semiconductor manufacturing. It is the step that determines the minimum feature size -- and therefore the transistor density, performance, and power efficiency -- of the finished chip. If you understand one semiconductor process step, it should be this one.

The concept is analogous to photography, or more precisely to photographic printing. A pattern -- the circuit layout for one layer of the chip -- is encoded on a glass plate called a photomask (or reticle). Light is projected through this mask and focused by a complex lens system onto the wafer surface, which has been coated with a light-sensitive polymer called photoresist. Where the light strikes the resist, it changes the resist's chemical solubility. The wafer is then "developed" in a chemical bath, dissolving away either the exposed or unexposed resist (depending on whether the resist is "positive" or "negative"), leaving behind a precise pattern that serves as a stencil for subsequent etching or deposition.

The analogy breaks down when you consider the scale. Lithography is like projecting a photograph onto a surface, except the photograph has features smaller than a virus, the projection must be aligned to the previous layer with an accuracy of about one nanometer, and the entire exposure must be completed in a fraction of a second per die to maintain economically viable throughput.

Two major lithography technologies dominate modern fabs:

**Deep ultraviolet (DUV) lithography** uses light at wavelengths of 248 nanometers (KrF excimer laser) or 193 nanometers (ArF excimer laser). At the most advanced DUV nodes, immersion lithography places a thin film of ultrapure water between the lens and the wafer, shortening the effective wavelength and enabling resolution below 40 nanometers. DUV with immersion and multi-patterning techniques (exposing the same layer multiple times with shifted patterns) pushed the industry all the way to the 7-nanometer node, though at escalating cost and complexity.

**Extreme ultraviolet (EUV) lithography** uses light at 13.5 nanometers -- a wavelength so short that it is absorbed by air and by glass, requiring the entire optical path to operate in a near-perfect vacuum and use reflective mirrors rather than lenses. EUV eliminates the need for multi-patterning at advanced nodes, simplifying the process but demanding entirely new infrastructure: different light sources, different masks, different resist chemistries. EUV scanners are the most expensive single machines in any fab, costing upward of $200 million each, and they are produced by a single manufacturer in the world.

Each lithography exposure must be aligned to the patterns already on the wafer with overlay accuracy better than 1-2 nanometers. Consider what this means: the wafer is 300mm across, and the pattern must be placed with an error smaller than the width of a few silicon atoms. This is equivalent to placing a sticker on a surface the size of a city and getting the position right to within the width of a human hair.

### Etching: Removing Material

After lithography has defined a pattern in photoresist, etching transfers that pattern into the underlying material -- oxide, metal, polysilicon, or other films. The resist acts as a protective mask: wherever resist remains, the underlying material is preserved; wherever resist has been removed, the underlying material is attacked.

There are two primary etching methods:

**Wet etching** immerses the wafer in a liquid chemical bath that dissolves the target material. It is isotropic, meaning it etches in all directions equally, which limits its use for features smaller than about one micrometer. Wet etching remains important for cleaning, surface preparation, and removing sacrificial layers.

**Dry etching** (plasma etching or reactive ion etching) uses ionized gases in a vacuum chamber to bombard the wafer surface. The energetic ions can be directed almost vertically, enabling anisotropic etching -- cutting straight down into the material with nearly vertical sidewalls. This directional control is essential for defining the steep, narrow features required at advanced nodes, where a transistor gate may be only 5-7 nanometers wide.

A critical parameter in etching is selectivity: the ratio of the etch rate of the target material to the etch rate of surrounding materials. High selectivity means the etchant removes only what it is supposed to remove, leaving everything else untouched. Achieving selectivity greater than 100:1 for certain film stacks is a persistent engineering challenge.

### Deposition: Adding Thin Films

Where etching removes material, deposition adds it. Thin films of metals, insulators, and semiconductors are deposited onto the wafer surface at various stages of fabrication. The major deposition techniques include:

**Chemical vapor deposition (CVD)** introduces gaseous precursors into a reaction chamber, where they undergo chemical reactions on the wafer surface to form a solid film. CVD is used to deposit silicon dioxide, silicon nitride, tungsten, and many other materials. Variants include low-pressure CVD (LPCVD), plasma-enhanced CVD (PECVD), and metal-organic CVD (MOCVD), each optimized for different materials and process conditions.

**Physical vapor deposition (PVD)**, commonly called sputtering, physically ejects atoms from a solid target using a plasma, depositing them onto the wafer. PVD is the primary method for depositing metals like aluminum, copper barrier layers (tantalum, tantalum nitride), and titanium.

**Atomic layer deposition (ALD)** deposits material one atomic layer at a time, using sequential, self-limiting chemical reactions. ALD provides unparalleled thickness control and conformality -- the ability to coat complex three-dimensional structures uniformly. At the 5nm node and below, where gate dielectrics may be only 10-20 atoms thick and transistor structures are highly non-planar (FinFET, gate-all-around), ALD has become indispensable.

**Epitaxy** grows a crystalline film on a crystalline substrate such that the deposited film continues the crystal structure of the substrate. Silicon epitaxy and silicon-germanium (SiGe) epitaxy are used to engineer the channel regions of advanced transistors, tuning carrier mobility for higher performance.

### Ion Implantation: Doping

A pure silicon crystal is a poor conductor of electricity. To create the p-type and n-type regions that form the building blocks of transistors, controlled quantities of impurity atoms -- "dopants" -- must be introduced into the silicon lattice. Boron is the most common p-type dopant; phosphorus and arsenic are common n-type dopants.

Ion implantation achieves this by ionizing dopant atoms and accelerating them in an electric field to energies ranging from a few hundred electron volts to several million electron volts. These high-energy ions are fired into the wafer surface, embedding themselves at precisely controlled depths. The dose (total number of ions per square centimeter) and energy (determining implant depth) can both be controlled with high accuracy.

After implantation, the crystal lattice is damaged by the impacts. A subsequent high-temperature annealing step -- typically a rapid thermal process lasting only a few seconds at 1,000-1,100 degrees Celsius -- repairs the lattice and electrically activates the dopant atoms, placing them into substitutional positions within the crystal structure.

### CMP: Chemical Mechanical Planarization

As layers are built up on the wafer surface -- oxide, metal, more oxide, more metal -- the topography becomes increasingly uneven. Hills and valleys develop, mirroring the circuit features underneath. This is a problem because lithography requires an extremely flat surface: the depth of focus for EUV lithography is only about 45 nanometers, meaning the surface must be flat to within that tolerance or the projected image will be out of focus and the pattern will be ruined.

CMP solves this by simultaneously polishing (mechanical) and dissolving (chemical) the wafer surface. The wafer is pressed face-down against a rotating pad while a slurry -- a carefully engineered mixture of abrasive nanoparticles and reactive chemicals -- is fed onto the pad. The combination of mechanical abrasion and chemical attack removes material from the high points faster than from the low points, gradually planarizing the surface to angstrom-level flatness.

CMP is used after almost every metal deposition step (to remove excess metal and create flat interconnect layers) and at many other points in the process flow. The slurry chemistry must be tuned precisely for each material -- copper CMP slurry is very different from oxide CMP slurry or tungsten CMP slurry. And the process must remove exactly the right amount of material: too little, and the surface is still uneven; too much, and the underlying features are damaged.

### Cleaning

Contamination is the enemy of semiconductor manufacturing. A single particle a few tens of nanometers in diameter -- far too small to see with an optical microscope -- can bridge a circuit trace and cause a short circuit, destroying a die. A few parts per billion of metallic contamination (sodium, iron, copper) can alter transistor threshold voltages and cause device failure.

Consequently, wafers are cleaned between essentially every process step. A modern fab may perform 200 or more cleaning steps during the fabrication of a single chip. The primary cleaning agent is ultrapure water (UPW) with a resistivity of 18.2 megaohm-centimeters -- water so pure that it contains virtually no dissolved ions, organic molecules, or particles. Specialty cleaning chemicals -- dilute hydrofluoric acid, ammonium hydroxide/hydrogen peroxide mixtures (SC-1), hydrochloric acid/hydrogen peroxide mixtures (SC-2), sulfuric acid/hydrogen peroxide mixtures (SPM) -- are used in prescribed sequences to remove specific classes of contaminants.

The volume of ultrapure water consumed by a modern fab is staggering: a large 300mm fab may use 30,000 to 40,000 cubic meters of UPW per day -- enough to fill a dozen Olympic swimming pools.

### Metrology and Inspection

You cannot control what you cannot measure. Between process steps, wafers undergo a battery of measurements and inspections to verify that each step was executed correctly.

**Critical dimension (CD) metrology** measures the width and shape of patterned features using scanning electron microscopy (CD-SEM) or optical scatterometry (OCD). At the 3nm node, features must be measured with sub-angstrom precision.

**Overlay metrology** verifies that each lithography layer is aligned to the previous layers within the required tolerance (typically less than 2 nanometers).

**Film thickness metrology** measures deposited films using ellipsometry, reflectometry, or X-ray techniques, verifying that coatings are within specification (often plus or minus 1-2%).

**Defect inspection** scans the wafer surface for particles, scratches, pattern defects, and other anomalies using bright-field and dark-field optical inspection systems or electron-beam inspection. Modern inspection tools can detect defects as small as 10-15 nanometers.

**Electrical test structures** -- small test circuits included on the wafer alongside the actual product dies -- provide real-time feedback on transistor performance, interconnect resistance, and other electrical parameters.

Metrology and inspection are not merely quality-control checkpoints; they are integral to the manufacturing process itself. The data they generate feeds back into process controllers that adjust recipe parameters in real time, keeping the process within its narrow window of acceptable variation.

## Back-End Processing: Assembly and Test

Once front-end processing is complete, the wafer contains hundreds of finished dies -- but they are still part of a single silicon disc and have not yet been tested or packaged for use. Back-end processing transforms the wafer into individual, packaged integrated circuits ready for integration into electronic systems.

### Wafer Test and Probing

Before the wafer is cut apart, each die is electrically tested while still on the wafer. A probe card -- an array of microscopic needles or contact pads -- is brought into contact with the bond pads of each die, and automated test equipment (ATE) applies a sequence of electrical stimuli, measuring the die's responses against expected values.

Dies that fail are marked (traditionally with a small ink dot, now tracked digitally) and will be discarded after dicing. This step is critical for yield economics: it prevents the waste of expensive packaging materials on defective dies. For advanced logic chips that may cost $50-100 per die in wafer processing costs, identifying failures at the wafer level saves substantial money.

### Dicing and Singulation

The tested wafer must be cut into individual dies. The wafer is first mounted on a flexible adhesive tape stretched across a metal frame, then cut using one of several methods:

**Blade dicing** uses a thin diamond-impregnated spinning blade (typically 20-30 micrometers wide) to saw through the silicon along the streets -- the narrow lanes of empty space between dies. This is the traditional method and remains dominant for most applications.

**Laser dicing** uses a focused laser beam to cut or scribe the wafer. Stealth dicing, a particularly elegant variant, focuses the laser inside the silicon to create a layer of internal damage without affecting the surface; the wafer is then expanded on its tape and cleanly separates along the damaged plane. Laser methods can produce narrower cuts (saving wafer area), eliminate chipping, and handle thin wafers that would crack under blade stress.

The quality of the dicing process matters more than one might expect. Chipping, cracking, or subsurface damage along the die edges can propagate over time, causing latent reliability failures. For safety-critical applications in automotive or medical devices, dicing quality is a qualification parameter.

### Packaging

A bare die is fragile, sensitive to moisture and contamination, and has no practical way to connect to a circuit board. Packaging provides mechanical protection, environmental sealing, electrical connections to the outside world, and thermal dissipation.

Traditional packaging involves several steps:

1. **Die attach**: The die is bonded to a substrate or lead frame using an adhesive or solder.
2. **Wire bonding**: Thin gold or copper wires (typically 18-25 micrometers in diameter) connect the bond pads on the die to the leads on the package. Alternatively, **flip-chip bonding** mounts the die face-down, using solder bumps on the die surface to connect directly to the substrate, providing shorter interconnect paths and better electrical performance.
3. **Encapsulation**: The assembly is covered with a protective epoxy molding compound, shielding the die and wires from moisture, particles, and mechanical damage.
4. **Lead forming and marking**: External leads are shaped, and the package is laser-marked with identification information.

### Advanced Packaging

As transistor scaling has slowed and the demand for performance has accelerated -- driven particularly by artificial intelligence workloads -- the semiconductor industry has increasingly turned to advanced packaging as a way to improve system performance without relying solely on smaller transistors.

**Chiplet architectures** decompose a large, monolithic die into several smaller dies (chiplets), each potentially manufactured on a different process node optimized for its function. These chiplets are then reassembled into a single package, connected by high-bandwidth interconnects. This approach improves manufacturing yield (smaller dies have higher yield), enables mix-and-match combinations of logic, memory, and I/O, and allows reuse of proven chiplet designs across product lines.

**2.5D integration** places multiple chiplets side by side on a silicon interposer -- a thin slab of silicon containing through-silicon vias (TSVs) and a dense network of interconnect wiring. The interposer acts as a high-bandwidth communication highway between the chiplets. One prominent implementation of this approach stacks high-bandwidth memory (HBM) alongside a logic die on a shared interposer, providing memory bandwidth several times greater than conventional approaches.

**3D integration** stacks dies directly on top of each other, connected vertically by TSVs. This minimizes the interconnect distance and footprint but introduces challenges in thermal management (heat from the bottom die must dissipate through the stack) and in testing (each layer must be verified before stacking, since rework after bonding is impractical).

**HBM (High Bandwidth Memory)** stacks multiple DRAM dies vertically using TSVs and micro-bumps, topped by a logic die that manages the memory interface. Current-generation HBM can stack 8-12 DRAM layers, providing memory bandwidth exceeding 1 terabyte per second -- a critical enabler for AI training and inference accelerators.

These advanced packaging techniques require new equipment (thermocompression bonders, hybrid bonding tools), new materials (underfill, advanced substrates, redistribution layers), and new inspection capabilities. Packaging, once considered the least technically demanding part of chip manufacturing, has become one of its most important frontiers.

### Final Test

After packaging, each IC undergoes final electrical testing. This is more comprehensive than wafer-level testing because it verifies the performance of the complete packaged device, including the effects of the packaging itself (parasitic inductance and capacitance from the leads, thermal behavior, signal integrity).

Final test typically includes functional testing (does the chip perform its intended function?), parametric testing (do electrical parameters like speed, power consumption, and voltage thresholds meet specifications?), and burn-in for high-reliability applications (operating the device at elevated temperature and voltage for hours to accelerate early-life failures and weed out marginal parts).

## The Iteration Problem

The process flow described above -- oxidation, lithography, etching, deposition, implantation, CMP, cleaning, inspection -- is not executed once. It is executed dozens of times in sequence, building up the chip layer by layer. A modern logic chip at the 3nm node has more than 80 lithography layers, each requiring its own mask, its own resist coating, its own exposure, its own development, its own etching step, and its own cleaning and inspection. Including all non-lithographic steps, the total process step count can exceed 1,000-1,500 individual operations.

Each of these steps must be executed within extraordinarily tight specifications. A lithography exposure must place its pattern within 1-2 nanometers of the correct position. A deposited film must be within 1-2% of its target thickness. A CMP step must planarize the surface to within a few angstroms. An etching step must cut to the correct depth with the correct profile. And each step must accomplish this not on one die, but uniformly across all several hundred dies on a 300mm wafer, and repeatably across wafer after wafer, day after day, for months.

This is why **yield** -- the percentage of dies on a wafer that function correctly -- is the central economic variable in semiconductor manufacturing. A fab producing chips at a 90% yield gets roughly 10% more good chips per wafer than a fab running at 80% yield, which directly translates to 10% lower cost per chip (since wafer processing costs are fixed regardless of how many good dies come out). At the leading edge, where a single 300mm wafer of finished chips may be worth $20,000-50,000, even a one-percentage-point yield improvement can mean tens of millions of dollars per year in additional revenue.

Yield is the product of the yields of every individual process step. If a chip has 1,000 process steps, each with 99.99% yield (a seemingly excellent figure), the cumulative yield is 0.9999 raised to the 1,000th power -- roughly 90.5%. If any step degrades to 99.9% yield, the cumulative yield drops to approximately 37%. This mathematical reality explains the semiconductor industry's obsessive focus on process control, contamination prevention, and equipment reliability. Every step matters. Every particle matters. Every nanometer matters.

## The Fab: Infrastructure for Extreme Manufacturing

The factory that houses all of this -- the fab -- is itself an extraordinary piece of engineering, often costing $15-25 billion to build and equip for leading-edge production.

### Cleanroom

The fab floor is a cleanroom rated at ISO Class 1 or better in the most critical areas -- meaning fewer than 10 particles larger than 0.1 micrometers per cubic meter of air. For comparison, the outdoor air in a typical city contains roughly 35 million particles of that size per cubic meter. Achieving this level of cleanliness requires massive air handling systems that recirculate and filter the entire volume of cleanroom air hundreds of times per hour through ultra-low-penetration air (ULPA) filters.

Personnel are a major source of contamination. Fab workers wear full-body "bunny suits" -- coveralls, hoods, gloves, boots, and face masks -- that contain the millions of skin cells, hair fragments, and other particles that the human body constantly sheds. In the most advanced fabs, humans rarely touch the wafers directly; automated systems move wafers in sealed pods (FOUPs -- Front Opening Unified Pods) between tools.

### Ultrapure Water

As noted above, modern fabs consume enormous quantities of ultrapure water. The UPW system typically receives municipal water and subjects it to a multi-stage purification process: pre-filtration, reverse osmosis, ion exchange, degasification, ultraviolet oxidation, and final ultra-filtration. The target is a resistivity of 18.2 megaohm-centimeters (the theoretical maximum for pure water), a total organic carbon level below 1 part per billion, and a particle count near zero. The UPW system in a large fab is a chemical plant in its own right, occupying an entire floor of the building.

### Automated Material Handling

In a modern fab, wafers never travel through the cleanroom in human hands. An automated material handling system (AMHS) uses overhead hoist transport (OHT) vehicles -- robotic carriers that travel along ceiling-mounted rail networks -- to move FOUP cassettes of wafers between process tools. A large fab may have thousands of OHT vehicles managing the flow of tens of thousands of wafers simultaneously. The logistics software that orchestrates this movement is a sophisticated optimization system, routing wafers through the correct sequence of hundreds of tools while minimizing wait times and maximizing tool utilization.

### Gas Delivery and Chemical Systems

Semiconductor manufacturing uses dozens of specialty gases -- silane, ammonia, nitrogen trifluoride, tungsten hexafluoride, hydrogen, oxygen, argon, and many more -- each delivered to individual process tools through elaborate piping networks with automatic shutoff valves, flow controllers, and continuous purity monitoring. Many of these gases are toxic, corrosive, flammable, or pyrophoric (spontaneously igniting on contact with air), requiring extensive safety systems.

Liquid chemicals -- acids, solvents, photoresist, CMP slurries, developers -- are similarly distributed through dedicated piping systems, stored in temperature-controlled environments, and monitored for purity and concentration. The purity requirements for these chemicals mirror those for UPW: parts-per-billion contamination levels for metals, near-zero particle counts, tightly controlled concentrations.

### Environmental Control

Temperature and humidity in the cleanroom are maintained within narrow bands -- typically 21-23 degrees Celsius and 40-45% relative humidity -- because even small variations can affect resist coating thickness, etch rates, and other process parameters. Vibration isolation is critical: lithography tools are mounted on active vibration-damping platforms that compensate for seismic activity, traffic vibrations, and even the footsteps of workers in adjacent areas. Electromagnetic shielding protects sensitive electron-beam tools from stray fields.

## Chapter Roadmap: Where the Process Meets the Companies

The process flow described in this chapter is the skeleton on which the rest of this book is built. Each subsequent chapter focuses on one segment of this flow and the companies that dominate it.

In **Chapter 4**, we meet the companies that manufacture the silicon wafers -- the starting material for everything. **Chapter 5** examines the ultrapure water systems and specialty gases without which no fab can operate. **Chapters 6 through 8** explore the lithography ecosystem in depth: the exposure tools themselves (Chapter 6), the photomasks that carry the circuit patterns (Chapter 7), and the photoresist chemicals that make the patterns possible (Chapter 8).

**Chapters 9 through 11** cover the core material-processing steps: deposition (Chapter 9), etching and cleaning (Chapter 10), and CMP planarization (Chapter 11). **Chapter 12** looks at the fab infrastructure -- the robots, the material handling systems, the precision components, and the ceramic parts that keep the factory running.

The back-end story unfolds in **Chapters 13 through 15**: wafer testing and probing (Chapter 13), dicing and singulation (Chapter 14), and the rapidly evolving world of advanced packaging (Chapter 15).

Finally, **Chapter 16** introduces the demand side -- the foundries, memory makers, and AI chip designers whose capital spending decisions ripple backward through the entire supply chain -- and **Chapter 17** examines the geopolitical forces that are reshaping who can buy, sell, and build these technologies.

With the process vocabulary now in hand, we are ready to meet the companies. Let us begin where every chip begins: with the wafer.

---
*This chapter is a technical reference and does not draw on individual company data files.*
