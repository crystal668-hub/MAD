---
source: Cabanillas-Esparza 等 - 2025 - Boosting Dual Hydrogen Electrocatalysis with PtNiMo Catalysts Tuning the NiMo Ratio and Minimizin.pdf
tool: marker
duration: 11.519s
generated: 2026-01-10T05:37:47.530882Z
---

*Article*

# **Boosting Dual Hydrogen Electrocatalysis with Pt/NiMo Catalysts: Tuning the Ni/Mo Ratio and Minimizing Pt Usage**

**Luis Fernando Cabanillas-Esparza <sup>1</sup> , Edgar Alonso Reynoso-Soto <sup>1</sup> [,](https://orcid.org/0000-0001-7676-411X) Balter Trujillo-Navarrete <sup>1</sup> [,](https://orcid.org/0000-0002-0196-1001) Brenda Alcántar-Vázquez [2](https://orcid.org/0000-0002-7462-249X) , Carolina Silva-Carrillo [3](https://orcid.org/0000-0002-1390-5429) and Rosa María Félix-Navarro 1,[\\*](https://orcid.org/0000-0003-3178-1164)**

- <sup>1</sup> Tecnológico Nacional de México, Instituto Tecnológico de Tijuana, Centro de Graduados e Investigación en Química, Blvd. Alberto Limón Padilla S/N, Mesa de Otay, Tijuana 22000, BC, Mexico; d25210005@tectijuana.edu.mx (L.F.C.-E.); edgar.reynoso@tectijuana.edu.mx (E.A.R.-S.); balter.trujillo@tectijuana.edu.mx (B.T.-N.)
- <sup>2</sup> Universidad Nacional Autónoma de México, Instituto de Ingeniería, Avenida Universidad 3000, Coyoacán, Ciudad de Mexico 04510, Mexico; balcantarv@iingen.unam.mx
- <sup>3</sup> Universidad Autónoma de Baja California, Facultad de Ciencias Químicas e Ingeniería, Calzada Universidad 14418, Parque Internacional Industrial Tijuana, Tijuana 22424, BC, Mexico; carolina.silva.carrillo@uabc.edu.mx
- **\*** Correspondence: rmfelix@tectijuana.mx; Tel.: +52-6646234043

#### **Abstract**

The development of efficient platinum group metal-free (PGM-free) catalysts for the hydrogen evolution reaction (HER) and the hydrogen oxidation reaction (HOR) is essential for advancing hydrogen-based energy technologies. In this study, NixMo100−<sup>x</sup> composites supported on Carbon Ketjenblack EC-300J (CK) were synthesized via thermal reduction under a controlled Ar/H<sup>2</sup> (95:5) atmosphere to investigate the effect of the Ni/Mo molar ratio on electrocatalytic performance. Structural and morphological analyses by XRD and TEM confirmed the formation of the NiMo alloys and carbide phases with controlled particle size distributions (~18 nm), while BET measurements revealed specific surface areas up to 124.69 m<sup>2</sup> g −1 for the Pt-loaded samples. Notably, the 3% Pt/Ni90Mo10-CK catalyst exhibited outstanding bifunctional activity in a half-cell configuration, achieving an overpotential of 65.2 mV and a Tafel slope of 41.6 mV dec−<sup>1</sup> for the HER, and a Tafel slope of 32.9 mV dec−<sup>1</sup> with an exchange current density of 1.03 mA cm−<sup>2</sup> for the HOR. These results demonstrate that compositional tuning and minimal Pt incorporation synergistically enhance the catalytic efficiency, providing a promising platform for next-generation

**Keywords:** hydrogen; electrocatalyst; water electrolysis; hydrogen evolution reaction;

# hydrogen electrocatalysts.

hydrogen oxidation reaction; NiMo; PtNiMo

# **1. Introduction**

Addressing climate change and environmental sustainability while meeting growing energy demands is one of the greatest challenges of our time. In this context, hydrogen (H2) has emerged as a promising clean energy carrier due to its high combustion enthalpy (287 kJ mol−<sup>1</sup> ) and its only byproduct being water [\[1,](#page-16-0)[2\]](#page-16-1). However, most of the global H<sup>2</sup> production still relies on fossil fuels through steam reforming, a process that emits significant amounts of CO<sup>2</sup> and contributes to global warming [\[3\]](#page-16-2).

Among the various green production routes, alkaline water electrolysis stands out as a sustainable technology for generating high-purity hydrogen through the hydrogen

Academic Editor: Yan Xie

Received: 30 May 2025 Revised: 23 June 2025 Accepted: 25 June 2025 Published: 28 June 2025

**Citation:** Cabanillas-Esparza, L.F.; Reynoso-Soto, E.A.; Trujillo-Navarrete, B.; Alcántar-Vázquez, B.; Silva-Carrillo, C.; Félix-Navarro, R.M. Boosting Dual Hydrogen Electrocatalysis with Pt/NiMo Catalysts: Tuning the Ni/Mo Ratio and Minimizing Pt Usage. *Catalysts* **2025**, *15*, 633. [https://doi.org/](https://doi.org/10.3390/catal15070633) [10.3390/catal15070633](https://doi.org/10.3390/catal15070633)

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(https://creativecommons.org/](https://creativecommons.org/licenses/by/4.0/) [licenses/by/4.0/\)](https://creativecommons.org/licenses/by/4.0/).

*Catalysts* **2025**, *15*, 633 2 of 20

evolution reaction (HER). Noble metal-based electrocatalysts, especially platinum, exhibit outstanding HER performance [\[4,](#page-16-3)[5\]](#page-16-4). Nevertheless, their high cost and scarcity hinder largescale application, prompting significant interest in developing platinum group metal-free (PGM-free) alternatives. These include electrocatalysts based on non-precious transition metals (Ni, Fe, Co, Mo, Cu) [\[6–](#page-16-5)[10\]](#page-16-6), transition metal chalcogenides [\[11\]](#page-16-7), alloys [\[12](#page-16-8)[–15\]](#page-16-9), and carbides [\[16–](#page-17-0)[18\]](#page-17-1).

The hydrogen evolution reaction (HER) in an alkaline medium can follow two pathways presented in the Volmer–Heyrovsky mechanism and the Volmer–Tafel mechanism. Equations (1)–(3) reveal each step of the reaction.

Volmer step: 
$$H_2O + M + e^- \rightarrow MH_{ads} + OH^-$$
 (1)

Heyrovsky step: 
$$H_2O + MH_{ads} + e^- \rightarrow H_2 + M + OH^-$$
 (2)

Tafel step: 
$$MH_{ads} + MH_{ads} \rightarrow H_2 + 2M$$
 (3)

Here, M represents the catalytic surface and MHads denotes the adsorbed hydrogen. The rate-limiting step in the alkaline HER is typically the Volmer step, which involves water dissociation. This requirement for an extra cleavage step slows the overall reaction kinetics compared to acidic media, where proton availability is higher [\[19](#page-17-2)[–21\]](#page-17-3). In this context, optimizing catalyst composition and surface chemistry becomes crucial for improving alkaline HER performance.

Nickel and its alloys are widely studied due to their low cost, good electrical conductivity, and corrosion resistance in alkaline environments. However, pure Ni suffers from poor HER kinetics due to sluggish OH<sup>−</sup> desorption and the formation of inactive Ni hydride species [\[22,](#page-17-4)[23\]](#page-17-5). Ni-based alloys, particularly with molybdenum (Mo), offer improved performance by tuning the electronic structure and optimizing hydrogen adsorption energy [\[24](#page-17-6)[,25\]](#page-17-7). NiMo alloys have thus emerged as promising candidates for the alkaline HER and even for the hydrogen oxidation reaction (HOR). These materials can be synthesized by various methods, including impregnation [\[26](#page-17-8)[,27\]](#page-17-9), microwave-assisted techniques [\[28,](#page-17-10)[29\]](#page-17-11), electrodeposition [\[30](#page-17-12)[,31\]](#page-17-13), and hydrothermal synthesis [\[32](#page-17-14)[,33\]](#page-17-15).

Several studies have highlighted the electrocatalytic potential of NiMo-based materials. For instance, V.K. Singh et al. demonstrated that MoS2/MoNi4/MoO<sup>2</sup> nanorods with a 4:1 Ni/Mo ratio achieved an overpotential of 155.6 mV and a Tafel slope of 67.0 mV dec−<sup>1</sup> in the HER [\[6\]](#page-16-5), attributing improved performance to the synergy between heteroatoms and surface reactivity. Zhiying Xu et al. developed a Co(OH)2/α-NiMoO<sup>4</sup> nanowire/nanoflower heterostructure that reached an overpotential of 183.01 mV due to its high surface area and enhanced active site exposure [\[34\]](#page-17-16). Another study on sputter-deposited NiMo thin films showed that a 65:35 Ni/Mo ratio yielded a surface-rich Ni(OH)<sup>2</sup> layer responsible for a HER overpotential of 198.0 mV and a Tafel slope of 167.0 mV dec−<sup>1</sup> at 10 mA cm−<sup>2</sup> [\[35\]](#page-17-17).

To further enhance the performance of NiMo systems, researchers have explored incorporating small amounts of Pt. Pt-Ni bimetallic catalysts have shown excellent HER and HOR activity. Zipeng Zhao et al. reported that PtNi-O/C achieved an overpotential of 39.8 mV and a mass activity of 7.23 mA µg <sup>−</sup><sup>1</sup> Pt, nearly eight times higher than commercial Pt/C [\[36\]](#page-17-18). Hengquan Chen et al. demonstrated that ordered and disordered PtNi phases on carbon supports both exhibited outstanding HER activity with disordered D-PtNi/C, showing an overpotential of 39.7 mV [\[37\]](#page-17-19). Yukuai He et al. synthesized a trimetallic PtNiMo/C catalysts with one-step annealing, achieving a remarkably low overpotential of 39.0 mV, outperforming Pt/C, PtNi/C, and PtMo/C [\[38\]](#page-18-0). These findings emphasize the importance of tuning both composition and structure at the nanoscale.

In this work, we systematically investigate the effect of the Ni/Mo molar ratio on the electrocatalytic performance of NixMo100−<sup>x</sup> composites supported on Carbon Ketjenblack *Catalysts* **2025**, *15*, 633 3 of 20

EC-300J (CK), and evaluate the contribution of low Pt loadings (1, 3, and 5 wt%) in the Ni90Mo10-CK systems. The materials were synthesized via a simple thermal reduction process and tested for their HER and HOR performance. Notably, the 3% Pt/Ni90Mo10-CK catalyst exhibited excellent activity in half-cell measurements, with an overpotential of 65.2 mV and a Tafel slope of 41.6 mV dec−<sup>1</sup> for the HER, and a Tafel slope of 32.9 mV dec−<sup>1</sup> and an exchange current density of 1.03 mA cm−<sup>2</sup> for the HOR. These results demonstrate that minimal Pt incorporation combined with optimized NiMo composition can deliver a bifunctional performance that competes with commercial 20% Pt/C, contributing to the development of efficient and cost-effective hydrogen energy systems.

# **2. Results and Discussion**

Table [1](#page-2-0) summarizes all the catalysts investigated in this work synthesized by the steps shown in Schemes [1](#page-13-0) and [2,](#page-13-1) which were subjected to electrochemical measurements (β-NiOOH quantification, CO stripping, chronopotentiometry, HER and HOR) and physicochemical characterizations (XRD, TEM, XPS, and BET surface area analysis).

| Notation    | Composition         | Notation          | Composition                    |
|-------------|---------------------|-------------------|--------------------------------|
| Mo-CK       | Mo on CK            | 1% Pt-CK          | 1 wt% Pt on CK                 |
| Ni-CK       | Ni on CK            | 3% Pt-CK          | 3 wt% Pt on CK                 |
| Ni10Mo90-CK | Ni/Mo = 10:90 on CK | 5% Pt-CK          | 5 wt% Pt on CK                 |
| Ni30Mo70-CK | Ni/Mo = 30:70 on CK | 1% Pt/Ni90Mo10-CK | 1 wt% Pt on Ni90Mo10-CK        |
| Ni50Mo50-CK | Ni/Mo = 50:50 on CK | 3% Pt/Ni90Mo10-CK | 3 wt% Pt on Ni90Mo10-CK        |
| Ni70Mo30-CK | Ni/Mo = 70:30 on CK | 5% Pt/Ni90Mo10-CK | 5 wt% Pt on Ni90Mo10-CK        |
| Ni80Mo20-CK | Ni/Mo = 80:20 on CK | 20% Pt-C          | commercial 20 wt% Pt on carbon |
| Ni85Mo15-CK | Ni/Mo = 85:15 on CK |                   |                                |
| Ni90Mo10-CK | Ni/Mo = 90:10 on CK |                   |                                |
| Ni95Mo5-CK  | Ni/Mo = 95:5 on CK  |                   |                                |

<span id="page-2-0"></span>**Table 1.** Description and notation of electrocatalysts used in this study.

# *2.1. Electrochemical Characterization of the Materials*

#### 2.1.1. Electrochemical Active Surface Area (ECSA) Determination of Ni by β-NiOOH Method

Cyclic voltammetry was carried out to estimate the electrochemical active surface area (ECSA) of the Ni-CK and NixMo100−x-CK materials. This test allows for quantifying the active sites and the exposed Ni, employing the β-NiOOH method [\[39\]](#page-18-1). The ECSANi was calculated using Equation (4):

$$ECSA_{Ni} = \frac{Q_{\beta.NiOOH}}{0.42 \text{ mC cm}^{-2} L_{Ni}}$$
 (4)

where Qβ-NiOOH indicates the area under the curve of the β-NiOOH reduction peak, 0.42 mC cm−<sup>2</sup> denotes the specific charge density of Ni and LNi, the nickel mass loading. Figure [1](#page-3-0) shows the voltammograms of the oxidation reaction of β-Ni(OH)<sup>2</sup> + OH−→ β-NiOOH + e<sup>−</sup> + H2O and the reduction reaction of β-NiOOH + e<sup>−</sup> + H2O → β-Ni(OH)<sup>2</sup> + OH−, this last reaction shows the reduction peak (Qβ-NiOOH) between 0.9 and 1.3 V vs. RHE that will provide the charge to calculate the ECSANi for each material.

The material with the largest ECSANi was not the one with the highest nickel loading (Ni-CK), as can be observed in Table [2.](#page-3-1) In the case of the bimetallic materials, the presence of molybdenum favors the exposure of Ni on the surface materials (NixMo100−x-CK); therefore, compared to the monometallic Ni material, the ECSANi of the bimetallic materials is higher per unit mass. Figure S1a in the Supporting Materials (SMs) shows the β-NiOOH test for

*Catalysts* **2025**, *15*, 633 4 of 20

the Mo-CK to rule out Mo signal interferences with the cathodic peaks of the NixMo100−x-CK materials. The absence of an Mo peak in that working window during this test rules out any influence on the cathodic peak of the materials with high Mo loading and low Ni content. The bimetallic materials show a displacement of the reduction peak (Figure [1\)](#page-3-0) towards lower potentials, where molybdenum, being present, favors the exposure of Ni and, at the same time, slightly shifts the signal. Therefore, it can be said that, as the amount of Mo decreases and the amount of Ni increases, it is evident that this displacement is decreasing in the direction of lower potentials.

<span id="page-3-0"></span>**Figure 1.** Cyclic voltammetry by the β-NiOOH method of Ni-CK and NixMo100−x-C electrocatalysts.

<span id="page-3-1"></span>

| Table 2. Summary of ECSA results of Ni-CK and NixMo100−x-CK electrocatalysts by the β-NiOOH |
|---------------------------------------------------------------------------------------------|
| method.                                                                                     |

| Material    | Qβ-NiOOH<br>(mC) | LNi<br>(mg) | ECSANi<br>(cm2<br>) | ECSANi<br>(cm2 g−1) |
|-------------|------------------|-------------|---------------------|---------------------|
| Ni10Mo90-CK | 0.33             | 0.02        | 0.80                | 3.73                |
| Ni30Mo70-CK | 1.31             | 0.06        | 3.13                | 4.84                |
| Ni50Mo50-CK | 1.92             | 0.10        | 4.58                | 4.25                |
| Ni70Mo30-CK | 3.36             | 0.15        | 8.00                | 5.30                |
| Ni80Mo20-CK | 3.42             | 0.17        | 8.16                | 4.73                |
| Ni85Mo15-CK | 3.56             | 0.18        | 8.47                | 4.62                |
| Ni90Mo10-CK | 4.40             | 0.19        | 10.47               | 5.39                |
| Ni95Mo5-CK  | 4.76             | 0.20        | 11.33               | 5.53                |
| Ni-CK       | 1.48             | 0.21        | 3.54                | 1.64                |

Figure S1b and Table S1 in the Supplementary Materials show the results obtained for the Pt/Ni90Mo10-CK materials by the Ni β-NiOOH method, it can be identified that there are losses of the exposed Ni content due to the incorporation of the Pt. Additionally the 20% Pt-C catalyst was tested in the β-NiOOH test, this catalyst did not show a reduction peak under this potential window, as shown in Figure S2 in the Supplementary Materials.

# 2.1.2. Active Surface Area of the Pt-CK and Pt/Ni90Mo10-CK Materials

Figure [2a](#page-4-0)–f presents the CO stripping analysis to determine the exposed Pt surface area (ECSAPt) in the Pt-CK and the Pt/Ni90Mo10-CK materials with different Pt metallic loads. In all cases, the first sweep of the voltammograms is attributed to the oxidation of CO in the material (the area of the gold-marked zone), and the second sweep denotes when there is no presence of CO, because all the CO was desorbed in the first sweep. The CO *Catalysts* **2025**, *15*, 633 5 of 20

<span id="page-4-0"></span>oxidation peak is observed at around 0.7 V, where the subsequent reaction occurs COad + OHad + OH<sup>−</sup> → CO<sup>2</sup> + e<sup>−</sup> + H2O (in an alkaline medium) [\[40\]](#page-18-2).

**Figure 2.** Cyclic voltammetry by CO stripping: (**a**) 1% Pt-CK, (**b**) 3% Pt-CK, (**c**) 5% Pt-CK, (**d**) 1% Pt/Ni90Mo10-CK, (**e**) 3% Pt/Ni90Mo10-CK, and (**f**) 5% Pt/Ni90Mo10-CK.

Equation (5) was used to determine the ECSAPt, where QCO represents the area under the curve of the CO oxidation peak, the specific charge density value is 0.42 mC cm−<sup>2</sup> and LPt signifies the mass of Pt.

$$ECSA_{Pt} = \frac{Q_{CO}}{0.42 \text{ mC cm}^{-2} L_{Pt}}$$
 (5)

Table [3](#page-5-0) displays the ECSAPt values of the Pt-CK and Pt/Ni90Mo10-CK with different Pt percentages. The ECSAPt of the Pt-CK materials exhibits fewer Pt active sites than the Pt/Ni90Mo10-CK. The oxophilic properties of the NiMo base-metal favor more Pt active spots on the surface of the Pt/Ni90Mo10-CK. Trimetallic materials perform 3.9 to 7.6 times better in the ECSAPt than the Pt-CK materials. Also, the Pt/Ni90Mo10-CK materials exhibited a competitive ECSAPt per unit of mass compared to 20% Pt-C in the CO stripping analysis (Figure S3 in the Supplementary Materials) which confirms that NiMo favors Pt to have a large exposure of active sites despite having low Pt loadings. The broadening of peaks observed in Figure [2d](#page-4-0)–f is absent in the CO oxidation signals of Figure [2a](#page-4-0)–c, since between 0.45 and 0.50 V vs. RHE, it is attributed to CO adsorbed on Pt via the oxygenated surface species arising from NiO<sup>x</sup> [\[40\]](#page-18-2). The largest peak, associated with CO adsorption on the Pt (100) facets, is seen at around 0.72 V vs. RHE, and overlaps with CO adsorption of Pt on the PtMo around 0.8 V vs. RHE [\[41](#page-18-3)[,42\]](#page-18-4). This explains the substantial rise in the adsorbed CO on the Pt/Ni90Mo10-CK materials and, consequently, the higher quantity of Pt active sites.

#### 2.1.3. Electrocatalytic Activity for the Hydrogen Evolution Reaction (HER)

The carbonaceous support (CK) has its own electrocatalytic activity but demands a high overpotential (661.8 mV) at 10 mA cm−<sup>2</sup> . When Mo and Ni were incorporated into the CK, the overpotential drops to 604.8 and 382.2 mV, respectively, indicating a significant improvement, as shown in Figure [3a](#page-5-1). In the HER, the bimetallic materials improved the results obtained by the monometallic materials as a function of the Ni/Mo molar ratio, increasing with the amount of Ni and decreasing with the amount of Mo. All materials from the Ni70Mo30-CK to the Ni95Mo5-CK (Figure S4 in the Supplementary Materials) *Catalysts* **2025**, *15*, 633 6 of 20

exhibit a catalytic performance higher than Ni-CK, where the Ni90Mo10-CK material stands out, obtaining an overpotential of 203.16 mV and a Tafel slope of 161.9 mV dec−<sup>1</sup> .

<span id="page-5-0"></span>

| Table 3. Summary of the ECSA results of the Pt-CK and Pt/Ni90Mo10-CK electrocatalyst by CO |  |
|--------------------------------------------------------------------------------------------|--|
| stripping.                                                                                 |  |

| Material          | QCO<br>(mC) | LPt<br>(mg) | (cm2<br>ECSAPt<br>) | ECSAPt<br>(cm2 g−1) |
|-------------------|-------------|-------------|---------------------|---------------------|
| 1% Pt-CK          | 0.180       | 0.002       | 0.428               | 19.877              |
| 3% Pt-CK          | 0.200       | 0.006       | 0.476               | 7.362               |
| 5% Pt-CK          | 0.234       | 0.010       | 0.557               | 5.174               |
| 1% Pt/Ni90Mo10-CK | 0.700       | 0.002       | 1.670               | 77.470              |
| 3% Pt/Ni90Mo10-CK | 1.010       | 0.006       | 2.420               | 37.480              |
| 5% Pt/Ni90Mo10-CK | 1.770       | 0.010       | 4.230               | 39.290              |
| 20% Pt/C          | 11.400      | 0.041       | 27.142              | 66.202              |

<span id="page-5-1"></span>**Figure 3.** HER polarization curves of different electrocatalysts recorded in 1.0 M KOH at room temperature, using a scan rate of 5 mV s−<sup>1</sup> , and without iR compensation: (**a**) CK, Mo-CK, Ni-CK, and Ni90Mo10-CK; (**b**) Pt-modified CK-based materials; (**c**) 3% Pt/Ni90Mo10-CK; (**d**) corresponding Tafel plots derived from the polarization curves.

The optimum molar ratio between Ni and Mo (90:10) was kept constant to test the additional materials. The parameters, such as carbon support (Vulcan Carbon, CNT, and graphene), temperature, and NiMo metal loading on the carbon support, were varied (Figure S5a–c in the Supplementary Materials), but the performance of the Ni90Mo10-CK could not be exceeded due to the large surface area and conductivity provided by the Carbon Ketjenblack EC-300 (CK).

As shown in Figure [3b](#page-5-1), the evaluation of the HER performance of the 1% Pt-CK, the 3% Pt-CK, and the 5% Pt-CK catalysts exhibits overpotentials of 173.8, 129.5, and 118.6 mV vs. the RHE, respectively, to reach the current density of 10 mA cm−<sup>2</sup> . These catalytic activity

*Catalysts* **2025**, *15*, 633 7 of 20

values were comparable to that of the commercial 20% Pt/C (109.1 mV vs. RHE). But, as shown in Figure [3c](#page-5-1), once Pt was deposited onto the Ni90Mo10-CK base, the overpotentials of the 1% Pt/Ni90Mo10-CK (77.4 mV vs. RHE), the 3% Pt/Ni90Mo10-CK (65.2 mV vs. RHE), and the 5% Pt/Ni90Mo10-CK (54.9 mV vs. RHE) decreased dramatically, replacing 20% Pt-C as the best catalyst in the current study. Moreover, trimetallic compounds have an improved Tafel slope (Figure [3d](#page-5-1)), where the 3% Pt/Ni90Mo10-CK can be highlighted due to its low overpotential (65.2 mV) and low Tafel slope (41.6 mV dec−<sup>1</sup> ) which could follow a Tafel–Volmer mechanism kinetics.

The bar diagram in Figure [4](#page-6-0) shows a summary of the catalytic performance of the evaluated materials in the HER at −10 mA cm−<sup>2</sup> in which the impact of the Pt/NiMo-CK system is more appreciable.

<span id="page-6-0"></span>**Figure 4.** Overpotentials at −10 mA cm−<sup>2</sup> of the materials tested in the HER.

To conclude the HER tests, the 3% Pt/Mo-CK and the 3% Pt/Ni-CK were evaluated, and the results showed that Ni and Mo separately do not produce the same effect in the presence of Pt (Figure S5d in the Supplementary Materials). While the 3% Pt/Ni-CK needed 123.05 mV, the 3% Pt/Mo-CK material showed an overpotential of 122.32 mV, which reflects higher overpotentials than the one exhibited by the 3% Pt/Ni90Mo10-CK (65.2 mV). Furthermore, the results of some of the electrocatalysts reported in the literature were compared with the performance of the electrocatalysts prepared in this work (Ni90Mo10-CK and Pt/Ni90Mo10-CK), and it should be noted that significant results were obtained in this investigation with the low loading of Pt (Table S2 in the Supplementary Materials).

The potential-time curve was recorded at 10 mA cm−<sup>2</sup> by chronopotentiometry to determine the HER stability of the 3% Pt/Ni90Mo10-CK. According to Figure [5a](#page-7-0), after a constant current test of 24-h, the overpotential of the 3% Pt/Ni90Mo10-CK increased, displaying a decline in stability. However, after the 24-h stability test, the HER polarization curve of the 3% Pt/Ni90Mo10-CK shows no great potential decay (Figure [5b](#page-7-0)), which indicates a competitive yield from the electrocatalyst at low and high current densities.

# 2.1.4. Electrocatalytic Activity for the Hydrogen Oxidation Reaction (HOR)

Polarization curves for the hydrogen oxidation reaction (HOR) on the studied catalysts (Pt/Ni90Mo10-CK) were performed using a rotating disk electrode (RDE) in an H2-saturated 0.1 M KOH solution at a scan rate of 1.0 mV s−<sup>1</sup> and a constant rotation rate of 1600 rpm. Commercial 20% Pt-C was used as a guide for the HOR measurements. The Ni90Mo10-CK did not show catalytic activity in the HOR studies because it did not present an anodic

*Catalysts* **2025**, *15*, 633 8 of 20

<span id="page-7-0"></span>current, as illustrated in Figure [6.](#page-7-1) However, high currents were obtained once 1, 3, and 5% Pt was deposited on the NiMo-base materials; the 1% Pt/Ni90Mo10-CK material was able to overcome the current of all the materials, including the commercial material. Furthermore, it can be observed that the onset potential of the Pt/Ni90Mo10-CK materials had a lower potential, which also favors the HOR catalytic performance.

**Figure 5.** (**a**) Chronopotentiometric stability test of the 3% Pt/Ni90Mo10-CK at −10 mA cm−<sup>2</sup> for 24 h in 1.0 M KOH; (**b**) HER polarization curves before and after stability testing, showing minimal performance loss.

<span id="page-7-1"></span>**Figure 6.** Polarization curves for the HOR of the Ni90Mo10-CK, 1% Pt/Ni90Mo10-CK, 3% Pt/Ni90Mo10- CK, 5% Pt/Ni90Mo10-CK, and commercial 20% Pt-C.

The exchange current densities (Jo) and Tafel slopes of the catalysts measured in the HOR are displayed in Table [4.](#page-8-0) The 3% Pt/Ni90Mo10-CK material is found to have the optimal kinetic parameters in comparison to the commercial 20% Pt-C because it has a lower Tafel slope (32.9 mV dec−<sup>1</sup> ) and a comparable Jo. The low value of the Tafel slope could be associated with the Volmer–Tafel reaction mechanism, which is the ideal pathway for the dissociative hydrogen adsorption (Equation (8)) [\[43\]](#page-18-5). However, the electron charge transfer is associated with the Tafel slope value of the Volmer step (Equation (6)) or Heyrovsky step (Equation (7)) [\[43\]](#page-18-5).

Volmer step: 
$$M - H_{ads} + OH^{-} \rightarrow M + H_{2}O + e^{-}$$
 (6)

Heyrovsky step: 
$$H_2 + OH^- + M \rightarrow M - H_{ads} + H_2O + e^-$$
 (7)

*Catalysts* **2025**, *15*, 633 9 of 20

| + 2M → 2M − Hads<br>Tafel step: H2 | (8) |
|------------------------------------|-----|
|------------------------------------|-----|

<span id="page-8-0"></span>

| Table 4. Electrochemical parameters of catalyst studied in the HOR. |  |  |
|---------------------------------------------------------------------|--|--|
|---------------------------------------------------------------------|--|--|

| Material          | Tafel Slope<br>(mV dec−1) | Jo<br>(mA cm−2) |
|-------------------|---------------------------|-----------------|
| Ni90Mo10-CK       | -                         | -               |
| 1% Pt/Ni90Mo10-CK | 40.00                     | 0.92            |
| 3% Pt/Ni90Mo10-CK | 32.90                     | 1.03            |
| 5% Pt/Ni90Mo10-CK | 38.84                     | 1.04            |
| 20% Pt-C          | 34.80                     | 1.04            |

In this particular case, the trimetallic system (Pt/Ni90Mo10-CK) requires low amounts of Pt to be a competitive catalyst in the HOR, as examined in these studies.

#### *2.2. Physicochemical Characterization of Catalysts*

The size and distribution of the NiMo metal deposited onto the Carbon Ketjenblack EC-300J were examined by TEM microscopy (Figure [7a](#page-8-1)). According to the histogram shown in Figure [7b](#page-8-1), the average size of the Ni90Mo10-CK nanoparticles was 18.09 ± 5.72 nm. Once Pt was incorporated into the Ni90Mo10-CK base (Figure [8a](#page-9-0)), the particle size decreased after the thermal reduction, obtaining an average particle size of 1.95 nm ± 0.32 nm for the 3% Pt/Ni90Mo10-CK catalyst (Figure [8b](#page-9-0)). TEM images of the Ni-CK, the Mo-CK, and the different magnification of the Ni90Mo10-CK and the 3% Pt/Ni90Mo10-CK are illustrated in Figure S6a, Figure S7a, and Figure S8a–f, respectively, in the Supplementary Materials.

<span id="page-8-1"></span>**Figure 7.** (**a**) TEM micrograph of the Ni90Mo10-CK catalyst, (**b**) the Ni90Mo10-CK particle size distribution, and (**c**) XRD pattern of the NixMo100−x-CK materials.

*Catalysts* **2025**, *15*, 633 10 of 20

<span id="page-9-0"></span>**Figure 8.** (**a**) TEM micrograph of the 3% Pt/Ni90Mo10-CK catalyst, (**b**) the 3% Pt/Ni90Mo10-CK particle size distribution, and (**c**) XRD pattern of the Pt/Ni90Mo10-CK materials.

A powder X-ray diffraction (XRD) analysis was utilized to determine the crystalline phase composition of the Mo-CK, Ni-CK, Ni90Mo10-CK, and Pt/Ni90Mo10-CK materials. In the case of the Mo-CK (Figure S6b in the Supplementary Materials), the characteristic peaks observed at 26.2◦ , 32.0◦ , 36.95◦ , 37.3◦ , 37.6◦ , 41.6◦ , 42.1◦ , 49.6◦ , 53.3◦ , 53.7◦ , and 54.2◦ correspond to the (−111), (−201), (200), (111), (−202), (−112), (120), (012), (−221), (220), (022), and (003) planes of the MoO<sup>2</sup> (PDF#00-005-0452). The Ni-CK pattern (Figure S7b in the Supplementary Materials) displays peaks at 44.6◦ and 51.9◦ attributing to the (111) and (200) planes of the metallic Ni (PDF#01-070-0989), respectively. It can be seen that the XRD pattern of the Ni90Mo10-CK (Figure [7c](#page-8-1)) exhibited various peaks, where a pair of intense peaks at 44.04◦ and 51.35◦ correspond to the (111) and (200) planes of the NiMo alloy (PDF# 04-027-3193); carbide species were identified on the Ni90Mo10-CK at 34.6◦ , 38.0◦ , 39.5◦ , 52.3◦ , and 58.5◦ matching to (100), (002), (011), (012), and (003) on the crystalline planes of the Mo2C (PDF# 04-019-0642), and the Ni3Mo3-C card (PDF# 01-089-4883) indexed for the obtained peaks at 22.6◦ , 26.6◦ , 32.6◦ , 35.7◦ , 39.9◦ , 42.8◦ , 46.8◦ , 48.9◦ , 49.8◦ , 54.4◦ , 55.4◦ , and 59.7◦ for the crystallographic facets of (220), (311), (400), (331), (422), (511), (440), (531), (442), (533), (622), and (551), respectively. A signal of the Ni3Mo3-C overlaps with the main peak of Mo (PDF# 04-004-8878) at 40.3◦ , corresponding to the plane (110). The remaining weak signals are attributed to MoO<sup>2</sup> (PDF#00-005-0452) and hydrated MoO<sup>3</sup> (PDF#00-048-0399). The XRD study of all the NixMo100−x-CK molar ratios is shown in Figure S9 in the Supplementary Materials.

On the other hand, different proportions of Pt deposited on the Pt/Ni90Mo10-CK were examined by XRD to define the main peak of the metallic Pt and to determine the effect of metal loading. It can be observed that the main peak of Pt becomes more intense as a higher load of this metal is incorporated, as shown in Figure [8c](#page-9-0). The pattern exhibits peaks at 40.4◦ and 46.8◦ that correspond to the (111) and (200) planes of Pt (PDF#04-016-3818), and simultaneously Pt forms alloys through interactions with Ni and Mo to obtain PtNi (PDF# 04-016-5005) and PtMo (PDF# 01-074-5984). As is evident, the metallic Ni (PDF#01-070- 0989) signals remain, while the Ni(OH)<sup>2</sup> (PDF#01-073-6992) and MoO<sup>2</sup> (PDF#00-005-0452) display low-intensity peaks.

*Catalysts* **2025**, *15*, 633 11 of 20

Although high-resolution TEM analysis was not initially conducted, the morphological features observed by TEM are in agreement with the crystalline phases identified by XRD. The Ni90Mo10-CK catalyst exhibited metallic particles with average diameters around 18 nm, which is consistent with the formation of the NiMo alloy and the Mo-based carbide phases previously identified by XRD. The incorporation of Pt into the Ni90Mo10-CK structure resulted in significantly smaller nanoparticles (~2 nm), which correlates with the appearance of characteristic Pt diffraction peaks and an increased surface area later confirmed by BET analysis. The observed decrease in particle size also supports the formation of Pt-containing alloy phases, such as PtNi and PtMo, as indicated by the slight broadening and shifting of peaks in the XRD patterns. Additionally, the high-resolution TEM image presented in Figure S10 in the Supplementary Materials reveals interplanar distances of 0.22 nm and 0.208 nm, which correspond to the (111) plane of Pt and to Mo incorporation within the Ni lattice along the same (111) plane, respectively. This structural evidence further supports the presence of intimately mixed Pt-Ni-Mo domains, and agrees with previous reports of Mo incorporation modifying the Ni lattice structure and electronic environment [\[44\]](#page-18-6). Overall, these combined results suggest a coherent structural evolution toward more finely dispersed and catalytically active nanodomains upon Pt deposition.

Table S3 in the Supplementary Materials summarizes the structural parameters derived from X-ray diffraction (XRD) patterns for various Mo, Ni, NiMo, and Pt–NiMo-based electrocatalysts supported on CK. The analysis includes crystallite size (determined by both the Scherrer and Williamson–Hall methods), microstructural strain, dislocation density, and degree of crystallinity. The incorporation of Mo into the Ni lattice leads to a systematic reduction in crystallite size and a concurrent increase in both strain and dislocation density. These structural distortions are favorable for enhancing HER activity, as they are typically associated with a higher density of active sites. For most samples, the crystallite sizes obtained from Scherrer and Williamson–Hall methods are comparable, indicating that the peak broadening in the diffraction patterns arises primarily from reduced coherent domain size rather than from significant lattice strain.

In the materials containing Pt, particularly the 3% Pt/Ni90Mo10-CK, a pronounced decrease in both crystallite size (<2 nm) and crystallinity is observed, suggesting the formation of highly defective nanodomains. This structural evolution correlates with enhanced HER performance, attributed to a synergistic effect between the metallic Pt and the defective NiMo surface.

A direct comparison between structural parameters and electrochemical performance further supports this correlation. For instance, the Ni90Mo10-CK exhibits a moderate crystallite size (~19 nm), intermediate strain (~0.0063), and a crystallinity of 65.0%. This balance between order and defect density provides both grain boundary and partially ordered active sites, which contribute to a relatively low overpotential (η10~203.0 mV) and a moderate Tafel slope (~161.0 mV dec−<sup>1</sup> ). By contrast, the 3% Pt/Ni90Mo10-CK presents the smallest crystallite size (~1.5 nm), the lowest strain (~0.0010), and a low crystallinity (~41%), indicating effective Pt dispersion and a high density of surface-active sites. Despite its low crystallinity, this material exhibits the best HER performance (η10~65.0 mV, Tafel~41.0 mV dec−<sup>1</sup> ), emphasizing the dominant role of the Pt–NiMo interfacial synergy in promoting catalytic activity.

X-ray photoelectron spectroscopy (XPS) was employed to obtain insights into the surface chemistry and oxidation states of the 3% Pt/Ni90Mo10-CK catalyst. The survey spectrum indicates the presence of C, O, Mo, Ni, and Pt elements (Figure [9a](#page-11-0)). The C 1s spectrum shown in Figure [9b](#page-11-0) exhibits four peaks corresponding to 283.45, 284.8, 285.9, and 286.75 eV attributed to M-C (M=Ni, Mo, NiMo), C-C/C=C, C-O, and O-C=O [\[45,](#page-18-7)[46\]](#page-18-8). Moreover, the O 1s spectra (Figure [9c](#page-11-0)) illustrated three peaks at 529.31, 531.37, and 533.23 eV,

*Catalysts* **2025**, *15*, 633 12 of 20

which correspond to the M-O (M=Ni, Mo), oxygen vacancies, and hydroxyl species adsorbed on the catalyst surface [\[44](#page-18-6)[,47\]](#page-18-9), respectively. The Mo 3d XPS spectrum of the 3% Pt/Ni90Mo10-CK shows a pair of weak peaks identified at binding energies of 228.98 and 232.11 eV, corresponding to the Moδ<sup>+</sup> species (0 < δ < 4) (Figure [9d](#page-11-0)), which are attributed to Mo2C and MoP (due to the Mo precursor used in the synthesis) [\[48](#page-18-10)[,49\]](#page-18-11). The other doublets at 230.85/233.98 (Mo4+) and 232.74/235.87 (Mo6+) are ascribed to MoO<sup>2</sup> and MoO<sup>3</sup> [\[50](#page-18-12)[,51\]](#page-18-13). The Ni 2P deconvolution (Figure [9e](#page-11-0)) exhibit three peaks at 854.2, 855.3, and 857.1 eV, corresponding to NiO, Ni(OH)2, and NiOOH [\[52](#page-18-14)[–54\]](#page-18-15), information that matches with the obtained data on the O 1s spectrum. Finally, Figure [9f](#page-11-0) displayed two sets of Pt stages, where the first set, at 72.05/75.35, correspond to Pt0+ and the second set, at 73.44/76.74 eV, relates to Pt2+ [\[38,](#page-18-0)[55\]](#page-18-16). The XPS of the Mo-CK, Ni-CK, and Ni90Mo10-CK are illustrated in Figure S11, Figure S12, and Figure S13, respectively, in the Supplementary Materials.

<span id="page-11-0"></span>**Figure 9.** XPS spectra of the 3% Pt/Ni90Mo10-CK: (**a**) survey; (**b**) C 1s; (**c**) O 1s; (**d**) Mo 3d; (**e**) Ni 2p; and (**f**) Pt 4f.

It is extremely important to mention that the XRD patterns and oxidation states determined by XPS of the Ni90Mo10-CK and the 3% Pt/Ni90Mo10-CK are related to the EDS spectrum (Figure S14a,b), which confirm the presence of nickel, molybdenum, carbon, oxygen, and platinum (in the case of the 3% Pt/Ni90Mo10-CK).

Figure [10a](#page-12-0),c shows the N<sup>2</sup> adsorption–desorption isotherms of the Ni90Mo10-CK and the 3% Pt/Ni90Mo10-CK. Both samples exhibit Type II isotherms with H3-type hysteresis loops, according to the IUPAC classification [\[56\]](#page-18-17). Type II isotherms are typically associated with non-microporous solids in which multilayer adsorption occurs on surfaces of unrestricted accessibility, suggesting that the materials possess a considerable external or macroporous surface area. The presence of H3 hysteresis loops, characterized by their non-closure at high relative pressures, is indicative of meso- or macropores of slit-like geometry, generally arising from the interparticle spacing of aggregates composed of platelike domains. This combination of features reflects a porous architecture dominated by mesoporous interstices and disordered agglomerates, which may enhance molecular diffu*Catalysts* **2025**, *15*, 633 13 of 20

sion and accessibility within the catalyst structure. The BET-specific surface areas of the Ni90Mo10-CK and the 3% Pt/Ni90Mo10-CK were calculated to be 51.99 and 124.69 m<sup>2</sup> g −1 , respectively. Additionally, the pore size distribution profiles obtained by the BJH method (Figure [10b](#page-12-0),d) show average pore diameters of 7.56 and 8.02 nm, indicating that both materials are predominantly mesoporous.

<span id="page-12-0"></span>**Figure 10.** N<sup>2</sup> adsorption–desorption isotherms and pore size distribution of (**a**,**b**) the Ni90Mo10-CK and (**c**,**d**) the 3% Pt/Ni90Mo10-CK materials.

The morphological and textural characteristics of the electrocatalysts play a crucial role in determining their electrochemical behavior. The high BET surface area and mesoporous structure observed in the 3% Pt/Ni90Mo10-CK catalyst (124.69 m<sup>2</sup> g −1 , average pore size 8.02 nm) provide a greater number of accessible active sites for the hydrogen reactions, and promote the efficient mass transport of reactants and products. The mesopores, typically arising from interparticle voids and slit-like structures as indicated by the H3-type hysteresis, facilitate the diffusion of H<sup>2</sup> and OH<sup>−</sup> species during the HER and HOR, thus lowering the overpotential and improving reaction kinetics. Moreover, the smaller particle size of the Pt nanoparticles (1.95 ± 0.32 nm) increases the surface-to-volume ratio, enhancing the catalytic utilization of Pt. The improved activity observed in both the HER (η<sup>10</sup> = 65.2 mV) and the HOR (J<sup>o</sup> = 1.03 mA cm−<sup>2</sup> , Tafel slope = 32.9 mV dec−<sup>1</sup> ) can be directly attributed to this optimized combination of nanostructure, pore size, and surface area.

Table [5](#page-13-2) summarizes the textural parameters of the materials in this study, and Figure S15 in the Supplementary Materials shows the N<sup>2</sup> adsorption–desorption isotherms and the pore size distribution for the Carbon Ketjenblack EC-300J, Ni-CK, and Mo-CK materials. The incorporation of Ni and Mo decreases the surface area of CK, with Mo producing the greatest reduction. However, once Pt was loaded, the surface area increased again due to the small Pt particles deposited on the surface of the materials.

*Catalysts* **2025**, *15*, 633 14 of 20

| Material             | Surface Area<br>(m2 g−1) | Total Pore Volume<br>(cm3 g−1) | Average Pore Size<br>(nm) |
|----------------------|--------------------------|--------------------------------|---------------------------|
| CK                   | 759.52                   | 1.14                           | 6.03                      |
| Ni-CK                | 297.73                   | 0.42                           | 5.64                      |
| Mo-CK                | 6.25                     | 0.01                           | 7.62                      |
| Ni90Mo10-CK          | 51.99                    | 0.09                           | 7.56                      |
| 3%<br>Pt/Ni90Mo10-CK | 124.69                   | 0.25                           | 8.02                      |

<span id="page-13-2"></span>**Table 5.** Summary of surface area, total pore volume, and average pore size of materials.

# **3. Materials and Methods**

#### *3.1. Reagents*

Nickel (II) nitrate hexahydrate (Ni(NO3)2·6H2O, ≥98%), phosphomolybdic acid hydrate (H3[P(Mo3O10)4]·xH2O, 99.99%), potassium hexachloroplatinate (IV) (K2PtCl6, 99%), potassium hydroxide (KOH, 99.9%), and Nafion®-117 solution (5%) were purchased from Sigma-Aldrich® (Saint Louis, MO, USA). Acetone (C3H6O, 99.7%) and ethanol (C2H6O, 99%) were acquired from Fermont (Mexico City, Mexico). Carbon Ketjenblack EC-300J, Carbon Black Vulcan XC 72R, commercial 20% Pt/C were obtained from Fuel Cell Store® (Bryan, TX, USA). High-Purity grade argon/hydrogen mixture (Ar/H<sup>2</sup> 95/5, 99.99%), nitrogen (99.5%), carbon monoxide compressed (99.99%), and pure hydrogen (99.99%) were purchased from Infra® (Naucalpan, Mexico). Deionized (DI) water used throughout the experiments was obtained from a Millipore DI water (18 MΩ Millipore®) system (St. Louis, MO, USA).

### *3.2. Synthesis of the Ni-CK, Mo-C, Ni90Mo10-CK, and NixMo100*−*x-CK*

The synthesis process is shown in Schemes [1](#page-13-0) and [2.](#page-13-1) The materials were synthesized through the incipient wetness impregnation method [\[26\]](#page-17-8), followed by the thermal reduction method [\[6\]](#page-16-5). For the Ni90Mo10-C, 0.587 mmol of nickel (Ni(NO3)2·6H2O) and 0.064 mmol of molybdenum (H3[P(Mo3O10)4]·xH2O) were perfectly dissolved in a small ethanol volume and incorporated on 60 mg of Carbon Ketjenblack (CK) through incipient wetness impregnation to reach 40% of metal loading. The obtained powder was dried overnight at 100 ◦C and then smashed with a mortar to obtain a fine powder. The powder was subjected to thermal reduction in a tubular furnace at 550 ◦C under a gas mixture of Ar/H<sup>2</sup> (95:5) for 4 h (10 ◦C min−<sup>1</sup> ). Subsequently, the material was cooled to room temperature with a pure Ar flow. The NixMo100−x-CK materials (x = 10, 30, 50, 70, 80, 85, 90, 95) were prepared for the study of the effect of the metal proportion. For the monometallic materials, the procedure was the same as that for their respective precursor quantities of Ni (0.696 mmol) and Mo (0.417 mmol) on 60 mg of carbon source.

<span id="page-13-0"></span>**Scheme 1.** Synthesis scheme of the Ni-CK, Mo-CK, and NixMo100−x-CK materials.

<span id="page-13-1"></span>**Scheme 2.** Schematic illustration for the synthesis of the Pt/Ni90Mo10-CK materials.

*Catalysts* **2025**, *15*, 633 15 of 20

# *3.3. Synthesis of the Pt/Ni90Mo10-CK*

The Pt deposition onto the Ni90Mo10-CK base material was carried out by a basic impregnation method. Firstly, different concentrations of K2PtCl<sup>6</sup> (0.002, 0.005, 0.009 mmol corresponding to 1%, 3%, and 5 wt% Pt) were dissolved in vials with 7 mL of DI water under magnetic stirring for 2 h. Then, 30 mg of the Ni90Mo10-CK was added to each vial and exposed to an ultrasound probe until uniform dispersion. After that, the dispersions were subjected to magnetic stirring at 120 ◦C until they obtained a dried powder. Subsequently, the material was dried overnight at 100 ◦C in a furnace to eliminate the residual moisture. To reduce the Pt precursor, the powder was deposited on a porcelain boat in a tubular furnace at 180 ◦C under Ar/H<sup>2</sup> (95:5) a gas mixture for 2 h (10 ◦C min−<sup>1</sup> ). Finally, the treated powder was washed with ethanol and DI water several times. Additionally, Pt-C was synthesized using the same method to obtain different Pt loading on the carbon support.

#### *3.4. Electrochemical Measurement*

An electrochemical measurement test was performed by a typical three electrodes system with Hg/HgO/NaOH 1.0 M employed as the reference electrode, Pt coil as a counter electrode, and glassy carbon (5 mm diameter) as a working electrode. All the electrochemical tests were performed using a Biologic SP-150 potentiostat/galvanostat (EC-Lab®, Nashville, TN, USA). The catalytic ink was prepared by dispersing 7 mg of catalyst powders in 904 µL of ethanol and 70 µL of Nafion-117® solution (5 wt%) by ultrasonication. An amount of 10 µL of the ink was applied to the vitreous carbon, for a total of 70 µL. Prior to evaluating the HER performance of the NiMo-CK base materials, 1.0 M KOH electrolyte was saturated with N<sup>2</sup> by bubbling for 15 min, followed by the electrocatalyst material activation by cyclic voltammetry (CV) between −1.0 and 0.4 V vs. Hg/HgO with a scanning rate of 50 mV s−<sup>1</sup> and 20 mV s−<sup>1</sup> for 15 and 5 cycles, respectively, to reach stability. Then the HER polarization curves were obtained by a sweep rate of 5 mV s−<sup>1</sup> . Employing the same three electrodes system and the same ink load on the working electrode, the materials were activated through CV (under N<sup>2</sup> atmosphere) and subsequently evaluated in the HOR. The samples were performed by hydrodynamic conditions (1600 rpm) under H<sup>2</sup> atmosphere in an electrolytic solution of 0.1 M KOH. Rotating disk electrode (RDE) measurements were taken from 0 to 0.45 V vs. RHE, with a scan rate of 1 mV s−<sup>1</sup> .

The β-NiOOH method and CO stripping were performed on a vitreous carbon electrode (0.079 cm<sup>2</sup> ) modified with 30 µL of catalytic ink. Both measurements were made in 0.1 M KOH solution. For the β-NiOOH method, chronoamperometry was first performed at −1.3 V vs. Hg/HgO for 5 min, followed by another chronoamperometry at −0.8 V vs. Hg/HgO. Then, 100 cyclic voltammetry of 0.1 to 0.7 V vs. Hg/HgO at 100 mV s−<sup>1</sup> was performed.

For CO stripping, the solution was first saturated with CO and a potential of −0.8 mV vs. Hg/HgO was applied for 15 min to adsorb the CO. Argon was then bubbled for 10 min to remove the CO from the solution. Finally, CO removal was performed by cyclic voltammetry at 50 mV s−<sup>1</sup> .

The long-term HER stability was carried out by chronopotentiometry test at an applied current density of 10 mA cm−<sup>2</sup> for 24 h.

The potential lectures obtained from each experiment were calibrated to the reversible hydrogen electrode (RHE) by the Nernst equation:

$$E_{RHE} = E_{Hg/HgO} + E_{Hg/HgO}^{\circ} + 0.059 \times \text{pH}$$
 (9)

where ERHE represents the converted potential vs. RHE, EHg/HgO is the measured potential from the reference electrode, E◦ Hg/HgO is the standard potential of Hg/HgO electrode, and pH is the pH from the electrolytic solution.

*Catalysts* **2025**, *15*, 633 16 of 20

#### *3.5. Physicochemical Characterization*

The crystalline phases of the synthesized materials were identified by means of an X-ray diffractometer D8 Advance, Bruker® (Billerica, MA, USA) with a Cu Kα radiation source (λ = 1.541). The equipment was configured in a typical Bragg–Brentano arrangement. The spectra were obtained in an angle range from 10 to 60◦ of 2θ, with a scanning step of 0.005◦ of 2θ and a step time of 0.7 s.

The ultra-high vacuum (UHV) system Scanning XPS microprobe PHI 5000 VersaProbe II (ULVAC-PHI, Inc., City of Industry, CA, USA), equipped with a 200 µm beam diameter Al Kα X-ray source (h = 1486.6 eV) monochromatic and an MCD analyzer, was used to carry out X-ray photoelectron spectroscopy (XPS) studies. XPS spectra were corrected to the binding energy of C 1s (284.70 eV).

Field Emission Scanning Electron Microscope (FE-SEM) was employed to obtain the energy dispersive X-ray spectroscopy (EDS) spectrum of the materials which was obtained with a JSM-7800F Prime (JEOL Ltd., Tokyo, Japan). The morphology of the powders was characterized using transmission electron microscopy (TEM) with a JEM-ARM200F (JEOL Ltd., Tokyo, Japan).

BET surface area and pore size distribution of the materials were obtained by N<sup>2</sup> adsorption/desorption at 77 K using a BELSORP-Mini II Instrument (Bel-Japan, Toyonaka, Japan).

# **4. Conclusions**

In summary, we developed a range of efficient trimetallic materials synthesized by a basic thermal reduction technique. The oxophilic properties of Ni and Mo contributed to improving the adsorption–desorption of H<sup>2</sup> on the Pt/Ni90M10-CK based catalyst, showing a high electrochemical yield. The obtained 3% Pt/Ni90Mo10-CK exhibited the most effective kinetic parameters for dual reactions (HER and HOR). This work reveals the role of the Ni/Mo molar ratio in optimizing catalyst performance and its contribution to reducing the Pt content needed (3% of Pt) to achieve better performance than a commercial 20% Pt catalyst.

**Supplementary Materials:** The following supporting information can be downloaded at: [https://](https://www.mdpi.com/article/10.3390/catal15070633/s1) [www.mdpi.com/article/10.3390/catal15070633/s1,](https://www.mdpi.com/article/10.3390/catal15070633/s1) Figure S1: Cyclic voltammetry by the β-NiOOH method of (a) Mo-CK and (b) Pt/Ni90Mo10-CK electrocatalysts; Figure S2: Cyclic voltammetry by the β-NiOOH method of Pt-C; Figure S3: Cyclic voltammetry by CO stripping of 20% Pt-C; Figure S4: (a–d) Catalytic performance of the NixMo100−x-CK materials; Figure S5: HER catalytic evaluation of the Ni90Mo<sup>10</sup> base material with modifications on (a) synthesis temperatures, (b) metal loading, (c) carbon allotropes, and (d) difference between bimetallic and trimetallic catalysts performance; Figure S6: (a) TEM micrography and (b) XRD pattern of Mo-CK; Figure S7: (a) TEM micrography and (b) XRD pattern of Ni-CK; Figure S8: TEM images of (a–c) Ni90Mo10-CK and (d–f) 3% Pt/Ni90Mo10- CK; Figure S9: XRD patterns of the NixMo100−x-CK materials; Figure S10: TEM micrograph and lattice spacing of the 3% Pt/Ni90Mo10/CK material; Figure S11: XPS analysis of the Mo-CK material. (a) Survey spectrum; (b) C 1s; (c) O 1s; (d) Mo 3d; Figure S12: XPS spectra of the Ni-CK catalyst: (a) Survey; (b) C 1s; (c) O 1s; (d) Ni 2P; Figure S13: (a) XPS survey scan of the Ni90Mo10-CK and corresponding deconvolution of (b) C 1s, (c) O 1s, (d) Mo 3d, and (e) Ni 2p; Figure S14: EDS spectrum of (a) Ni90Mo10-CK and (b) 3% Pt/Ni90Mo10-CK; Figure S15: N<sup>2</sup> adsorption–desorption isotherms and pore size distribution of (a,d) CK, (b–e) Ni-CK, and (c,f) Mo-CK materials; Table S1: Summary of the ECSA results of the Pt/Ni90Mo10-CK electrocatalysts by the β-NiOOH method; Table S2: Comparison of the HER performance for Ni90Mo10-CK and Pt/Ni90Mo10-CK with recently reported electrocatalysts in 1.0 M KOH; Table S3: Structural parameters such as crystallite size, strain, dislocation density, and crystallinity percentage calculated using XRD patterns. Refs. [\[6,](#page-16-5)[35,](#page-17-17)[38,](#page-18-0)[57](#page-18-18)[–65\]](#page-19-0) are cited in the supplementary materials.

*Catalysts* **2025**, *15*, 633 17 of 20

**Author Contributions:** L.F.C.-E.: investigation, formal analysis, writing—original draft. E.A.R.-S.: supervision, investigation, formal analysis. B.T.-N.: investigation, formal analysis. B.A.-V.: investigation, formal analysis. C.S.-C.: supervision, investigation, formal analysis. R.M.F.-N.: conceptualization, funding acquisition, investigation, formal analysis, writing—review and editing. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was funded by National Technological Institute of Mexico, grant number 19297.24-P and 21565.25-P.

**Data Availability Statement:** The data presented in this study are available upon request from the corresponding authors.

**Acknowledgments:** Thanks, the National Council of Humanities, Sciences, and Technologies (CONAHCYT, Mexico) for scholarship for master's studies. The authors thank the CONAHCYT National Laboratory in Hydrogen Technologies (LANH2) for allowing the use of its facilities. The authors thank E. Romero-Ibarra, L. Bazán, and L. Huerta from UNAM for their technical help in TEM and XPS studies.

**Conflicts of Interest:** The authors declare no conflicts of interest.

# **References**

- <span id="page-16-0"></span>1. Morales-Guio, C.G.; Stern, L.-A.; Hu, X. Nanostructured Hydrotreating Catalysts for Electrochemical Hydrogen Evolution. *Chem. Soc. Rev.* **2014**, *43*, 6555. [\[CrossRef\]](https://doi.org/10.1039/C3CS60468C) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/24626338)
- <span id="page-16-1"></span>2. Bai, S.; Yang, M.; Jiang, J.; He, X.; Zou, J.; Xiong, Z.; Liao, G.; Liu, S. Recent Advances of MXenes as Electrocatalysts for Hydrogen Evolution Reaction. *npj 2D Mater. Appl.* **2021**, *5*, 78. [\[CrossRef\]](https://doi.org/10.1038/s41699-021-00259-4)
- <span id="page-16-2"></span>3. Alsawat, M.; Alshehri, N.A.; Shaltout, A.A.; Ahmed, S.I.; Al-Malki, H.M.O.; Das, M.R.; Boukherroub, R.; Amin, M.A.; Ibrahim, M.M. Enhanced Alkaline Hydrogen Evolution on Gd1.0/Ndx (x = 0.5, 1.0, 3.0, and 6.0%)-Doped TiO<sup>2</sup> Bimetallic Electrocatalysts. *Catalysts* **2023**, *13*, 1192. [\[CrossRef\]](https://doi.org/10.3390/catal13081192)
- <span id="page-16-3"></span>4. Wang, C.; Shang, H.; Xu, H.; Du, Y. Nanoboxes Endow Non-Noble-Metal-Based Electrocatalysts with High Efficiency for Overall Water Splitting. *J. Mater. Chem. A* **2021**, *9*, 857–874. [\[CrossRef\]](https://doi.org/10.1039/D0TA10596A)
- <span id="page-16-4"></span>5. Cai, W.; Liu, X.; Wang, L.; Wang, B. Design and Synthesis of Noble Metal–Based Electrocatalysts Using Metal–Organic Frameworks and Derivatives. *Mater. Today Nano* **2022**, *17*, 100144. [\[CrossRef\]](https://doi.org/10.1016/j.mtnano.2021.100144)
- <span id="page-16-5"></span>6. Singh, V.K.; Gupta, U.; Mukherjee, B.; Chattopadhyay, S.; Das, S. MoS<sup>2</sup> Nanosheets on MoNi4/MoO<sup>2</sup> Nanorods for Hydrogen Evolution. *ACS Appl. Nano Mater.* **2021**, *4*, 886–896. [\[CrossRef\]](https://doi.org/10.1021/acsanm.0c03296)
- 7. Badreldin, A.; Abusrafa, A.E.; Abdel-Wahab, A. Oxygen-Deficient Cobalt-Based Oxides for Electrocatalytic Water Splitting. *ChemSusChem* **2021**, *14*, 10–32. [\[CrossRef\]](https://doi.org/10.1002/cssc.202002002)
- 8. Cao, X.; Wang, T.; Jiao, L. Transition-Metal (Fe, Co, and Ni)-Based Nanofiber Electrocatalysts for Water Splitting. *Adv. Fiber Mater.* **2021**, *3*, 210–228. [\[CrossRef\]](https://doi.org/10.1007/s42765-021-00065-z)
- 9. Nivetha, R.; Sajeev, A.; Mary Paul, A.; Gothandapani, K.; Gnanasekar, S.; Bhardwaj, P.; Jacob, G.; Sellappan, R.; Raghavan, V.; N, K.C.; et al. Cu Based Metal Organic Framework (Cu-MOF) for Electrocatalytic Hydrogen Evolution Reaction. *Mater. Res. Express* **2020**, *7*, 114001. [\[CrossRef\]](https://doi.org/10.1088/2053-1591/abb056)
- <span id="page-16-6"></span>10. Nadar, A.; Banerjee, A.M.; Pai, M.R.; Antony, R.P.; Patra, A.K.; Sastry, P.U.; Donthula, H.; Tewari, R.; Tripathi, A.K. Effect of Mo Content on Hydrogen Evolution Reaction Activity of Mo2C/C Electrocatalysts. *Int. J. Hydrog. Energy* **2020**, *45*, 12691–12701. [\[CrossRef\]](https://doi.org/10.1016/j.ijhydene.2020.02.156)
- <span id="page-16-7"></span>11. Anantharaj, S.; Kundu, S.; Noda, S. Progress in Nickel Chalcogenide Electrocatalyzed Hydrogen Evolution Reaction. *J. Mater. Chem. A* **2020**, *8*, 4174–4192. [\[CrossRef\]](https://doi.org/10.1039/C9TA14037A)
- <span id="page-16-8"></span>12. Du, W.; Shi, Y.; Zhou, W.; Yu, Y.; Zhang, B. Unveiling the In Situ Dissolution and Polymerization of Mo in Ni4Mo Alloy for Promoting the Hydrogen Evolution Reaction. *Angew. Chemie Int. Ed.* **2021**, *60*, 7051–7055. [\[CrossRef\]](https://doi.org/10.1002/anie.202015723)
- 13. Yao, R.; Zhou, Y.; Shi, H.; Wan, W.; Zhang, Q.; Gu, L.; Zhu, Y.; Wen, Z.; Lang, X.; Jiang, Q. Nanoporous Surface High-Entropy Alloys as Highly Efficient Multisite Electrocatalysts for Nonacidic Hydrogen Evolution Reaction. *Adv. Funct. Mater.* **2021**, *31*, 2009613. [\[CrossRef\]](https://doi.org/10.1002/adfm.202009613)
- 14. Song, J.; Jin, Y.Q.; Zhang, L.; Dong, P.; Li, J.; Xie, F.; Zhang, H.; Chen, J.; Jin, Y.; Meng, H.; et al. Phase-Separated Mo–Ni Alloy for Hydrogen Oxidation and Evolution Reactions with High Activity and Enhanced Stability. *Adv. Energy Mater.* **2021**, *11*, 2003511. [\[CrossRef\]](https://doi.org/10.1002/aenm.202003511)
- <span id="page-16-9"></span>15. Xu, X.; Yu, X.; Guo, K.; Dong, L.; Miao, X. Alkaline Media Regulated NiFe-LDH-Based Nickel–Iron Phosphides toward Robust Overall Water Splitting. *Catalysts* **2023**, *13*, 198. [\[CrossRef\]](https://doi.org/10.3390/catal13010198)

*Catalysts* **2025**, *15*, 633 18 of 20

<span id="page-17-0"></span>16. Regmi, Y.N.; Waetzig, G.R.; Duffee, K.D.; Schmuecker, S.M.; Thode, J.M.; Leonard, B.M. Carbides of Group IVA, VA and VIA Transition Metals as Alternative HER and ORR Catalysts and Support Materials. *J. Mater. Chem. A* **2015**, *3*, 10085–10091. [\[CrossRef\]](https://doi.org/10.1039/C5TA01296A)

- 17. Meyer, S.; Nikiforov, A.V.; Petrushina, I.M.; Köhler, K.; Christensen, E.; Jensen, J.O.; Bjerrum, N.J. Transition Metal Carbides (WC, Mo2C, TaC, NbC) as Potential Electrocatalysts for the Hydrogen Evolution Reaction (HER) at Medium Temperatures. *Int. J. Hydrog. Energy* **2015**, *40*, 2905–2911. [\[CrossRef\]](https://doi.org/10.1016/j.ijhydene.2014.12.076)
- <span id="page-17-1"></span>18. Wan, C.; Regmi, Y.N.; Leonard, B.M. Multiple Phases of Molybdenum Carbide as Electrocatalysts for the Hydrogen Evolution Reaction. *Angew. Chemie Int. Ed.* **2014**, *126*, 6525–6528. [\[CrossRef\]](https://doi.org/10.1002/ange.201402998)
- <span id="page-17-2"></span>19. Dubouis, N.; Grimaud, A. The Hydrogen Evolution Reaction: From Material to Interfacial Descriptors. *Chem. Sci.* **2019**, *10*, 9165–9181. [\[CrossRef\]](https://doi.org/10.1039/C9SC03831K)
- 20. Peng, L.; Liao, M.; Zheng, X.; Nie, Y.; Zhang, L.; Wang, M.; Xiang, R.; Wang, J.; Li, L.; Wei, Z. Accelerated Alkaline Hydrogen Evolution on M(OH)X/M-MoPO<sup>X</sup> (M = Ni, Co, Fe, Mn) Electrocatalysts by Coupling Water Dissociation and Hydrogen Ad-Desorption Steps. *Chem. Sci.* **2020**, *11*, 2487–2493. [\[CrossRef\]](https://doi.org/10.1039/C9SC04603H)
- <span id="page-17-3"></span>21. Luo, Y.; Zhang, Z.; Yang, F.; Li, J.; Liu, Z.; Ren, W.; Zhang, S.; Liu, B. Stabilized Hydroxide-Mediated Nickel-Based Electrocatalysts for High-Current-Density Hydrogen Evolution in Alkaline Media. *Energy Environ. Sci.* **2021**, *14*, 4610–4619. [\[CrossRef\]](https://doi.org/10.1039/D1EE01487K)
- <span id="page-17-4"></span>22. Chen, Z.; Liu, X.; Shen, T.; Wu, C.; Zu, L.; Zhang, L. Porous NiFe Alloys Synthesized via Freeze Casting as Bifunctional Electrocatalysts for Oxygen and Hydrogen Evolution Reaction. *Int. J. Hydrog. Energy* **2021**, *46*, 37736–37745. [\[CrossRef\]](https://doi.org/10.1016/j.ijhydene.2021.09.059)
- <span id="page-17-5"></span>23. Lima, D.W.; Trombetta, F.; Paula Benvenutti, P.; Teixeira, S.R.; Martini, E.M.A. Effect of Different Carbon Supports for Ni Particles for the HER in Tetra-alkylammonium-sulfonic Acid Media. *Int. J. Energy Res.* **2019**, *43*, 7352–7363. [\[CrossRef\]](https://doi.org/10.1002/er.4765)
- <span id="page-17-6"></span>24. Hu, T.; Fan, Y.; Ye, Y.; Cai, Y.; Liu, J.; Ma, Y.; Li, P.; Liang, C. Laser Irradiation-Induced Pt-Based Bimetallic Alloy Nanostructures without Chemical Reducing Agents for Hydrogen Evolution Reaction. *Catalysts* **2023**, *13*, 1018. [\[CrossRef\]](https://doi.org/10.3390/catal13061018)
- <span id="page-17-7"></span>25. Popov, A.A.; Afonnikova, S.D.; Varygin, A.D.; Bauman, Y.I.; Trenikhin, M.V.; Plyusnin, P.E.; Shubin, Y.V.; Vedyagin, A.A.; Mishakov, I.V. Pt1−xNi<sup>x</sup> Alloy Nanoparticles Embedded in Self-Grown Carbon Nanofibers: Synthesis, Properties and Catalytic Activity in HER. *Catalysts* **2023**, *13*, 599. [\[CrossRef\]](https://doi.org/10.3390/catal13030599)
- <span id="page-17-8"></span>26. Kabir, S.; Lemire, K.; Artyushkova, K.; Roy, A.; Odgaard, M.; Schlueter, D.; Oshchepkov, A.; Bonnefont, A.; Savinova, E.; Sabarirajan, D.C.; et al. Platinum Group Metal-Free NiMo Hydrogen Oxidation Catalysts: High Performance and Durability in Alkaline Exchange Membrane Fuel Cells. *J. Mater. Chem. A* **2017**, *5*, 24433–24443. [\[CrossRef\]](https://doi.org/10.1039/C7TA08718G)
- <span id="page-17-9"></span>27. Park, J.; Jang, J.; Lee, A.; Kim, S.; Lee, S.; Yoo, S.J.; Lee, J. Effect of Support for Non-Noble NiMo Electrocatalyst in Alkaline Hydrogen Oxidation. *Adv. Sustain. Syst.* **2022**, *6*, 2100226. [\[CrossRef\]](https://doi.org/10.1002/adsu.202100226)
- <span id="page-17-10"></span>28. Duan, Y.; Yu, Z.-Y.; Yang, L.; Zheng, L.-R.; Zhang, C.-T.; Yang, X.-T.; Gao, F.-Y.; Zhang, X.-L.; Yu, X.; Liu, R.; et al. Bimetallic Nickel-Molybdenum/Tungsten Nanoalloys for High-Efficiency Hydrogen Oxidation Catalysis in Alkaline Electrolytes. *Nat. Commun.* **2020**, *11*, 4789. [\[CrossRef\]](https://doi.org/10.1038/s41467-020-18585-4) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/32963247)
- <span id="page-17-11"></span>29. Zhao, Y.; Tian, C.; Zhai, Y.; Li, X.; Li, J.; Chen, H.; Cheng, L.; Zhao, H.; Dai, P. Ternary MoWNi Alloy as a Bifunctional Catalyst for Alkaline Hydrogen Oxidation and Evolution Reactions. *Catalysts* **2025**, *15*, 15. [\[CrossRef\]](https://doi.org/10.3390/catal15010015)
- <span id="page-17-12"></span>30. Zhu, S.; Liu, T.; Yu, S.; Yang, H.; Sun, Q.; Zheng, J.Y. Constructing Stable MoOx-NiSx Film via Electrodeposition and Hydrothermal Method for Water Splitting. *Catalysts* **2023**, *13*, 1426. [\[CrossRef\]](https://doi.org/10.3390/catal13111426)
- <span id="page-17-13"></span>31. Kamel, M.M.; Abd-Ellah, A.A.; Alhadhrami, A.; Ibrahim, M.M.; Anwer, Z.M.; Shata, S.S.; Mostafa, N.Y. Ni-Mo Nanostructure Alloys as Effective Electrocatalysts for Green Hydrogen Production in an Acidic Medium. *RSC Adv.* **2025**, *15*, 1344–1357. [\[CrossRef\]](https://doi.org/10.1039/D4RA08619H) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/39816181)
- <span id="page-17-14"></span>32. Li, X.; Peng, Z.; Jia, D.; Wang, Y.; Wu, W.; Deng, P.; Xu, M.; Xu, X.; Jia, G.; Ye, W.; et al. Interfacial Electronic Rearrangement and Synergistic Catalysis for Alkaline Water Splitting in Carbon-Encapsulated Ni (111)/Ni3C (113) Heterostructures. *Catalysts* **2022**, *12*, 1367. [\[CrossRef\]](https://doi.org/10.3390/catal12111367)
- <span id="page-17-15"></span>33. Kim, H.; Park, H.; Tran, D.S.; Kim, S.-K. Facile Fabrication of Amorphous NiMo Catalysts for Alkaline Hydrogen Oxidation Reaction. *J. Ind. Eng. Chem.* **2021**, *94*, 309–316. [\[CrossRef\]](https://doi.org/10.1016/j.jiec.2020.10.042)
- <span id="page-17-16"></span>34. Xu, Z.; Hao, M.; Liu, X.; Ma, J.; Wang, L.; Li, C.; Wang, W. Co(OH)<sup>2</sup> Nanoflowers Decorated α-NiMoO<sup>4</sup> Nanowires as a Bifunctional Electrocatalyst for Efficient Overall Water Splitting. *Catalysts* **2022**, *12*, 1417. [\[CrossRef\]](https://doi.org/10.3390/catal12111417)
- <span id="page-17-17"></span>35. Neumüller, D.; Rafailovi´c, L.D.; Pašti, I.A.; Griesser, T.; Gammer, C.; Eckert, J. Revealing the Role of Mo Leaching in the Structural Transformation of NiMo Thin Film Catalysts upon Hydrogen Evolution Reaction. *Small* **2024**, *20*, 2402200. [\[CrossRef\]](https://doi.org/10.1002/smll.202402200)
- <span id="page-17-18"></span>36. Zhao, Z.; Liu, H.; Gao, W.; Xue, W.; Liu, Z.; Huang, J.; Pan, X.; Huang, Y. Surface-Engineered PtNi-O Nanostructure with Record-High Performance for Electrocatalytic Hydrogen Evolution Reaction. *J. Am. Chem. Soc.* **2018**, *140*, 9046–9050. [\[CrossRef\]](https://doi.org/10.1021/jacs.8b04770) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/29983055)
- <span id="page-17-19"></span>37. Chen, H.; Wang, G.; Gao, T.; Chen, Y.; Liao, H.; Guo, X.; Li, H.; Liu, R.; Dou, M.; Nan, S.; et al. Effect of Atomic Ordering Transformation of PtNi Nanoparticles on Alkaline Hydrogen Evolution: Unexpected Superior Activity of the Disordered Phase. *J. Phys. Chem. C* **2020**, *124*, 5036–5045. [\[CrossRef\]](https://doi.org/10.1021/acs.jpcc.9b10384)

*Catalysts* **2025**, *15*, 633 19 of 20

<span id="page-18-0"></span>38. He, Y.; Hu, J.; Yin, W.; Xing, Y.; Hu, F.; Wei, H.; Wei, H.; Li, J. Disordered and Ultrafine PtNiMo Alloy for Superior Electrocatalytic Hydrogen Evolution in Alkaline. *Mater. Chem. Phys.* **2023**, *301*, 127585. [\[CrossRef\]](https://doi.org/10.1016/j.matchemphys.2023.127585)

- <span id="page-18-1"></span>39. Cossar, E.; Houache, M.S.E.; Zhang, Z.; Baranova, E.A. Comparison of Electrochemical Active Surface Area Methods for Various Nickel Nanostructures. *J. Electroanal. Chem.* **2020**, *870*, 114246. [\[CrossRef\]](https://doi.org/10.1016/j.jelechem.2020.114246)
- <span id="page-18-2"></span>40. Ciapina, E.G.; Santos, S.F.; Gonzalez, E.R. Electrochemical CO Stripping on Nanosized Pt Surfaces in Acid Media: A Review on the Issue of Peak Multiplicity. *J. Electroanal. Chem.* **2018**, *815*, 47–60. [\[CrossRef\]](https://doi.org/10.1016/j.jelechem.2018.02.047)
- <span id="page-18-3"></span>41. Danisman, B.; Zhang, G.-R.; Baumunk, A.F.; Yang, J.; Brummel, O.; Darge, P.; Mayrhofer, K.J.J.; Libuda, J.; Ledendecker, M.; Etzold, B.J.M. Strong Activity Changes Observable during the First Pretreatment Cycles of Trimetallic PtNiMo/C Catalysts. *ChemElectroChem* **2023**, *10*, e202300109. [\[CrossRef\]](https://doi.org/10.1002/celc.202300109)
- <span id="page-18-4"></span>42. Ordóñez, L.C.; Roquero, P.; Sebastian, P.J.; Ramírez, J. CO Oxidation on Carbon-Supported PtMo Electrocatalysts: Effect of the Platinum Particle Size. *Int. J. Hydrog. Energy* **2007**, *32*, 3147–3153. [\[CrossRef\]](https://doi.org/10.1016/j.ijhydene.2006.02.035)
- <span id="page-18-5"></span>43. Cruz-Reyes, I.; Trujillo-Navarrete, B.; García-Tapia, K.; Salazar-Gastélum, M.I.; Paraguay-Delgado, F.; Félix-Navarro, R.M. Pd/MnO<sup>2</sup> as a Bifunctional Electrocatalyst for Potential Application in Alkaline Fuel Cells. *Fuel* **2020**, *27*, 118470. [\[CrossRef\]](https://doi.org/10.1016/j.fuel.2020.118470)
- <span id="page-18-6"></span>44. Sadeghi, E.; Chamani, S.; Erdem, E.; Peighambardoust, N.S.; Aydemir, U. NiMo/CoMoO<sup>4</sup> Heterostructure with Confined Oxygen Vacancy for Active and Durable Alkaline Hydrogen Evolution Reaction. *ACS Appl. Energy Mater.* **2023**, *6*, 7658–7671. [\[CrossRef\]](https://doi.org/10.1021/acsaem.3c01146)
- <span id="page-18-7"></span>45. Wei, H.; Xi, Q.; Chen, X.; Guo, D.; Ding, F.; Yang, Z.; Wang, S.; Li, J.; Huang, S. Molybdenum Carbide Nanoparticles Coated into the Graphene Wrapping N-Doped Porous Carbon Microspheres for Highly Efficient Electrocatalytic Hydrogen Evolution Both in Acidic and Alkaline Media. *Adv. Sci.* **2018**, *5*, 1700733. [\[CrossRef\]](https://doi.org/10.1002/advs.201700733)
- <span id="page-18-8"></span>46. Hussain, S.; Muhammad, S.; Faizan, M.; Nam, K.-W.; Kim, H.-S.; Vikraman, D.; Jung, J. Hierarchical Mo2C@CNT Hybrid Structure Formation for the Improved Lithium-Ion Battery Storage Performance. *Nanomaterials* **2021**, *11*, 2195. [\[CrossRef\]](https://doi.org/10.3390/nano11092195)
- <span id="page-18-9"></span>47. Li, H.; Li, H.; Qiu, Y.; Liu, S.; Fan, J.; Guo, X. Improving Oxygen Vacancies by Cobalt Doping in MoO<sup>2</sup> Nanorods for Efficient Electrocatalytic Hydrogen Evolution Reaction. *Nano Sel.* **2021**, *2*, 2148–2158. [\[CrossRef\]](https://doi.org/10.1002/nano.202100075)
- <span id="page-18-10"></span>48. Liu, B.; Li, H.; Cao, B.; Jiang, J.; Gao, R.; Zhang, J. Few Layered N, P Dual-Doped Carbon-Encapsulated Ultrafine MoP Nanocrystal/MoP Cluster Hybrids on Carbon Cloth: An Ultrahigh Active and Durable 3D Self-Supported Integrated Electrode for Hydrogen Evolution Reaction in a Wide PH Range. *Adv. Funct. Mater.* **2018**, *28*, 1801527. [\[CrossRef\]](https://doi.org/10.1002/adfm.201801527)
- <span id="page-18-11"></span>49. Zhang, Y.; Wang, Y.; Jia, S.; Xu, H.; Zang, J.; Lu, J.; Xu, X. A Hybrid of NiMo-Mo2C/C as Non-Noble Metal Electrocatalyst for Hydrogen Evolution Reaction in an Acidic Solution. *Electrochim. Acta* **2016**, *222*, 747–754. [\[CrossRef\]](https://doi.org/10.1016/j.electacta.2016.11.031)
- <span id="page-18-12"></span>50. Kurys, Y.I.; Mazur, D.O.; Koshechko, V.G.; Pokhodenko, V.D. Nanocomposite Based on N,P-Doped Reduced Graphene Oxide, Mo2C, and Mo2N as Efficient Electrocatalyst for Hydrogen Evolution in a Wide PH Range. *Electrocatalysis* **2021**, *12*, 469–477. [\[CrossRef\]](https://doi.org/10.1007/s12678-021-00667-6)
- <span id="page-18-13"></span>51. Hou, H.; Wang, W.; Kang, Q.; Wang, J.; Chen, Z.; Wang, Y.; Cui, Y.; Yu, Y.; Zhu, J.; Yan, H.; et al. Undoped MoO<sup>X</sup> with Oxygen-Rich Vacancies as Hole Transport Material for Efficient Indoor/Outdoor Organic Solar Cells. *Nano Energy* **2024**, *131*, 110173. [\[CrossRef\]](https://doi.org/10.1016/j.nanoen.2024.110173)
- <span id="page-18-14"></span>52. Salunkhe, P.; Kekuda, D. Effect of Annealing Temperature on the Physical Properties of NiO Thin Films and ITO/NiO/Al Schottky Diodes. *J. Mater. Sci. Mater. Electron.* **2022**, *33*, 21060–21074. [\[CrossRef\]](https://doi.org/10.1007/s10854-022-08910-6)
- 53. Seo, K.; Jeong, S.-M.; Lim, T.; Ju, S. Continuous Hydrogen Regeneration through the Oxygen Vacancy Control of Metal Oxides Using Microwave Irradiation. *RSC Adv.* **2018**, *8*, 37958–37964. [\[CrossRef\]](https://doi.org/10.1039/C8RA08055K) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/35558584)
- <span id="page-18-15"></span>54. Xiong, D.; Li, W.; Liu, L. Vertically Aligned Porous Nickel (II) Hydroxide Nanosheets Supported on Carbon Paper with Long-Term Oxygen Evolution Performance. *Chem.—An Asian J.* **2017**, *12*, 543–551. [\[CrossRef\]](https://doi.org/10.1002/asia.201601590)
- <span id="page-18-16"></span>55. Jiang, Y.; Fu, T.; Liu, J.; Zhao, J.; Li, B.; Chen, Z. Molten Salt Synthesis of Carbon-Supported Pt–Rare Earth Metal Nanoalloy Catalysts for Oxygen Reduction Reaction. *RSC Adv.* **2022**, *12*, 4805–4812. [\[CrossRef\]](https://doi.org/10.1039/D1RA09400A)
- <span id="page-18-17"></span>56. Ratke, L.; Gurikov, P. Specific Surface Area. In *The Chemistry and Physics of Aerogels*; Gurikov, P., Ratkd, L., Eds.; Cambridge University Press: Cambridge, UK, 2021; pp. 236–267.
- <span id="page-18-18"></span>57. Soo, J.Z.; Riaz, A.; Zhang, D.; Jagadish, C.; Tan, H.H.; Karuturi, S. Enhancing the Hydrogen Evolution Reaction Performance of Solution-Corroded NiMo via Plasma Modification. *Chem. Mater.* **2024**, *36*, 4164–4173. [\[CrossRef\]](https://doi.org/10.1021/acs.chemmater.3c02978)
- 58. Zhang, T.; Debow, S.; Song, F.; Qian, Y.; Creasy, W.R.; DeLacy, B.G.; Rao, Y. Interface Catalysis of Nickel Molybdenum (NiMo) Alloys on Two-Dimensional (2D) MXene for Enhanced Hydrogen Electrochemistry. *J. Phys. Chem. Lett.* **2021**, *12*, 11361–11370. [\[CrossRef\]](https://doi.org/10.1021/acs.jpclett.1c02676)
- 59. Yang, C.; Zhou, L.; Yan, T.; Bian, Y.; Hu, Y.; Wang, C.; Zhang, Y.; Shi, Y.; Wang, D.; Zhen, Y.; et al. Synergistic Mechanism of Ni(OH)2/NiMoS Heterostructure Electrocatalyst with Crystalline/Amorphous Interfaces for Efficient Hydrogen Evolution over All PH Ranges. *J. Colloid Interface Sci.* **2022**, *606*, 1004–1013. [\[CrossRef\]](https://doi.org/10.1016/j.jcis.2021.08.090)
- 60. Chen, Q.; Cao, Z.; Du, G.; Kuang, Q.; Huang, J.; Xie, Z.; Zheng, L. Excavated Octahedral Pt-Co Alloy Nanocrystals Built with Ultrathin Nanosheets as Superior Multifunctional Electrocatalysts for Energy Conversion Applications. *Nano Energy* **2017**, *39*, 582–589. [\[CrossRef\]](https://doi.org/10.1016/j.nanoen.2017.07.041)

*Catalysts* **2025**, *15*, 633 20 of 20

61. Wu, W.; Tang, Z.; Wang, K.; Liu, Z.; Li, L.; Chen, S. Peptide Templated AuPt Alloyed Nanoparticles as Highly Efficient Bi-Functional Electrocatalysts for Both Oxygen Reduction Reaction and Hydrogen Evolution Reaction. *Electrochim. Acta* **2018**, *260*, 168–176. [\[CrossRef\]](https://doi.org/10.1016/j.electacta.2017.11.057)

- 62. Qin, X.; Zhang, L.; Xu, G.-L.; Zhu, S.; Wang, Q.; Gu, M.; Zhang, X.; Sun, C.; Balbuena, P.B.; Amine, K.; et al. The Role of Ru in Improving the Activity of Pd toward Hydrogen Evolution and Oxidation Reactions in Alkaline Solutions. *ACS Catal.* **2019**, *9*, 9614–9621. [\[CrossRef\]](https://doi.org/10.1021/acscatal.9b01744)
- 63. Mosallaei, H.; Hadadzadeh, H.; Ensafi, A.A.; Mousaabadi, K.Z.; Weil, M.; Foelske, A.; Sauer, M. Evaluation of HER and OER Electrocatalytic Activity over RuO2–Fe2O<sup>3</sup> Nanocomposite Deposited on HrGO Nanosheets. *Int. J. Hydrogen Energy* **2023**, *48*, 1813–1830. [\[CrossRef\]](https://doi.org/10.1016/j.ijhydene.2022.10.026)
- 64. Du, Z.; Wang, Y.; Li, J.; Liu, J. Facile Fabrication of Pt–Ni Alloy Nanoparticles Supported on Reduced Graphene Oxide as Excellent Electrocatalysts for Hydrogen Evolution Reaction in Alkaline Environment. *J. Nanoparticle Res.* **2019**, *21*, 13. [\[CrossRef\]](https://doi.org/10.1007/s11051-018-4436-7)
- <span id="page-19-0"></span>65. de la Cruz-Cruz, J.J.; Domínguez-Crespo, M.A.; Ramírez-Meneses, E.; Torres-Huerta, A.M.; Brachetti-Sibaja, S.B.; Rodríguez-Salazar, A.E.; Pastor, E.; González-Sánchez, L.E. Data Supporting the in Situ Synthesis by Organometallic Method of Vulcan Supported PdNi Nanostructures for Hydrogen Evolution Reaction in Alkaline Solution. *Data Br.* **2022**, *42*, 108256. [\[CrossRef\]](https://doi.org/10.1016/j.dib.2022.108256)

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.