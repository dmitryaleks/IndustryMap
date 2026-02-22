# Appendix E: Glossary of Semiconductor Terms

> Definitions for technical, business, and financial terms used throughout this book. Entries are arranged alphabetically. Chapter references indicate where the term is discussed in greatest detail.

---

## A

**Ablation dicing** — A laser dicing technique that uses a high-energy laser beam to vaporize material along the scribe line, physically removing silicon and dielectric layers to create a separation groove. Ablation dicing avoids mechanical blade stress but introduces a heat-affected zone and debris that must be managed. (Chapter 14)

**ALD (Atomic Layer Deposition)** — A thin-film deposition technique that builds up material one atomic layer at a time through sequential, self-limiting chemical reactions. Each ALD cycle deposits approximately 0.5 to 1.5 angstroms of film, providing unparalleled thickness control and conformality on complex three-dimensional structures. ALD is indispensable for high-k gate dielectrics and 3D NAND manufacturing. (Chapter 9)

**ALE (Atomic Layer Etching)** — The inverse of ALD: a process that removes material one atomic layer at a time through a two-step cycle of surface modification and selective removal. ALE enables sub-angstrom etch depth control at the most advanced nodes. (Chapter 10)

**AMHS (Automated Material Handling System)** — The automated transport network inside a semiconductor fab that moves wafer cassettes (FOUPs) between process tools. Modern AMHS installations use overhead hoist transport (OHT) vehicles traveling on ceiling-mounted rail networks. Daifuku is the dominant global supplier. (Chapter 12)

**Angstrom** — A unit of length equal to one ten-billionth of a meter (0.1 nanometers). Used in semiconductor manufacturing to express atomic-scale dimensions such as deposited film thickness or surface roughness. One angstrom is approximately the diameter of a hydrogen atom.

**Anisotropic etching** — An etching process that removes material preferentially in one direction (typically vertical), producing steep, nearly vertical sidewalls in the etched features. Anisotropic etching is essential for defining nanometer-scale circuit features and is the hallmark of dry/plasma etching techniques. Contrast with *isotropic etching*. (Chapter 10)

**APM (Ammonia-Peroxide Mixture)** — See *SC-1*.

**ArF (Argon Fluoride)** — An excimer laser light source producing deep ultraviolet light at 193 nanometers wavelength. ArF lithography, particularly when combined with immersion techniques, has been the workhorse of advanced semiconductor patterning from the 90-nanometer node through the 7-nanometer node. (Chapter 6)

**Aspect ratio** — The ratio of the depth (or height) of a feature to its width. High-aspect-ratio structures -- such as the deep trenches in 3D NAND flash memory, which can exceed 50:1 -- pose severe challenges for deposition, etching, and cleaning processes. (Chapters 9, 10)

**ATE (Automatic Test Equipment)** — Precision electronic systems that generate test signals, apply them to semiconductor devices under test, and analyze the resulting outputs to determine whether each device meets specifications. Advantest and Teradyne together control over 80% of the global ATE market. (Chapter 13)

## B

**Back-end processing** — The stages of semiconductor manufacturing that occur after front-end wafer fabrication is complete, including wafer test, dicing, packaging, and final test. Sometimes called BEOL in a broader sense, though BEOL more precisely refers to the interconnect layers formed during front-end processing. (Chapter 2)

**Batch processing** — A manufacturing approach in which multiple wafers (typically 100-200) are processed simultaneously in a single furnace or reactor. Batch processing is common for LPCVD, thermal oxidation, and diffusion steps. Kokusai Electric dominates batch ALD equipment. Contrast with *single-wafer processing*. (Chapter 9)

**BEOL (Back-End-of-Line)** — The portion of front-end wafer fabrication that creates the metal interconnect wiring layers connecting transistors to one another. BEOL processing involves repeated cycles of dielectric deposition, lithography, etching, metal deposition, and CMP. A leading-edge logic chip may have fifteen or more BEOL metal layers. (Chapter 11)

**BGA (Ball Grid Array)** — A type of IC package in which the external electrical connections are arranged as an array of solder balls on the underside of the package, rather than as leads on the periphery. See also *FC-BGA*. (Chapter 15)

**BHF (Buffered Hydrofluoric Acid)** — A mixture of hydrofluoric acid and ammonium fluoride used for controlled etching of silicon dioxide. The ammonium fluoride acts as a buffer that stabilizes the pH and etch rate, enabling more precise oxide removal than dilute HF alone. (Chapter 10)

**Blade dicing** — The dominant method of wafer singulation, using a thin diamond-impregnated spinning blade (typically 20-50 micrometers wide) to saw through the wafer along the streets between die. DISCO holds over 70% of the global blade dicing equipment market. (Chapter 14)

**Boule** — A cylindrical single-crystal ingot of silicon produced by the Czochralski process. A 300mm boule can be up to two meters long and weigh several hundred kilograms. Boules are sliced into individual wafers using diamond wire saws. Also called an "ingot." (Chapter 4)

**BTA (Benzotriazole)** — A corrosion inhibitor used in copper CMP slurries to protect recessed copper areas from chemical attack during polishing, preventing dishing and erosion defects. (Chapter 11)

**Burn-in** — A reliability screening process in which packaged ICs are operated at elevated temperature and voltage for an extended period to accelerate early-life failures (infant mortality) and weed out marginally defective parts before shipment. (Chapter 2)

## C

**CAR (Chemically Amplified Resist)** — A class of photoresist in which a photoacid generator (PAG) compound absorbs the exposure photon and catalytically amplifies the chemical change in the resist polymer, enabling the resist to function efficiently at DUV and EUV wavelengths. Developed for KrF lithography and used in all modern DUV and EUV resists. (Chapter 8)

**CD (Critical Dimension)** — The smallest feature size that can be reliably printed and transferred in a given lithography and etch process. CD is the primary metric of lithographic resolution and directly determines transistor density and chip performance. (Chapter 2)

**CD-SEM (Critical Dimension Scanning Electron Microscope)** — A specialized scanning electron microscope used to measure the width and shape of patterned features on a semiconductor wafer with sub-nanometer precision. (Chapter 2)

**Chiplet** — A small, modular semiconductor die designed to be combined with other chiplets in a single package. Chiplet architectures improve manufacturing yield (smaller dies have higher yield), enable mix-and-match process nodes, and allow reuse of proven designs across product lines. AMD pioneered commercial chiplet architectures with Zen 2. (Chapter 15)

**Chipping** — A dicing defect in which small fragments break away from the die edge due to mechanical stress during blade cutting. Front-side chipping is particularly dangerous as it can damage active circuit layers. (Chapter 14)

**CMP (Chemical Mechanical Planarization)** — A process that combines chemical dissolution and mechanical abrasion to planarize the wafer surface to angstrom-level flatness between process layers. A rotating wafer is pressed against a polishing pad while a chemically reactive slurry of abrasive nanoparticles is applied. CMP is performed after nearly every metal deposition step in modern chip fabrication. (Chapter 11)

**Coater/developer** — Track equipment that applies photoresist to the wafer surface (coating) before lithography exposure and removes the soluble portions of exposed resist (developing) after exposure. Tokyo Electron holds over 90% of the global coater/developer market. The coater/developer and lithography scanner typically operate as an integrated cluster. (Chapters 6, 9)

**Colloidal silica** — Nanometer-scale silicon dioxide particles suspended in liquid, used as the abrasive component in oxide and polysilicon CMP slurries. Fuso Chemical supplies approximately 90% of the colloidal silica used in semiconductor CMP. (Chapter 11)

**Conformality** — The ability of a deposition process to coat complex three-dimensional structures uniformly, including the sidewalls and bottoms of deep trenches and narrow features. ALD provides the highest conformality of any deposition technique. (Chapter 9)

**CoWoS (Chip-on-Wafer-on-Substrate)** — TSMC's 2.5D advanced packaging platform in which one or more logic dies and HBM memory stacks are placed side by side on a silicon interposer, which is then mounted on an FC-BGA substrate. CoWoS enables the ultra-high-bandwidth connections between GPU and memory that AI accelerators require. CoWoS capacity has been the single largest bottleneck in the global AI chip supply chain since 2023. (Chapter 15)

**CVD (Chemical Vapor Deposition)** — A deposition technique in which gaseous precursor chemicals react on the wafer surface to form a solid thin film. Major variants include LPCVD, PECVD, MOCVD, and HDP-CVD. CVD is the primary method for depositing silicon dioxide, silicon nitride, tungsten, and many other films in semiconductor manufacturing. (Chapter 9)

**CZ process** — See *Czochralski process*.

**Czochralski process** — The dominant technique for growing single-crystal silicon ingots. Polysilicon is melted in a quartz crucible at approximately 1,425 degrees Celsius, a seed crystal is dipped into the melt and slowly withdrawn while rotating, and the molten silicon solidifies onto the seed, extending the single-crystal structure. Named after the Polish chemist Jan Czochralski. (Chapter 4)

## D

**DAF (Die-Attach Film)** — A thin adhesive film used to bond a semiconductor die to its package substrate or lead frame. DAF must provide electrical conductivity (or insulation), thermal conductivity, and mechanical reliability. Resonac Holdings is a leading global supplier. (Chapter 15)

**DBG (Dicing Before Grinding)** — A process in which half-cuts or laser modifications are made into the wafer from the front side before the wafer is thinned by back-grinding. The thinning step completes the singulation, producing ultra-thin die without the mechanical stress of cutting through thin silicon. Essential for HBM and other stacked-die applications. (Chapter 14)

**Defocus** — A lithographic defect condition in which the projected image is out of focus, typically caused by excessive surface topography that exceeds the depth of focus of the lithography tool. Defocus produces blurred patterns that result in open or short circuits. (Chapter 11)

**Depth of focus (DOF)** — The range of vertical heights over which a lithography tool's projected image remains sharp enough to define circuit features. For EUV lithography, the DOF is approximately 45 nanometers; for ArF immersion, it ranges from 100 to 200 nanometers. CMP ensures the wafer surface stays within DOF. (Chapters 2, 11)

**Developer** — A chemical solution (typically tetramethylammonium hydroxide, or TMAH, for positive resists) used after lithographic exposure to dissolve away either the exposed or unexposed portions of the photoresist, revealing the intended circuit pattern. (Chapter 8)

**DHF (Dilute Hydrofluoric Acid)** — Hydrofluoric acid diluted to concentrations of 0.5 to 5 percent, used to remove silicon dioxide (native oxide and thermal oxide) from wafer surfaces during cleaning sequences. (Chapter 10)

**Die** — A single integrated circuit on a semiconductor wafer. A 300mm wafer may contain hundreds to thousands of individual die, depending on die size. Also called a "chip" informally. Plural: "die" or "dies."

**Die attach** — The process of bonding a semiconductor die to its package substrate or lead frame using an adhesive, solder, or film. See also *DAF*. (Chapter 15)

**DIO3 (Dissolved Ozone Water)** — Ultrapure water saturated with dissolved ozone, used as an environmentally friendly cleaning agent to remove organic contaminants from wafer surfaces. Increasingly used as a replacement for piranha solution in advanced fabs. (Chapter 10)

**Dishing** — A CMP defect in which the center of a wide metal feature is polished lower than its edges, creating a concave surface. Dishing increases metal line resistance and propagates topography to subsequent layers. (Chapter 11)

**Dividend yield** — A financial ratio calculated as a company's annual dividend per share divided by its stock price, expressed as a percentage. Used in this book to assess the income return component of semiconductor equity investments. (Chapter 18)

**Dopant** — An impurity atom intentionally introduced into the silicon crystal lattice to alter its electrical conductivity. Boron is the most common p-type dopant; phosphorus and arsenic are common n-type dopants. (Chapter 2)

**DRAM (Dynamic Random-Access Memory)** — The dominant type of volatile semiconductor memory, used as main memory in computers, servers, and mobile devices. DRAM cells must be periodically refreshed because they store data as charge on a capacitor. SK Hynix, Samsung, and Micron are the three major DRAM manufacturers. (Chapter 16)

**DUV (Deep Ultraviolet)** — A classification of lithography light sources operating at wavelengths of 248 nanometers (KrF) and 193 nanometers (ArF). DUV lithography, particularly ArF immersion, remains the workhorse technology for the majority of lithographic layers even at the most advanced nodes. Contrast with *EUV*. (Chapter 6)

## E

**Ebara** — See company profile in Chapter 11. Ebara Corporation manufactures CMP polishing systems used in semiconductor fabrication.

**EDI (Electrodeionization)** — A water purification technology that uses ion exchange resins and an applied electric field to remove dissolved ionic impurities. EDI is a key stage in semiconductor UPW production, replacing traditional chemical regeneration of ion exchange columns. (Chapter 5)

**Electrostatic chuck (ESC)** — A device that uses electrostatic force to hold a semiconductor wafer in place during processing steps such as plasma etching, deposition, or ion implantation. ESCs are typically made from advanced ceramics. NGK Insulators and Kyocera are leading suppliers. (Chapter 12)

**Encapsulation** — The process of covering a packaged semiconductor assembly with a protective epoxy molding compound to shield the die and interconnects from moisture, particles, and mechanical damage. The encapsulant must match the coefficient of thermal expansion of the die and substrate to prevent mechanical stress. (Chapter 15)

**Endpoint detection** — Techniques used during CMP and etching to determine precisely when to stop the process. Methods include optical interferometry, motor current monitoring, and eddy current sensing. Accurate endpoint detection prevents over-polishing or over-etching. (Chapters 10, 11)

**Epitaxy** — A deposition process that grows a crystalline film on a crystalline substrate such that the deposited film continues the crystal structure of the substrate. Silicon epitaxy and silicon-germanium (SiGe) epitaxy are used to engineer the channel regions of advanced transistors. (Chapter 9)

**Erosion** — A CMP defect in which the dielectric surface in areas of high metal pattern density is over-polished, creating systematic thickness differences between dense and isolated regions. (Chapter 11)

**EUV (Extreme Ultraviolet)** — Lithography technology using light at 13.5 nanometers wavelength. EUV requires reflective optics (since all materials absorb at this wavelength), vacuum environment, and tin-plasma light sources. ASML holds a 100% monopoly on EUV lithography systems. EUV is required for the most critical layers at nodes of 7 nanometers and below. (Chapter 6)

**Excimer laser** — A type of ultraviolet laser used as the light source in DUV lithography. KrF excimer lasers operate at 248 nm, ArF excimers at 193 nm. The term "excimer" derives from "excited dimer." (Chapter 6)

## F

**Fab (Fabrication facility)** — A semiconductor manufacturing facility, typically costing $15-25 billion to build and equip at the leading edge. A modern fab is an ISO Class 1 cleanroom housing hundreds of process tools connected by automated material handling systems. (Chapter 2)

**Fabless** — A business model in which a semiconductor company designs chips but does not own or operate its own fabrication facilities. Fabless companies contract with foundries (such as TSMC) for manufacturing. NVIDIA and AMD are prominent fabless companies. (Chapter 16)

**FC-BGA (Flip Chip Ball Grid Array)** — A high-performance IC package substrate technology in which the die is mounted face-down (flip chip) on a multi-layer organic substrate, with external connections provided by a ball grid array on the substrate's underside. FC-BGA substrates for AI processors can have 20 or more wiring layers. Ibiden commands over 50% of the AI server FC-BGA substrate market. (Chapter 15)

**FEOL (Front-End-of-Line)** — The portion of wafer fabrication that creates the transistors and other active devices on the silicon surface. FEOL processing includes oxidation, ion implantation, gate formation, and source/drain engineering. Contrast with *BEOL*. (Chapter 2)

**FinFET (Fin Field-Effect Transistor)** — A three-dimensional transistor architecture in which the channel region is shaped like a vertical fin protruding from the wafer surface, with the gate wrapping around three sides of the fin. FinFETs replaced planar transistors at the 22-nanometer node and dominated from the 14nm through 5nm generations. Succeeded by *GAA* at 3nm and below. (Chapter 2)

**Flip chip** — A packaging technique in which the die is mounted face-down on the substrate, with solder bumps on the die surface connecting directly to the substrate pads. Flip chip provides higher I/O density and shorter interconnect paths than wire bonding. (Chapter 15)

**Fluororesin** — A class of fluoropolymer materials (including PTFE and PFA) with exceptional chemical resistance, used to manufacture fittings, tubing, and valves for handling corrosive semiconductor chemicals such as hydrofluoric acid. PILLAR Corporation holds over 90% of the fluororesin fitting market for semiconductor applications. (Chapter 10)

**FOUP (Front Opening Unified Pod)** — A sealed container used to transport and store semiconductor wafers (typically 25 wafers per FOUP) within the cleanroom. FOUPs protect wafers from particle contamination during transport between process tools via the AMHS. (Chapter 12)

**Foundry** — A semiconductor manufacturing company that fabricates chips designed by other companies (fabless firms), rather than designing its own products. TSMC is the world's largest foundry, commanding over 60% of the global foundry market. (Chapter 16)

**Front-end processing** — The stages of semiconductor manufacturing that create transistors and interconnects on the wafer surface, including oxidation, lithography, etching, deposition, ion implantation, CMP, and cleaning. Front-end processing typically accounts for 60-70% of the total manufacturing cost. (Chapter 2)

## G

**GAA (Gate-All-Around)** — A transistor architecture in which the gate electrode completely surrounds the channel on all sides, providing superior electrostatic control compared to FinFET. GAA transistors (also called nanosheet transistors) are used at the 3-nanometer node and below by Samsung and TSMC (under the name GAAFET or nanosheet FET). (Chapter 2)

**Gate oxide** — A thin insulating layer (historically silicon dioxide, now typically a high-k dielectric such as hafnium oxide) formed between the gate electrode and the channel of a transistor. Gate oxide quality directly determines transistor performance and reliability. At advanced nodes, the gate oxide may be only a few atoms thick. (Chapter 2)

## H

**HAZ (Heat-Affected Zone)** — The region of material surrounding a laser cut or ablation that has been thermally altered. In laser dicing, the HAZ can cause damage to adjacent circuits and must be minimized. (Chapter 14)

**HBM (High Bandwidth Memory)** — A type of memory that stacks multiple DRAM dies vertically using through-silicon vias (TSVs) and micro-bumps. HBM provides memory bandwidth exceeding 1 TB/s per stack, making it essential for AI training and inference accelerators. Current-generation HBM3E stacks up to 12 DRAM layers. SK Hynix is the dominant HBM producer. (Chapter 15)

**HDP-CVD (High-Density Plasma CVD)** — A CVD variant that combines chemical vapor deposition with a high-density plasma source, enabling simultaneous deposition and sputtering. HDP-CVD provides excellent gap-fill capability for narrow trenches such as shallow trench isolation structures. (Chapter 9)

**HF (Hydrofluoric Acid)** — The most strategically important chemical in semiconductor manufacturing, used to etch silicon dioxide and clean wafer surfaces. At advanced nodes, HF must be purified to "twelve-nine" purity (99.9999999999%). The Stella Chemifa and Morita Chemical duopoly controls the global supply of ultra-high-purity HF. (Chapter 5)

**High-k dielectric** — An insulating material with a dielectric constant (k) significantly higher than silicon dioxide (k = 3.9). High-k materials such as hafnium oxide (HfO2, k approximately 25) replaced SiO2 as the gate dielectric from the 45nm node onward, enabling thinner equivalent oxide thickness without excessive leakage current. Deposited by ALD. (Chapter 9)

**High-NA EUV** — The next generation of EUV lithography with an increased numerical aperture of 0.55 (up from 0.33 in current EUV systems), enabling single-exposure resolution below 8 nanometers. ASML's first High-NA system (EXE:5000) shipped in 2024 at a price exceeding 350 million euros. (Chapter 6)

**HPM (Hydrochloric acid-Peroxide Mixture)** — See *SC-2*.

## I

**IC (Integrated Circuit)** — A semiconductor device containing multiple transistors, resistors, capacitors, and interconnects fabricated on a single piece of silicon. Modern ICs can contain tens of billions of transistors.

**ICP (Inductively Coupled Plasma)** — A plasma generation technique used in dry etching, where the plasma is created by an RF coil separate from the wafer electrode. ICP decouples plasma density from ion energy, enabling independent control of etch rate and directionality. ICP-RIE is the standard for leading-edge etch. (Chapter 10)

**IDM (Integrated Device Manufacturer)** — A semiconductor company that both designs and manufactures its own chips. Intel, Samsung, and SK Hynix are prominent IDMs. Contrast with *fabless* and *foundry* business models. (Chapter 16)

**i-line** — A lithography light source using the 436-nanometer emission line of a mercury arc lamp. i-line lithography resolves features down to approximately 350 nanometers and remains in active production for mature-node semiconductors including automotive, power management, and MEMS devices. Nikon and Canon are the primary i-line stepper suppliers. (Chapter 6)

**Immersion lithography** — An enhancement to ArF lithography that places a thin film of ultrapure water between the final lens element and the wafer surface, increasing the effective numerical aperture from approximately 0.93 to 1.35 and enabling resolution below 40 nanometers. The immersion transition was the decisive competitive event that established ASML's dominance over Nikon. (Chapter 6)

**Ingot** — See *boule*.

**Interposer** — A thin silicon or organic substrate placed between chiplets and the package substrate in 2.5D packaging. The interposer contains fine-pitch wiring and TSVs that provide high-bandwidth connections between adjacent dies. TSMC's CoWoS platform uses a silicon interposer. (Chapter 15)

**Ion implantation** — The process of introducing dopant atoms into the silicon lattice by ionizing them and accelerating them at high energy into the wafer surface. Ion implantation provides precise control of dose (atoms per square centimeter) and depth. The crystal damage caused by implantation is repaired by subsequent thermal annealing. (Chapter 2)

**ISO Class 1** — The highest cleanroom classification under ISO 14644-1, specifying fewer than 10 particles larger than 0.1 micrometers per cubic meter of air. The most critical areas of a modern semiconductor fab operate at ISO Class 1 or better. (Chapter 2)

**Isotropic etching** — An etching process that removes material equally in all directions, including laterally beneath the mask. Isotropic etching is characteristic of wet chemical etching and limits its use to features larger than approximately one micrometer. Contrast with *anisotropic etching*. (Chapter 10)

## J

**JEDEC** — A global standards organization (Joint Electron Device Engineering Council) that develops open standards for the microelectronics industry, including the HBM memory specification. (Chapter 15)

**JOINT2** — A collaborative consortium of twelve Japanese semiconductor materials companies developing next-generation materials. An example of Japan's distinctive model of pre-competitive cooperation between industry rivals. (Chapter 15)

## K

**Kerf** — The width of material removed during a dicing cut. Kerf represents lost silicon that cannot become functioning die. Minimizing kerf width (e.g., through stealth dicing, which has effectively zero kerf) allows more die per wafer or narrower streets between die. (Chapter 14)

**KGD (Known-Good Die)** — A die that has been electrically tested and confirmed to meet specifications before being used in a multi-die package. KGD testing is essential for advanced packaging (especially HBM stacking and chiplet assembly) because a single bad die in a stack or package can render the entire assembly worthless. (Chapter 13)

**KrF (Krypton Fluoride)** — An excimer laser light source producing deep ultraviolet light at 248 nanometers wavelength. KrF lithography resolves features down to approximately 130 nanometers and was the industry standard for the 250nm through 130nm technology nodes. (Chapter 6)

## L

**Lead frame** — A thin metal frame (typically copper alloy) that provides the external electrical connections and structural support for a semiconductor package. Lead frames are used in traditional wire-bonded packages. (Chapter 2)

**Lithography** — The process of transferring a circuit pattern from a photomask onto a photoresist-coated wafer using projected light. Lithography is the defining process step in semiconductor manufacturing, determining the minimum feature size and thereby the transistor density, performance, and power efficiency of the finished chip. (Chapter 6)

**Low-k dielectric** — An insulating material with a dielectric constant lower than that of silicon dioxide (k = 3.9), used between copper interconnect lines in BEOL processing to reduce capacitive coupling and signal delay. Advanced low-k materials can have dielectric constants below 2.5. (Chapter 9)

**LPCVD (Low-Pressure Chemical Vapor Deposition)** — A CVD variant operating at reduced pressures (0.1-10 Torr) and temperatures of 400-900 degrees Celsius. LPCVD produces highly uniform, conformal films and is commonly performed in batch furnaces. The standard method for depositing silicon nitride, polysilicon, and certain oxide films. (Chapter 9)

## M

**Market capitalization (Market cap)** — The total market value of a company's outstanding shares, calculated as share price multiplied by the number of shares. All market capitalization figures in this book are expressed in Japanese yen unless otherwise noted. (Chapter 18)

**Mass flow controller (MFC)** — A device that precisely measures and controls the flow rate of gases into semiconductor process chambers. Horiba holds over 30% of the global MFC market. Accurate gas flow control is essential for achieving the correct etch selectivity, deposition rate, and film composition. (Chapter 10)

**Megasonic cleaning** — A wafer cleaning technique that uses high-frequency sound waves (approximately 800 kHz to 1 MHz) to dislodge particles from the wafer surface without the cavitation damage caused by lower-frequency ultrasonic cleaning. (Chapter 10)

**MEMS (Micro-Electro-Mechanical Systems)** — Miniaturized mechanical and electro-mechanical devices fabricated using semiconductor manufacturing techniques. In the context of this book, MEMS probe cards use lithographically fabricated contact structures for wafer testing. (Chapter 13)

**Metallurgical-grade silicon** — Silicon refined to approximately 98-99% purity by reducing quartz in an electric arc furnace. This is the starting material for further purification to semiconductor grade but is orders of magnitude too impure for chip fabrication. (Chapter 4)

**Metrology** — The science of measurement as applied to semiconductor manufacturing. Metrology tools measure critical dimensions, overlay accuracy, film thickness, defect counts, and electrical properties between process steps. Metrology data feeds back into process controllers for real-time adjustment. (Chapter 2)

**Micro-bump** — A miniature solder connection (typically 20-40 micrometers in diameter) used to bond stacked dies in 3D packaging, particularly in HBM memory stacks. Micro-bumps connect the TSVs between adjacent die layers. (Chapter 15)

**MOCVD (Metal-Organic Chemical Vapor Deposition)** — A CVD variant using metal-organic precursors, primarily employed for depositing compound semiconductor films such as gallium nitride. Important for LED and power semiconductor manufacturing. (Chapter 9)

**Moore's Law** — The observation, first articulated by Intel co-founder Gordon Moore in 1965, that the number of transistors on an integrated circuit doubles approximately every two years. Moore's Law has guided the semiconductor industry's roadmap for over five decades, though the cadence of scaling has slowed at the most advanced nodes. (Chapter 1)

**Multi-patterning** — A set of lithographic techniques that achieve feature sizes smaller than the resolution limit of a single exposure by exposing the same wafer layer multiple times with different mask patterns. Techniques include SADP (self-aligned double patterning) and SAQP (self-aligned quadruple patterning). Multi-patterning multiplies process cost and complexity, which is the economic driver for EUV adoption. (Chapter 6)

## N

**NAND flash** — A type of non-volatile semiconductor memory used for solid-state storage. Modern 3D NAND stacks over 200 layers vertically, requiring extensive ALD and etch capabilities. Kioxia (formerly Toshiba Memory) is a major NAND manufacturer. (Chapter 16)

**Nanoimprint lithography (NIL)** — A patterning technique that physically presses a template into liquid resist on the wafer to transfer the circuit pattern, bypassing optical projection entirely. Canon's FPA-1200NZ2C system is the leading commercial NIL tool. NIL consumes approximately one-tenth the power of an EUV system but faces challenges in throughput and defectivity. (Chapter 6)

**Nanometer (nm)** — One billionth of a meter. The standard unit for expressing semiconductor feature sizes. As of 2025-2026, leading-edge logic chips are manufactured at the 3nm node, with 2nm in development.

**Numerical aperture (NA)** — A measure of the light-gathering ability of a lithography tool's lens system. Higher NA enables finer resolution. Current EUV systems have NA = 0.33; High-NA EUV increases this to 0.55. For ArF immersion, the maximum NA is approximately 1.35. (Chapter 6)

## O

**OCD (Optical Critical Dimension)** — A metrology technique that uses optical scatterometry to measure the dimensions and shape of patterned features on a wafer. OCD provides non-destructive, high-throughput CD measurement as a complement to CD-SEM. (Chapter 2)

**OHT (Overhead Hoist Transport)** — Robotic carrier vehicles that travel along ceiling-mounted rail networks inside a semiconductor cleanroom, transporting FOUP cassettes between process tools. OHT is the primary transport mechanism within an AMHS. Daifuku is the dominant OHT supplier. (Chapter 12)

**Operating margin** — A financial metric calculated as operating income divided by revenue, expressed as a percentage. Operating margin measures a company's profitability from its core business operations before interest and taxes. Peer group medians range from 14.9% (G1 equipment) to 28.0% (G4 other). (Chapter 18)

**OSAT (Outsourced Semiconductor Assembly and Test)** — A company that provides semiconductor packaging and testing services on a contract basis. Major OSATs include ASE Technology, Amkor, and JCET. OSATs handle packaging for fabless chip designers that do not own back-end facilities. (Chapter 16)

**Overlay accuracy** — The precision with which one lithography layer is aligned to the previous layers on the wafer. At the 3nm node, overlay must be controlled to within approximately 1.5 nanometers. Overlay error causes layer-to-layer misalignment, producing non-functional transistors or interconnects. (Chapter 6)

**Oxidation (Thermal)** — The process of growing a thin layer of silicon dioxide on the wafer surface by exposing silicon to oxygen or steam at high temperatures (800-1,200 degrees Celsius). Thermal oxidation is used to create gate oxides, isolation layers, and passivation films. (Chapter 2)

## P

**PAG (Photoacid Generator)** — A chemical compound in chemically amplified photoresists that absorbs exposure light (DUV or EUV photons) and generates a strong acid that catalytically alters the surrounding resist polymer. Toyo Gosei is a specialist in PAG compounds for EUV resist. (Chapter 8)

**Passivation** — A protective insulating layer (typically silicon nitride or silicon oxynitride) deposited over the completed circuit to protect it from moisture, contamination, and mechanical damage. (Chapter 2)

**PBR (Price-to-Book Ratio)** — A financial valuation metric calculated as a company's market capitalization divided by its book value (total assets minus total liabilities). A PBR below 1.0 means the company trades below the accounting value of its net assets. (Chapter 18)

**PECVD (Plasma-Enhanced Chemical Vapor Deposition)** — A CVD variant that uses a plasma to lower the reaction temperature to 200-400 degrees Celsius, making it compatible with temperature-sensitive structures such as metal interconnect layers. PECVD is widely used for interlayer dielectrics and passivation films. (Chapter 9)

**PER (Price-to-Earnings Ratio)** — A financial valuation metric calculated as a company's stock price divided by its earnings per share. PER indicates how many years of current earnings the market is willing to pay for. Peer group medians in this book range from 17.0x (G2 materials) to 31.59x (G1 equipment). (Chapter 18)

**PFA (Perfluoroalkoxy)** — A fluoropolymer material with exceptional chemical resistance, used for ultra-high-purity piping, fittings, and valves in semiconductor chemical delivery systems. PFA does not leach impurities into corrosive chemicals. (Chapter 5)

**Photomask** — A glass plate (typically fused silica for DUV, or a multilayer Mo/Si reflector for EUV) carrying the circuit pattern for one layer of a chip. The mask pattern is projected through the lithography tool's optical system onto the wafer. Also called a "reticle." A single mask defect can be replicated onto millions of chips. (Chapter 7)

**Photoresist** — A light-sensitive polymer coated onto the wafer surface before lithography exposure. Exposure to light changes the resist's chemical solubility, enabling selective removal (development) to create a stencil pattern for subsequent etching or deposition. Major resist types include novolac/DNQ (i-line), CAR (KrF/ArF), and metal-oxide EUV resists. (Chapter 8)

**Piranha solution** — A mixture of sulfuric acid and hydrogen peroxide (typically 3:1 to 7:1) heated to 120-180 degrees Celsius, used to strip organic residues and photoresist from wafer surfaces. One of the most aggressive cleaning chemistries in semiconductor manufacturing. Also called SPM (Sulfuric acid-Peroxide Mixture). (Chapter 10)

**Planarization** — See *CMP*.

**Polysilicon** — Ultra-high-purity polycrystalline silicon, the feedstock for single-crystal ingot growth via the Czochralski process. Also, deposited polysilicon thin films are used as gate electrodes and structural elements in semiconductor devices. (Chapter 4)

**Probe card** — An array of microscopic contact tips mounted on a printed circuit board, used to make simultaneous electrical contact with the bond pads on one or more die during wafer test. Major architectures include cantilever, vertical, and MEMS probe cards. (Chapter 13)

**Prober** — See *wafer prober*.

**PVD (Physical Vapor Deposition)** — A deposition technique, most commonly sputtering, in which atoms are physically ejected from a solid target by plasma bombardment and deposited onto the wafer. PVD is the primary method for depositing metal films (aluminum, titanium, tantalum, copper seed layers). (Chapter 9)

**PVDF (Polyvinylidene Fluoride)** — A fluoropolymer used for valves, piping, and components in semiconductor UPW and chemical distribution systems due to its chemical resistance and low extractable contamination. (Chapter 5)

## R

**Rapidus** — A Japanese national champion foundry project aimed at establishing leading-edge (2nm) semiconductor manufacturing capability in Hokkaido, Japan. Rapidus has partnerships with IBM for process technology and with Toppan for photomask production. (Chapter 15)

**Rayleigh criterion** — The fundamental equation governing lithographic resolution: Resolution = k1 x (wavelength / numerical aperture). The Rayleigh criterion defines the minimum resolvable feature size as a function of light wavelength, lens NA, and the process factor k1. (Chapter 6)

**RCA clean** — A two-step wafer cleaning sequence developed in 1965 by Werner Kern at RCA Laboratories, consisting of SC-1 (organic and particle removal) and SC-2 (metallic contamination removal). The RCA clean remains the foundation of modern semiconductor cleaning protocols. (Chapter 10)

**RDL (Redistribution Layer)** — A layer of fine-pitch wiring deposited on a die or wafer surface that reroutes the I/O connections from their original locations to a new pattern suitable for packaging. RDL is a key technology in fan-out wafer-level packaging and advanced interposer fabrication. (Chapter 15)

**Resistivity (UPW)** — A measure of water purity, expressed in megaohm-centimeters. Semiconductor-grade UPW targets the theoretical maximum resistivity of 18.2 megaohm-centimeters at 25 degrees Celsius, indicating the near-complete absence of dissolved ions. (Chapter 5)

**Reticle** — See *photomask*.

**RIE (Reactive Ion Etching)** — The most common form of dry etching, in which the wafer sits on an RF-powered electrode that accelerates plasma ions perpendicularly toward the surface, producing anisotropic etch profiles with vertical sidewalls and minimal lateral undercutting. (Chapter 10)

**RLS trade-off** — The three-way trade-off in photoresist performance between Resolution (how small a feature can be printed), Line-edge roughness (how smooth the feature edges are), and Sensitivity (how little light is needed for exposure). Improving one parameter typically degrades one or both of the others. (Chapter 8)

**ROE (Return on Equity)** — A financial metric calculated as net income divided by shareholders' equity, expressed as a percentage. ROE measures how effectively a company generates profits from its equity capital. Peer group medians range from 9.38% (G2 materials) to 38.8% (G4 other). (Chapter 18)

**RO (Reverse Osmosis)** — A water purification technology in which water is forced through semi-permeable membranes at high pressure, rejecting 99.5% or more of dissolved salts, organics, and particles. RO is a foundational stage in semiconductor UPW production. (Chapter 5)

## S

**SADP (Self-Aligned Double Patterning)** — A multi-patterning technique that uses a single lithography exposure followed by deposition and etching steps to effectively double the pattern density. SADP enables features smaller than the single-exposure resolution limit. (Chapter 6)

**SAQP (Self-Aligned Quadruple Patterning)** — An extension of SADP that achieves four times the pattern density of a single exposure, at the cost of greatly increased process complexity (twelve to fifteen steps where a single EUV exposure would suffice). SAQP was used for critical layers at 7nm DUV nodes. (Chapter 6)

**SC-1 (Standard Clean 1)** — A cleaning solution of ammonium hydroxide, hydrogen peroxide, and deionized water (typically 1:1:5 to 1:2:7), heated to 65-80 degrees Celsius. SC-1 removes organic contaminants and particles from the wafer surface through oxidation and chemical undercutting. Also called APM. (Chapter 10)

**SC-2 (Standard Clean 2)** — A cleaning solution of hydrochloric acid, hydrogen peroxide, and deionized water (typically 1:1:6 to 1:2:8), heated to 65-80 degrees Celsius. SC-2 removes metallic contaminants by forming soluble chloride complexes. Also called HPM. (Chapter 10)

**Scanner** — A lithography exposure tool that scans the mask and wafer simultaneously during exposure, allowing a small slit of light to sweep across the full field. Scanners replaced steppers for advanced lithography because scanning enables a larger exposure field and tighter overlay control. ASML's TWINSCAN is the dominant scanner platform. Contrast with *stepper*. (Chapter 6)

**Scribe lane** — See *street*.

**Selectivity (etch)** — The ratio of the etch rate of the target material to the etch rate of the surrounding material that must be preserved. A selectivity of 100:1 means the etchant removes the target material one hundred times faster than the adjacent material. High selectivity is essential for preserving thin films during pattern transfer. (Chapter 10)

**Siemens process** — The dominant industrial process for purifying silicon to semiconductor grade. Metallurgical-grade silicon is converted to trichlorosilane gas, purified by fractional distillation, and decomposed by CVD onto heated silicon rods to produce ultra-high-purity polysilicon. (Chapter 4)

**Silicon interposer** — See *interposer*.

**Single-crystal silicon** — Silicon in which the atoms are arranged in a continuous, unbroken crystal lattice across the entire wafer. Single-crystal structure is required for semiconductor device fabrication and is achieved through the Czochralski process. Contrast with *polysilicon*. (Chapter 4)

**Single-wafer processing** — A manufacturing approach in which wafers are processed one at a time, allowing individual recipe tuning for each wafer. Single-wafer processing is standard for lithography, CMP, plasma etch, and PECVD. Contrast with *batch processing*. (Chapter 9)

**SiGe (Silicon-Germanium)** — A semiconductor alloy of silicon and germanium used in epitaxial channel layers to engineer carrier mobility in advanced transistors. SiGe epitaxy is deposited by CVD or MBE. (Chapter 9)

**Slurry** — A suspension of abrasive nanoparticles in a chemically reactive liquid, used in CMP to simultaneously dissolve and mechanically remove material from the wafer surface. Different slurry formulations are required for different materials (oxide, copper, tungsten, polysilicon). (Chapter 11)

**SoC (System-on-Chip)** — An integrated circuit that combines multiple functional blocks -- processor cores, memory, I/O controllers, and other components -- on a single die. SoC ATE testing is one of Advantest's primary markets. (Chapter 13)

**SPM (Sulfuric acid-Peroxide Mixture)** — See *piranha solution*.

**Sputtering** — See *PVD*.

**Stealth dicing** — A laser dicing technique that focuses a laser inside the silicon wafer to create internal damage lines without affecting the surface. The wafer is then expanded on tape and separates cleanly along the damaged planes. Stealth dicing produces zero kerf, no chipping, and strong die edges. Pioneered by Hamamatsu Photonics and commercialized by DISCO. (Chapter 14)

**Step coverage** — The ratio of the film thickness on the sidewall or bottom of a feature to the film thickness on a flat surface, expressed as a percentage. Good step coverage (approaching 100%) means the film coats vertical surfaces as well as horizontal ones. ALD provides the best step coverage. (Chapter 9)

**Stepper** — A lithography exposure tool that exposes one die (or a small group of die) at a time, then "steps" to the next position on the wafer and repeats the exposure. Steppers were the standard lithography platform before scanners superseded them for advanced nodes. i-line steppers remain in production for mature-node manufacturing. (Chapter 6)

**STI (Shallow Trench Isolation)** — A technique for electrically isolating adjacent transistors on a chip by etching shallow trenches into the silicon and filling them with silicon dioxide. CMP is used to planarize the filled trenches flush with the surrounding silicon surface. (Chapter 11)

**Street** — The narrow lane of empty space between adjacent die on a semiconductor wafer, along which the wafer is diced. Streets are typically 50-80 micrometers wide. Also called a "scribe lane." (Chapter 14)

**Substrate** — In packaging, the multi-layer circuit board onto which semiconductor die are mounted. Substrates route electrical signals from the die to the package's external connections. See *FC-BGA*, *ceramic package substrate*. (Chapter 15)

## T

**TC bonder (Thermocompression bonder)** — Equipment that bonds semiconductor dies together under controlled temperature and pressure, used primarily for stacking DRAM dies in HBM production. Hanmi Semiconductor holds 71.2% of the global TC bonder market for HBM. (Chapter 15)

**Thermal oxidation** — See *oxidation*.

**Throughput** — The number of wafers a process tool can process per unit time, typically expressed as wafers per hour (WPH). Throughput is a primary determinant of cost per wafer layer and therefore of the economics of each process step. (Chapter 6)

**TOC (Total Organic Carbon)** — A measure of organic contamination in ultrapure water, expressed in parts per billion (ppb). Semiconductor-grade UPW requires TOC below 1 ppb. Organic contaminants can form residues on wafer surfaces that interfere with subsequent processing. (Chapter 5)

**Track** — See *coater/developer*.

**Trichlorosilane** — A chemical compound (SiHCl3) used as an intermediate in the Siemens process for purifying silicon. Metallurgical-grade silicon is converted to trichlorosilane, which is purified by fractional distillation and then decomposed to yield semiconductor-grade polysilicon. (Chapter 4)

**TSV (Through-Silicon Via)** — A vertical electrical connection that passes completely through a silicon die or interposer, enabling 3D stacking of dies. TSVs are the enabling technology for HBM memory stacks and 2.5D interposers. TSV fabrication requires etching deep, narrow holes through silicon and filling them with copper. (Chapter 15)

**TTV (Total Thickness Variation)** — A wafer quality specification measuring the maximum variation in wafer thickness across the entire 300mm diameter. Advanced wafers require TTV of less than 1 micrometer. (Chapter 4)

**TWINSCAN** — ASML's lithography scanner platform, used for both DUV and EUV systems. The TWINSCAN architecture uses two wafer stages -- one being aligned while the other is being exposed -- to maximize throughput. (Chapter 6)

## U

**UCIe (Universal Chiplet Interconnect Express)** — An open industry standard, published in 2022, that defines the physical and logical interface for chiplet-to-chiplet connections within a package. UCIe is backed by Intel, AMD, Arm, TSMC, Samsung, and others and aims to enable interoperable chiplet ecosystems. (Chapter 15)

**ULPA (Ultra-Low Penetration Air) filter** — High-efficiency air filters used in cleanroom air handling systems to remove particles larger than 0.12 micrometers with 99.9995% efficiency. ULPA filters maintain the ISO Class 1 cleanroom conditions required for semiconductor manufacturing. (Chapter 2)

**Underfill** — An epoxy adhesive injected between a flip-chip die and its substrate to redistribute mechanical stress from the solder bumps and protect the interconnections from thermal cycling damage. (Chapter 15)

**UPW (Ultrapure Water)** — Water purified to semiconductor grade, with resistivity of 18.2 megaohm-centimeters, TOC below 1 ppb, dissolved metals below 1 part per trillion, and near-zero particle counts. A modern 300mm fab consumes 30,000-50,000 cubic meters of UPW per day. Organo, Kurita, and Nomura Micro Science dominate the UPW system market. (Chapter 5)

## V

**VLSI (Very Large Scale Integration)** — An integrated circuit containing 100,000 to one million transistors. In this book, VLSI primarily refers to Japan's VLSI Research Project (1976-1980), a government-funded collaborative effort among Japanese companies that established Japan's semiconductor equipment industry and created the foundation for the supply chain dominance described throughout this book. (Chapter 1)

## W

**Wafer** — A thin, circular disc of single-crystal silicon on which semiconductor devices are fabricated. The current standard diameter is 300 millimeters (approximately 12 inches), with a thickness of approximately 775 micrometers. A single 300mm wafer may contain hundreds to thousands of individual die. (Chapter 4)

**Wafer prober** — A machine that positions a semiconductor wafer with sub-micron accuracy beneath a probe card and brings the probe card contacts into contact with the die pads, enabling electrical testing of every die while still on the wafer. Tokyo Seimitsu holds 46% of the global wafer prober market. (Chapter 13)

**Wafer sort** — See *wafer test*.

**Wafer test** — The process of electrically testing every die on a completed wafer before dicing, identifying good and defective die. Also called wafer sort or wafer probe. Wafer test prevents the waste of expensive packaging materials on defective die. (Chapter 13)

**Wire bonding** — A packaging technique that uses thin gold or copper wires (18-25 micrometers in diameter) to connect bond pads on the die to leads on the package. Wire bonding is the oldest and still the most widely used packaging interconnect by unit volume, though it is limited in I/O density and electrical performance. (Chapter 15)

## Y

**Yield** — The percentage of die on a wafer that function correctly after fabrication. Yield is the central economic variable in semiconductor manufacturing: a one-percentage-point yield improvement on a leading-edge wafer can translate to tens of millions of dollars per year in additional revenue. Cumulative yield is the product of yields at every individual process step, which is why even 99.99% per-step yield can produce significant losses over 1,000+ steps. (Chapter 2)

## Numerical

**2.5D integration** — An advanced packaging architecture in which multiple dies are placed side by side on a silicon interposer, connected through fine-pitch wiring and TSVs. The interposer provides high-bandwidth die-to-die communication that is impossible through organic substrates alone. TSMC's CoWoS is the most commercially significant 2.5D platform. (Chapter 15)

**3D integration** — An advanced packaging architecture in which dies are stacked directly on top of one another and connected vertically through TSVs. HBM memory is the most commercially important application of 3D integration. (Chapter 15)

**3D NAND** — A type of NAND flash memory in which memory cells are stacked vertically in over 200 layers, dramatically increasing storage density per unit area. 3D NAND fabrication requires extensive ALD and high-aspect-ratio etching. (Chapter 9)

**300mm (12-inch)** — The current standard wafer diameter for leading-edge semiconductor manufacturing. The transition from 200mm (8-inch) to 300mm wafers increased the usable wafer area by 2.25 times, significantly reducing cost per die. (Chapter 4)

---

*This glossary covers the principal technical, business, and financial terms used in Chapters 1 through 18 and Appendices A through D. For company-specific details, consult Appendix A (Japanese companies) and Appendix B (global ecosystem companies).*
