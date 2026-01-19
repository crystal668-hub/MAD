---
source: Attias 等 - 2021 - Optimization of Ni−Co−Fe‐Based Catalysts for Oxygen Evolution Reaction by Surface and Relaxation Phe.pdf
tool: marker
duration: 105.422s
generated: 2026-01-09T19:39:08.351720Z
---

# Optimization of Ni—Co—Fe-Based Catalysts for Oxygen Evolution Reaction by Surface and Relaxation Phenomena Analysis

Rinat Attias,<sup>[a]</sup> Kalimuthu Vijaya Sankar,<sup>[a, b]</sup> Kapil Dhaka,<sup>[c]</sup> Wenjamin Moschkowitsch,<sup>[d]</sup> Lior Elbaz,<sup>[d]</sup> Maytal Caspary Toroker,<sup>[a, c]</sup> and Yoed Tsur\*<sup>[a, b]</sup>

Trimetallic double hydroxide NiFeCo–OH is prepared by coprecipitation, from which three different catalysts are fabricated by different heat treatments, all at 350 °C maximum temperature. Among the prepared catalysts, the one prepared at a heating and cooling rate of  $2\,^{\circ}\text{C}$  min $^{-1}$  in  $N_2$  atmosphere (designated NiFeCo– $N_2$ -2 °C) displays the best catalytic properties after stability testing, exhibiting a high current density (9.06 mA cm $^{-2}$  at 320 mV), low Tafel slope (72.9 mV dec $^{-1}$ ), good stability (over 20 h), high turnover frequency (0.304 s $^{-1}$ ), and high mass activity (46.52 Ag $^{-1}$  at 320 mV). Stability tests reveal

that the hydroxide phase is less suitable for long-term use than catalysts with an oxide phase. Two causes are identified for the loss of stability in the hydroxide phase: a) Modeling of the distribution function of relaxation times (DFRT) reveals the increase in resistance contributed by various relaxation processes; b) density functional theory (DFT) surface energy calculations reveal that the higher surface energy of the hydroxide-phase catalyst impairs the stability. These findings represent a new strategy to optimize catalysts for water splitting.

#### Introduction

Electrochemical hydrogen production plays a vital role in the field of eco-friendly energy storage and conversion applications. [1-3] Water splitting is a sustainable approach for converting electrical energy into chemical energy (oxygen and hydrogen) without  $\rm CO_2$  emission at site. Two half-cell reactions occur during the water splitting process: oxygen evolution reaction (OER) and hydrogen evolution reaction (HER). The benchmark catalysts for OER are lr- and Ru-based oxides in acidic medium. Likewise, Pt-based compounds are benchmark catalysts for HER. [4-6]

During overall water splitting, OER is the major bottleneck due to several reaction steps involved in transferring the required four electrons, which slows down the reaction kinetics.<sup>[5,7]</sup> The standard reaction potential to split water is 1.23 V vs. RHE. Practically, there is a kinetic hindrance, which

 [a] R. Attias, Dr. K. Vijaya Sankar, Prof. M. Caspary Toroker, Prof. Y. Tsur The Nancy and Stephen Grand Technion Energy Program Technion-Israel Institute of Technology Haifa 3200003 (Israel)
E-mail: tsur@technion.ac.il

[b] Dr. K. Vijaya Sankar, Prof. Y. Tsur Department of Chemical Engineering Technion-Israel Institute of Technology Haifa 3200003 (Israel)

[c] Dr. K. Dhaka, Prof. M. Caspary Toroker Department of Materials Science and Engineering Technion-Israel Institute of Technology Haifa 3200003 (Israel)

[d] W. Moschkowitsch, Prof. L. Elbaz Department of Chemistry Bar Ilan University Ramat Gan 5290002 (Israel)

Supporting information for this article is available on the WWW under https://doi.org/10.1002/cssc.202002946

leads to an increase in overpotential. Thus, it is desirable to develop an efficient catalyst which executes the reaction at a low overpotential, exhibits good stability and earth abundant for OER.<sup>[8,9]</sup> Nobel metal oxides (Ir- and Ru-based compounds) partially meet most of the previous demands in alkaline and acidic medium.<sup>[10]</sup> However, high cost, limited stability and low-abundance limit their use in large-scale applications.<sup>[11]</sup>

To date, many research efforts have been dedicated to identifying catalysts capable of meeting the above requirements. Transition metal-based hydroxides and oxyhydroxides show better catalytic activities in alkaline solution.<sup>[12-15]</sup> Ni(OH)<sub>2</sub>/NiOOH in different compositions is one of the most studied catalyst family. It was found that catalysts of this family fulfill most of the above mentioned requirements in the alkaline medium.<sup>[5,11,16,17]</sup> Many reasons for enhancement of electrochemical performance using both experimental and theoretical approaches have been published.<sup>[5,11,16-25]</sup> Yet, there are only few reports relating electrocatalytic performances with surface energy of the catalyst. Xiang et al.<sup>[26]</sup> has noted that low surface energy catalysts exhibit good stability and vice versa.

Usually, the electrocatalytic performances of the catalyst were investigated by cyclic voltammetry (CV), linear sweep voltammetry (LSV), chronoamperometry or chronopotentiometry and electrochemical impedance spectroscopy (EIS). In this context, EIS is a vastly used analytical technique to identify electrochemical phenomena in the sample. Most commonly, an equivalent circuit helps extract the physical parameters from EIS. Sometimes, however, the same equivalent circuit does not fit the impedance spectra of the same catalyst under different conditions or during degradation, which may point to possible misinterpretation of the results. To overcome these issues, Tsur et al. developed MATLAB-based genetic programming to analyze and extract the physical information from EIS.<sup>[27]</sup> Genetic

1737

, 7, Downloaded from https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.202002946 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons. License

programming provides an analytical form of the distribution function of relaxation times (DFRT) that consists of a linear combination of known peaks taken from a library. Ideally, each peak represents a different electrochemical phenomenon occurring in and on the catalyst. The program does not rely on filtering with tweaking parameters that influence the results. Various systems have been analyzed using this technique, for instance, solid oxide fuel cells, solid oxide electrolyzers, supercapacitors, batteries, and electrocatalysts at various reactions. [27–32] To our knowledge, hardly any reports discuss DFRT modelling for electrocatalysts. [32]

In this work, we have combined and elucidated the importance of DFRT modelling and theoretical surface energy calculations for understanding the stability of OER catalysts. We have prepared  $\text{Ni}_{0.81}\text{Fe}_{0.12}\text{Co}_{0.07}(\text{OH})_2$  as a parent catalyst and its heat-treated derivatives for the test  $(\text{Ni}_{0.81}\text{Fe}_{0.12}\text{Co}_{0.07}(\text{OH})_2$  showed low stability compared to its heat-treated analogue). The doping percentages of both iron and cobalt have been selected after a series of experiments. First, we carried out doping with iron in different percentages until optimization. Then, we added cobalt in different percentages until optimized. Herein, we only report on the optimized electrocatalyst.

#### **Results and Discussion**

#### Physicochemical characterization of precatalysts

The phases and crystallinity of the catalysts were analyzed with X-ray diffraction (XRD). Figure 1a displays the XRD patterns of NiFeCo–OH, NiFeCo–N<sub>2</sub>-2°C, NiFeCo–N<sub>2</sub>–5°C and NiFeCo–Air-2°C. The diffraction peaks of NiFeCo–OH match with  $\alpha$ -Ni(OH)<sub>2</sub>·0.75H<sub>2</sub>O (JCPDS file no. 00–038-0715). After heat treatment, the observed diffraction peaks look like a NiO-phase indicating suppression or disappearance of the hydroxide phase. The latter formed regardless of the heating/cooling rates and atmosphere. The diffraction planes (NiFeCo–N<sub>2</sub>-2°C, NiFeCo–N<sub>2</sub>–5°C and NiFeCo–Air-2°C) have been indexed and fit with NiO (JCPDS file no. 01–078-4367). All patterns show broad diffraction peaks, as expected from nanocrystalline samples.  $^{[6,33]}$  No other peaks were identified in the XRD.

Thermogravimetric and differential thermal analyses (TGA/DTA) were conducted to study the influence of thermal treatment on the NiFeCo–OH phase, in an inert atmosphere, and in air at rates of 2 °C min<sup>-1</sup> and 5 °C min<sup>-1</sup>. Figure 1b shows the TGA curves of NiFeCo–OH at different conditions. In all cases, the weight loss before ca. 200 °C, is the removal of adsorbed and crystalline water molecules.

In air, NiFeCo–OH displays a clear weight loss between 219 °C and 356 °C. It is due to the decomposition of NiFeCo (OH)<sub>2</sub> to NiFeCoO<sub>x</sub> by releasing water molecules. <sup>[34,35]</sup> The conversion was not completed because a small amount of Ni<sup>2+</sup> was oxidized to a higher oxidation state. This step is an endothermic reaction, as seen by DTA (see the Supporting Information, Figure S1). Above 356 °C, the oxidized NiFeCoO<sub>x</sub> (x > 1) decomposes to NiFeCoO.

**Figure 1.** a) XRD pattern of the catalysts. b) TGA curves of NiCoFe—OH at different conditions (inset: schematic illustration of the conversion of hydroxide phase into hydroxide/oxide or oxide phase).

The TGA profile of NiFeCo-OH looks different under an inert atmosphere. The decomposition temperature of NiFeCo-OH shifts slightly higher when the heating rate is raised to 5°C min<sup>-1</sup>. Depending on the heat conduction and the particle size, at a higher heating rate the temperature difference between the center and the surface of the particle may be larger. This might slow down the decomposition process, as seen for the 5°C sample. For both heating rates, NiFeCo-OH shows two distinct weight loss regions beyond 200 °C. The decomposition of NiFeCo(OH)<sub>2</sub> to NiFeCo(OH)<sub>2</sub>/NiFeCoO<sub>x</sub> by releasing water molecules is marked as Region I. Then, a slower weight loss (Region II) is observed, which might be related to the final conversion of NiFeCo(OH)<sub>2</sub>/NiFeCoO<sub>x</sub> into NiFeCoO<sub>y</sub>. [34,35] It suggests that the material has mixed phases of an amorphous NiFeCo(OH)<sub>2</sub> and nonstoichiometric NiFeCoO at a temperature of 350 °C. [36] However, due to the NiFeCo(OH)<sub>2</sub> is minute quantity or amorphous nature is not identified by XRD and selected area electron diffraction pattern (Figure S2). The possible weight loss mechanisms of NiFeCo-OH in air and inert atmosphere are depicted schematically in the inset of Figure 1b. The synergistic effect of mixed phases in heat-treated inert atmosphere samples is expected to contribute to better catalytic activity.[37]

Chemistry Europe European Chemical Societies Publishing

We have identified the valence states of the surface elements using X-ray photoelectron spectroscopy (XPS). All the catalysts contain Ni, Fe, Co and O as the elements. Figure 2 and Figures S3-S5 show the deconvoluted XPS spectra of Ni2p, Fe2p, Co2p, and O1s in NiFeCo-N<sub>2</sub>-2 °C, NiFeCo-OH, NiFeCo-N<sub>2</sub>-5 °C, and NiFeCo-Air-2 °C, respectively.

The Ni spectra (Figure S3a) shows a doublet peak at 855.5 eV  $(2p_{3/2})$  and 872.9 eV  $(2p_{1/2})$  as well as a satellite peak at 861.3 eV. All of these peaks are attributed to Ni<sup>2+</sup> and agree well with the literature. [38-40] After heat treatment (Figure 2a, S4a, S5a), the binding energy is slightly shifted compared to NiFeCo-OH (Table 1). The observed satellite at 880.0 eV in a heat-treated catalyst could be a sign that some Ni is in the oxidation state +3 but no major peak was found for it.

Fe is in oxidation state +3, which can be seen at the peaks at 711.5 eV  $(2p_{3/2})$  and 724.3 eV  $(2p_{1/2};$  Figure S3b), as well as the satellite peak at 719.2 eV. The peak at 706.2 eV is a Ni Auger

peak.[38,39,41,42] The binding energy of peaks is lightly -deviated (Table 1) after heat treatment (Figures 2b, S4b, and S5b).

The Co spectrum shows a main peak at 780.7 eV  $(2p_{3/2})$  and a peak at 795.9 eV (2p<sub>1/2</sub>; Figure S3c) which is a doublet attributed to Co<sup>2+</sup> and Co<sup>3+</sup> mixed oxidation states. The peak at 786.0 eV is a satellite peak, the peak at 773.8 is a Co Auger peak.[39,42,43] A similar kind of peak with a slight shift in binding energy (Table 1) is observed after heat treatment (Figure 2c, S4c, and S5c). In Figure S3d, the O1s peak is at 531.1 eV, which shows oxygen deficiency.<sup>[44]</sup> O1s spectra of the heat-treated catalysts are displayed in Figure 2d, S4d, S5d. Here too, the O1s peak appears at around 531 eV (Table 1). The presence of oxygen vacancies could assist in OH<sup>-</sup> ion adsorption. [45-47]

We examined the morphological features of the catalysts using high-resolution scanning electron microscopy (HRSEM). Figure 3a shows a typical HRSEM image of NiFeCo-OH. The particle surfaces have a flake-like-shape. The size and thickness

Figure 2. Deconvoluted high-resolution X-ray photoelectron spectra of NiFeCo-N<sub>2</sub>-2 °C: a) Ni2p; b) Fe2p; c) Co2p; d) O1s.

www.chemsuschem.org

| Table 1. Binding e          | energies [e               | /] of Ni, Fe      | , Co, and C | ) in the pre | epared cata               | alysts.           |       |          |                           |                   |       |       |       |
|-----------------------------|---------------------------|-------------------|-------------|--------------|---------------------------|-------------------|-------|----------|---------------------------|-------------------|-------|-------|-------|
| Catalyst                    | Ni2p<br>2p <sub>3/2</sub> | 2p <sub>1/2</sub> | Sat.1       | Sat.2        | Fe2p<br>2p <sub>3/2</sub> | 2p <sub>1/2</sub> | Sat.  | Ni Auger | Co2p<br>2p <sub>3/2</sub> | 2p <sub>1/2</sub> | Sat.  | Auger | O1 s  |
| NiFeCo-OH                   | 855.5                     | 872.9             | 861.3       | _            | 711.5                     | 724.3             | 719.2 | 706.2    | 780.7                     | 795.9             | 786.0 | 773.8 | 531.1 |
| NiFeCo-N <sub>2</sub> -2 °C | 855.9                     | 873.7             | 861.9       | 880.0        | 712.1                     | 724.9             | 718.6 | 705.5    | 781.4                     | 796.9             | 787.0 | 774.8 | 531.4 |
| NiFeCo-N <sub>2</sub> -5 °C | 856.4                     | 874.2             | 862.3       | 880.5        | 712.8                     | 724.4             | 718.2 | 706.8    | 781.5                     | 797.3             | 786.8 | 774.6 | 531.4 |
| NiFeCo–Air-2°C              | 855.4                     | 873.2             | 861.5       | 879.4        | 711.8                     | 724.3             | 717.9 | 705.4    | 780.6                     | 796.7             | 786.7 | 773.6 | 530.8 |

**Figure 3.** High-resolution scanning electron microscopy images: a) NiFeCo-OH; b) NiFeCo-N<sub>2</sub>-2 °C; c) NiFeCo-N<sub>2</sub>-5 °C; d) NiFeCo-Air-2 °C.

of the flakes are about 100 and 20 nm, respectively. After heat treatment (Figure 3b,c) in the inert atmosphere, the original shape of the particles is lost and larger aggregates are seen. Likewise, air heat-treated catalysts show slight aggregation with fewer surface pores (Figure 3d).

X-ray fluorescence measurements were carried out to quantify the elemental composition in the catalysts (Table 2). These values are equal to the expected compositions and show that the NiFeCo—OH is composed of 81.6 at% Ni, 11.7 at% Fe and 6.7 at% Co. NiFeCo—N<sub>2</sub>—2 °C, NiFeCo—N<sub>2</sub>—5 °C and NiFeCo—Air—2 °C have nearly the same metal ratios. Here, the reported atomic percentage corresponds to the average value of the powder. The atomic percentage of elements in the selected area is determined using EDAX (Figures S6—S9). The calculated atomic percentage values are very close to the values measured with XRF (Tables S1—S4).

Figure S10 shows the nitrogen adsorption—desorption isotherms at 77 K, t-plot and pore size distribution plots. All isotherms (Figure S10a,b) belong to a type IV adsorption-

Table 2. Elemental compositions of the catalysts [at.%] determined by Xray fluorescence measurements. Catalyst Fe Co NiFeCo-OH 81.6 11.7 6.7 NiFeCo-N2-2°C 80.9 12.1 7.0 NiFeCo-N2-5°C 80.7 12.5 6.8

797

desorption isotherm. Further, the hysteresis loop confirms the mesoporous nature of the catalysts. [48] Table 3 summarizes the N<sub>2</sub> physisorption results of the catalysts. Using the Brunauer-Emmett-Teller (BET) model, the calculated specific surface areas are 283, 298, 259 and 282 m<sup>2</sup> g<sup>-1</sup> for NiFeCo-OH, NiFeCo-N<sub>2</sub>-2°C, NiFeCo-N<sub>2</sub>-5°C and NiFeCo-Air-2°C, respectively. These results indicate that the heating/cooling rate has no net effect on the specific surface area. Further, the t-plot model (Figure S10c) was used to measure the specific surface area contributed by the external surface. The results show that NiFeCo-N<sub>2</sub>-2°C and NiFeCo-N<sub>2</sub>-5°C have micropores along with mesopores. The specific surface area and pore volume contributed by micropore in those samples are found to be 43 m<sup>2</sup> g<sup>-1</sup> and 19 mm<sup>3</sup> g<sup>-1</sup>, respectively. No micropores are detected in the samples that were not heat treated under inert atmosphere. The meso- and micropores enable electrolyte diffusion and thus enhance the active sites. [48]

The Barrett–Joyner–Halenda (BJH) model was used to calculate the pore size distribution in the catalysts (Figure S10d,e and Table 3). For NiFeCo– $N_2$ – $2\,^{\circ}$ C and NiFeCo– $N_2$ – $5\,^{\circ}$ C, the pore size of the micropores was calculated by the Horvath–Kawazoe model and the results show that the median pore width is 0.5 nm for both catalysts.

#### **Electrocatalytic activity**

Three electrode cells (working: catalyst modified GCE; counter: Pt wire; reference: Hg/HgO) have been used to measure the catalyst's OER activities in 0.1 M KOH electrolyte. First, the catalysts were activated by 100 cycles (0.2-0.8 V vs Hg/HgO) at a scan rate of 10 mV s<sup>-1</sup> in 0.1 M KOH. During the activation cycles, the transition metal hydroxide or oxide is converted into transition metal oxyhydroxide. In addition, Fe intercalation into the metal oxyhydroxide matrix from the unpurified KOH electrolyte probably increases the OER activity of the catalyst. [49] The LSV curves of bare GCE (glassy carbon electrode), and of various catalysts deposited on GCE: RuO2, NiFe-OH, NiFeCo-OH, NiFeCo-N<sub>2</sub>-2°C, NiFeCo-N<sub>2</sub>-5°C and NiFeCo-Air-2°C has recorded at a scan rate of 5 mV s<sup>-1</sup>. Figure 4a displays the IRcorrected polarization curves of the catalysts. The resistance for the IR-correction was taken from EIS measurements, which were analyzed using the ISGP method.<sup>[27–31]</sup> Figure S12 shows the comparison of LSV curves of NiFeCo-N2-2°C with and without IR correction.

The oxidation peak (ca. 1.45 V vs RHE) can be observed in all polarization curves except for  $RuO_2$  and GCE (Figure 4a). The

| Catalyst                    | Surface are<br>Total <sup>[a]</sup> | a [m² g <sup>-1</sup> ]<br>External <sup>[b]</sup> | Internal <sup>[b]</sup> | Micropore volume <sup>[b]</sup><br>[cm³ g <sup>-1</sup> ] | Average diameter <sup>[c]</sup><br>[nm] | Median pore width <sup>[c</sup><br>[nm] |
|-----------------------------|-------------------------------------|----------------------------------------------------|-------------------------|-----------------------------------------------------------|-----------------------------------------|-----------------------------------------|
| NiFeCo-OH                   | 283                                 | _                                                  | _                       | _                                                         | 13.2                                    | _                                       |
| NiFeCo-N <sub>2</sub> -2 °C | 298                                 | 255                                                | 43                      | 0.019                                                     | 12.3                                    | 0.5                                     |
| NiFeCo-N <sub>2</sub> -5 °C | 259                                 | 216                                                | 43                      | 0.019                                                     | 14.4                                    | 0.5                                     |
| NiFeCo-Air-2°C              | 282                                 | _                                                  | _                       | _                                                         | 12.2                                    | _                                       |

NiFeCo-Air-2°C

13.1

72

, 7, Downloaded from https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.202002946 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons. License

Figure 4. a) Polarization curves of NiFeCo-OH, NiFeCo-N<sub>2</sub>-2 °C, NiFeCo-N<sub>2</sub>-5 °C, NiFeCo-Air-2 °C, RuO<sub>2</sub>, and GCE in 0.1 M KOH at a scan rate of 5 mV s<sup>-1</sup>. b) TOFs of catalysts as a function of potential. c) Tafel plots of the catalysts. d) Chronoamperometric curves of the catalysts for 20 h at an overpotential of 300 mV.

origin of the oxidation peak is from the transition of Ni<sup>2+</sup> to Ni<sup>3+</sup>. The presence of Co lowers the oxidation potential of nonconductive Ni<sup>2+</sup> to conductive Ni<sup>3+</sup>, owing to the charge transfer effect derived from Co. In contrast, Fe stabilizes the oxidation state of Ni<sup>2+</sup> and creates more disordered local structures.<sup>[5,19]</sup> After heat treatment, the oxidation peak current drops, suggesting a decrease in the electrochemical surface area or active sites, indicating a crystalline phase of catalysts.<sup>[19]</sup> For all catalysts, the oxygen evolution reaction begins after the oxidation peak, and an increase in current density is seen.<sup>[50]</sup>

The OER activity of GCE and RuO<sub>2</sub> is lower than the activity of electrocatalysts prepared in this study (Figure 4a). NiFeCo-OH delivers a high current density of 10.54 mA cm<sup>-2</sup> at an overpotential of 320 mV, which is higher than NiFe-OH  $(4.90 \text{ mA cm}^{-2}),$ NiFeCo-N<sub>2</sub>-2°C  $(3.64 \text{ mA cm}^{-2}),$ NiFeCo-N<sub>2</sub>-5°C  $(3.20 \text{ mA cm}^{-2})$ and NiFeCo-Air-2°C (2.05 mA cm<sup>-2</sup>). Furthermore, the mass activities of RuO<sub>2</sub>, NiFeCo-OH, NiFe-OH, NiFeCo-N2-2°C, NiFeCo-N2-5°C and NiFeCo-Air-2°C are found to be 7.61, 54.39, 25.26, 18.78, 16.43 and 10.55 Ag<sup>-1</sup>, respectively, at an overpotential of 320 mV (Figure S13). These results suggest that hydroxide phases increase the areal and mass current densities compared to heattreated catalysts.

Turnover frequencies (TOFs) were calculated to evaluate the reaction kinetics [see the Supporting Information, Equation (S4)].<sup>[51]</sup> For TOF calculation, the surface concentration of active site values is changeable according to the calculation procedure, which impacts the TOF value. The calculated area under the reduction peak is one of the most common methods for determining the surface concentration of active sites or atoms.<sup>[51]</sup> Figure 4b shows the calculated TOF values of catalysts at different potentials. NiFeCo-N<sub>2</sub>-2°C exhibits a TOF value of  $0.123~\text{s}^{-1}$  at an overpotential of 320 mV. It is higher than the values obtained for NiFeCo-OH (0.051 s<sup>-1</sup>), NiFeCo-N<sub>2</sub>-5°C (0.106 s<sup>1</sup>) and NiFeCo-Air-2°C (0.079 s<sup>-1</sup>). The hydroxide catalyst slows down the reaction kinetics. In contrast, heat-treated catalysts, specifically the catalyst prepared at a slow rate under an inert atmosphere, accelerates the reaction kinetics. The obtained TOF value of NiFeCo- $N_2$ - $2\,^{\circ}$ C is high compared to other reported catalysts. [52-55]

The logarithmic current density vs. overpotential plot represents the Tafel plot of the catalysts (Figure 4c). Usually, a

Chemistry Europe

European Chemical Societies Publishing

1,7, Downloaded from https://chemistry-urope.onlinelibrary.wiley.com/doi/10.1002/csec2020002946 by University Of Science, Wiley Online Library on [06/01/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons. License

good electrocatalyst exhibits a low Tafel slope value. [8] Equation (S6) has been used to calculate the Tafel slope values of the catalysts. NiFeCo-N<sub>2</sub>-2°C exhibits a Tafel slope of 56 mV dec<sup>-1</sup>, which is lower than RuO<sub>2</sub> (77 mV dec<sup>-1</sup>), NiFe–OH (156 mV dec<sup>-1</sup>), NiFeCo-OH (140 mV dec<sup>-1</sup>), NiFeCo $-N_2-5$  °C (57 mV dec<sup>-1</sup>) and NiFeCo-Air-2 °C (75 mV dec<sup>-1</sup>). Likewise, the obtained value is small compared to other reports.<sup>[52,55,56]</sup> This implies that the NiFeCo-N<sub>2</sub>-2°C catalyst has good catalytic activity towards OER.

The catalysts stability during OER is one of the critical factors for practical utilization of the catalyst. Figure 4d shows the time-dependent current density curve over 20 h at overpotential of 300 mV (without IR-correction). The decline in current density occurs only for NiFe-OH, NiFeCo-OH and RuO<sub>2</sub>, indicating that these catalysts are unstable in alkaline solution. the current density for NiFeCo-N<sub>2</sub>-2°C, NiFeCo-N<sub>2</sub>-5°C and NiFeCo-Air-2°C increases with time, which demonstrates an improvement in the catalytic activity. It may originate from the increase in active sites, the creation of

mixed phases, etc.<sup>[57,58]</sup> We have observed that the hydroxide phase accelerates the reaction kinetics, but suffers from less stability. In contrast, the oxide phase is not suitable for accelerating the reaction kinetics, however, it delivers good stability. The synergistic effect of the above phases enhances reaction kinetics and stability.[59]

Figure S14 illustrates the polarization curves, mass activity, TOF and Tafel plots after 20 h of continuous electrolysis. Figure 5 summarizes the areal current, mass current, TOF and Tafel slope values of catalysts before and after the stability test at overpotential of 320 mV.

Figure 5a,b shows that the areal and mass currents drop for RuO<sub>2</sub>, NiFe-OH, and NiFeCo-OH, indicating a decrease in OER activity. In contrast, the heat-treated catalysts, especially NiFeCo-N<sub>2</sub>-2 °C, show an increase in current density, suggesting an improvement in OER activity.

Figure 5c shows the comparative TOF value of the catalysts at 320 mV. The TOF value of NiFeCo-N<sub>2</sub>-2 °C has been increased by a factor of 3.2 after the stability test and is higher

Figure 5. Comparison of catalysts before and after stability testing at an overpotential of 320 mV: a) Areal current density; b) mass current density; c) TOF values; d) Tafel slope values.

www.chemsuschem.org

1,7, Downloaded from https://chemistry-urope.onlinelibrary.wiley.com/doi/10.1002/csec2020002946 by University Of Science, Wiley Online Library on [06/01/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons. License

than the TOF values of the other catalysts. Furthermore, the Tafel slope values of the catalysts are displayed in Figure 5d. The relatively low slope value of NiFeCo– $N_2$ –2°C suggests the feasibility of that catalyst for the OER.

For a better understanding of the catalytic activity enhancement after 20 h of test, EIS was recorded before and after the stability test at an overpotential of 300 mV (without IRcorrection). The EIS spectra show two arcs (Figure S15) at high and low-frequency region. It indicates the presence of two relaxation processes. Usually, the catalysts exhibit various relaxation processes during oxygen evolution reaction:<sup>[32]</sup> solution plus other series resistances (P3), active material (P2), charge transfer (P1), and production rate of intermediates (P1'). It is hard to distinguish all those contributions by looking at the EIS spectrum alone, e.g., in the Nyquist plot. Hence, we attempted to analyze the EIS spectra of catalysts using ISGP.

The resultant DFRT plot (Figure 6a,b) is constructed by known peaks, which ideally correspond to different electrochemical phenomena. In all cases, there is one out-of-range peak that corresponds to the solution resistance plus some other series resistance (P3) contributions. Within the measured range, peaks can be characterized based on their relaxation time in the order of active material (P2; low-relaxation time/high frequency) < charge transfer (P1; mid-relaxation time/mid-

frequency) < production rate of intermediates (P1'; high-relaxation time/low-frequency). [32]

From the DFRT, the effective resistances contributed by various relaxation processes have been calculated (Figure 6c,d). Initially, the catalysts exhibit nearly the same solution plus other series resistance, active material resistance and charge transfer resistance. But the resistance to a production rate of intermediates varies based on the catalyst. NiFeCo-OH has low resistance to a production rate of intermediates that is one of the reasons for high areal and mass current densities. After the stability test the situation changes, NiFeCo-OH shows higher resistance to solution plus other series resistance, active material, and production rate of intermediates. This increase is probably the reason for the decrease in catalytic activity. However, the reduction in resistance to solution plus other series resistances, active material, charge transfer steps and intermediate products are noted for heat-treated catalysts. The reduction in resistance leads to the improvement of electrocatalytic activity and, thus,

The calculated double-layer capacitance of catalysts before/ after stability test is 3.69/2.91 mF, 2.91/5.44 mF, 2.09/2.09 mF, and 1.64/1.41 mF for NiFeCo–OH, NiFeCo–N $_2$ –2°C, NiFeCo–N $_2$ –5°C and NiFeCo–Air–2°C respectively. The double-layer capacitance of NiFeCo–OH diminished after the stability test, which infers the decrease in active sites. In contrast, the

Figure 6. a,b) DFRT plots of the catalysts before (a) and after (b) stability testing. c,d) Calculated resistance values of the relaxation process before (c) and after (d) stability testing of the catalysts.

www.chemsuschem.org

Chemistry Europe European Chemical Societies Publishing

double-layer capacitance value of NiFeCo-N2-2°C increases suggesting the increase in active sites. It leads to improvement in catalytic activity and stability. [60]

In many cases, it has been argued that Pt is not a durable and efficient catalyst for the OER process in an alkaline solution. [61,62] However, a small amount of decomposed Pt, which part of it may deposited on the working electrode, will not affect OER performance. Indeed, Pt is prone to redeposit onto the cathode and enhance the HER process in acidic solution. [63] Following the measurements performed with Pt as a counter electrode, we have examined the OER activity of the catalysts using glassy carbon electrode (GCE) as counter electrode for comparison. The data and discussion are provided in the Supporting Information (Figures S16-S18). Similar results in the catalytic activity were obtained by using a GCE rod as a counter electrode. We noticed a small difference in the current values at 320 mV vs RHE. It may be due to the large area of the glassy carbon electrode.

To offer insights into the good stability of NiFeCo-N<sub>2</sub>-2 °C, density functional theory (DFT) calculations were performed (Figure 7). We initially converged the bulk unit-cell structures based on NiO structure (NiO and  $Ni_{83.3}Fe_{12.5}Co_{4.17}O_x$ ) by using a k-mesh of  $8\times8\times8$  and structures based on  $\alpha$ -Ni(OH)<sub>2</sub> ( $\alpha$ -Ni(OH)<sub>2</sub>, and Ni<sub>83.3</sub>Fe<sub>11.1</sub>Co<sub>5.6</sub>(OH)<sub>2</sub>). The experimental compositions  $(Ni_{81.6}Fe_{11.7}Co_{6.7}(OH)_2$  and  $Ni_{81.6}Fe_{11.7}Co_{6.7}O_x)$  are close to the DFT samples. There are structural possibilities to test more Fe-Co doping sites in these calculations, but we chose one for each case where Fe-Co atoms are mostly close to the surface in order to account for the dopants' most dominant effect. For the prepared surfaces shown in Figure 7, we used larger supercells. The energy cutoff is 600 eV for the plane-wave basis set. These k-points and energy cutoffs were converged to a total energy within 1 meV per atom. For all the calculations, we relaxed the cells using a convergence criterion of 10<sup>-5</sup> eV for electronic iterations and 0.03 eV Å-1 for ionic iterations. Geometrical

Figure 7. Typical optimized model of NiO(100),  $\alpha$ -Ni(OH)<sub>2</sub>(100),  $Ni_{83.3}Fe_{12.5}Co_{4.17}O_x(100)$  and  $Ni_{83.3}Fe_{11.1}Co_{5.6}(OH)_2(100)$  surfaces. Red, gray, golden, blue, and white balls indicate O, Ni, Fe, Co, and H atoms, respectively. Created by using VESTA. [64]

relaxations took place with a conjugate gradient algorithm. All slabs were separated from their periodic image by a minimum of 14 Å vacuum layers which converged the total energy up to 1 meV atom<sup>-1</sup>.

We calculated the surface energies of the NiO and  $\alpha$ - $Ni(OH)_2$ . Surface energy  $E_{Surf}$  is defined by Equation (1):

$$E_{\text{Surf}} = \frac{E_{\text{Slab}} - E_{\text{bulk}}}{2A} \tag{1}$$

where  $E_{Slab}$  is the energy of the surface cell,  $E_{bulk}$  is the energy of the bulk structure with the same stoichiometry, and A is the surface area. The calculated surface energies are listed in Table 4. Lower surface energies point that NiO phase with and without Fe–Co doping are comparably more stable than the  $\alpha$ phase of Ni(OH)<sub>2</sub>. Higher surface energy indicates lower stability of the surface and higher catalytic efficiency. [18,26] It means that metal oxide phase is comparably more stable, in agreement with our experimental work.

#### **Conclusions**

Trimetallic OER electrocatalysts were prepared by a coprecipitation method followed by heat treatment. NiFeCo-OH shows two different weight losses between 200 and 350 °C in an inert atmosphere and a single weight loss in air. The inert atmosphere heat-treated catalyst contains a bimodal pore size distribution, but there is no huge variation in the specific surface area compared to NiFeCo-OH. The oxidation peak for Ni<sup>2+</sup> to Ni<sup>3+</sup> in the NiFeCo-OH catalyst is shifted to a lower potential compared to NiFe-OH, owing to charge transfer effects. Initially, NiFeCo-OH and NiFe-OH catalysts delivered high areal and mass activities, but also low TOFs, high Tafel slopes, and lower stabilities. In contrast, the heat-treated catalysts, especially NiFeCo-N<sub>2</sub>-2 °C, gave high TOFs, low Tafel slopes, and good stabilities, but lower areal and mass activities. After stability testing, the situation had changed, the heattreated catalyst exhibited high catalytic activity in terms of high TOF, high mass and areal current densities, and low Tafel slope. Through DFRTs, we understand that the improvements in catalytic activity and stability are due to the reduction of effective resistance contributed by various relaxation phenomena. Moreover, the low surface energy of the heat-treated catalysts led to an enhancement in the stability, which is also supported by DFT surface energy calculations.

| Table 4. Calculated surface energies of different samples from DFT.             |                                        |  |  |  |  |
|---------------------------------------------------------------------------------|----------------------------------------|--|--|--|--|
| Surface                                                                         | Surface energy<br>[J m <sup>-2</sup> ] |  |  |  |  |
| NiO(100)<br>α-Ni(OH) <sub>2</sub> (100)                                         | 0.81<br>1.07                           |  |  |  |  |
| $Ni_{83.3}Fe_{12.5}Co_{4.17}O_x$ (100)                                          | 1.00                                   |  |  |  |  |
| Ni <sub>83.3</sub> Fe <sub>11.1</sub> Co <sub>5.6</sub> (OH) <sub>2</sub> (100) | 1.05                                   |  |  |  |  |

# **Experimental Section**

#### Reagents and materials

Nickel(II) chloride hexahydrate (NiCl $_2\cdot$ 6H $_2$ O, 99.3% trace metals basis), and Cobalt(II) chloride hexahydrate (CoCl $_2\cdot$ 6H $_2$ O, 99.9% trace metals basis) were purchased from Alfa Aesar. Iron(II) chloride tetrahydrate (FeCl $_2\cdot$ 4H $_2$ O 99.0% trace metals basis), ammonium hydroxide solution, ethanol, isopropanol, Nafion perfluorinated, potassium persulfate and potassium hydroxide ( $\geq$ 85%, Fe content is  $\leq$ 0.001%) pellets were purchased from Sigma-Aldrich. All the chemicals were used directly without any further treatment. Double distilled water was utilized for material preparation and washing. The electrolyte was prepared using ultrapure (>18.2 M $\Omega$ cm) deionized water.

#### Preparation of electrocatalysts

Fe- and Co-doped Ni hydroxide nanocatalysts were prepared by coprecipitation followed by thermal treatment. NiCl<sub>2</sub>·6H<sub>2</sub>O (1.925 g, 8.1 mmol),  $CoCl_2 \cdot 6H_2O$  (0.166 g, 0.7 mmol), and  $FeCl_2 \cdot 4H_2O$ (0.238 g, 1.2 mmol) were dissolved in 100 mL of distilled water under stirring (300 rpm; at room temperature) to obtain a total of 0.1 M precursor solution. In parallel, a solution of potassium persulfate (0.3379 g, 1.25 mmol) in distilled water (50 mL) was prepared. After stirring for 15 min, the potassium persulfate solution was added slowly into the transparent precursor solution and was stirred for another 10 min. Ammonium hydroxide solution (5 mL, 30–33 % NH<sub>3</sub> in H<sub>2</sub>O) was added gradually into the solution. Stirring (300 rpm) was continued for 5 h at room temperature. A black particle suspension was formed and was left without any disturbance for 24 h at room temperature. The supernatant solution was removed from the container. The black particle sediment was washed with double-distilled water (5 times) and ethanol (2 times) and subjected to centrifugation (6000 rpm for 5 min). The product (NiFeCo-OH) was oven-dried at 60 °C overnight and ground.

The NiFeCo–OH was used as a parent compound to prepare the heat-treated samples. It was placed in an alumina boat in a programmable tubular furnace to get uniform heating. The sample was heat-treated at 350 °C for 2 h in air at a heating/cooling rate of  $2\,^{\circ}\text{C}$  min $^{-1}$ . After cooling down, the obtained product (NiFeCo–Air– $2\,^{\circ}\text{C}$ ) was grounded. A similar procedure was followed to prepare NiFeCo–N $_2$ – $2\,^{\circ}\text{C}$  and NiFeCo–N $_2$ – $5\,^{\circ}\text{C}$  under N $_2$  atmosphere (50 sccm flow rates) at heating/cooling rates of  $2\,^{\circ}\text{C}$  min $^{-1}$  and  $5\,^{\circ}\text{C}$  min $^{-1}$ , respectively.

For electrochemical comparison, NiFe–OH was prepared by using the same procedure as mentioned above. In this typical synthesis, we used NiCl $_2$ ·6H $_2$ O (2.091 g, 8.8 mmol), and FeCl $_2$ ·4H $_2$ O (0.238 g, 1.2 mmol) as raw materials.

# Catalyst ink preparation

The electrochemical analysis was performed with a glassy carbon electrode (GCE, 5 mm inner diameter; purchased from ALS Co., LTD) as support for the catalyst. Catalyst ink was prepared with 5 mg of the catalyst and a solution of ultrapure deionized water (750  $\mu L$ ), isopropanol (250  $\mu L$ ), and Nafion perfluorinated resin solution (45  $\mu L$ ). The mixture was stirred (200 rpm) for 3 h at room temperature. 8  $\mu L$  of catalyst ink was drop cast on the GCE active area (mass loading: ca. 38  $\mu g$ ). The modified GCE was dried at 30 °C for 3 h. The measurements were conducted in a three-electrode cell (working: catalyst modified GCE; counter: Pt wire  $^{[64]}/\text{GCE}$  rod; reference: Hg/HgO) in 0.1 M KOH and a potentiostat/galvanostat

(Biologic SP-300). The potentials were converted to V vs. RHE. More details are given in the Supporting Information.

# Impedance Spectroscopy analysis by Genetic Programming (ISGP)

The catalyst impedance can be written as a Fredholm equation of the second kind [Eq. (2)]:

$$Z(\omega) = R_{\infty} + R_{\text{pol}} \int_{-\infty}^{\infty} \frac{\Gamma(\log(\tau))}{1 + i\omega\tau} d(\log(\tau))$$
 (2)

where  $Z(\omega)$ ,  $R_{\infty}$ ,  $R_{\rm pol}$ ,  $\Gamma$ ,  $\tau$ , and  $\omega$  represent the impedance, series resistance, total polarization resistance, distribution function of relaxation times, relaxation time and angular frequency, respectively. For ISGP two sets of the same impedance data were added as input. The validity of the data is reviewed within the program using the Kramers-Kronig (K-K) transformation. Experimental artifacts can distort the EIS data, so the K-K transformation should give valuable input on the validity of the data. ISGP provides the output in the DFRT form. The physical parameters of each peak can be easily extracted from the DFRT, since the function is given in analytical form. The effective resistance is calculated by multiplying the area under the peak by the normalization factor (typically, the real part of the impedance at the lowest frequency). The effective capacitance can then be calculated by the central position of the peak in the time domain divided by the effective resistance. The procedure was described in full in our previous reports. [27,28,30]

### **Acknowledgements**

Financial support of the Ministry of energy and water, Israel, the Israel National Research Center for Electrochemical Propulsion (INREP) and the Grand Technion Energy Program (GTEP) are gratefully acknowledged. R.A. wishes to thank the generous support of the Leonard and Diane Sherman Interdisciplinary Graduate School Fellowship. K. V. wishes to thank the generous support of the Technion-Israel Institute of Technology postdoctoral fellowship as well as the UConn-GTEP joint program. We thank Noam Zion of BIU for XPS and Gennady Shter of Technion for TGA \DTA.

# **Conflict of Interest**

The authors declare no conflict of interest.

**Keywords:** density functional calculations · electrocatalysis · hydroxides · porous materials · relaxation processes

- [1] X. F. Lu, Y. Chen, S. Wang, S. Gao, X. W. Lou, Adv. Mater. 2019, 31, 1902339.
- [2] C. Chen, P. L. Zhang, M. Wang, D. H. Zheng, J. C. Chen, F. S. Li, X. J. Wu, K. Fan, L. C. Sun, ChemSusChem 2020, 13, 5067–5072.
- [3] Y. Wang, Y. Yang, S. F. Jia, X. M. Wang, K. J. Lyu, Y. Q. Peng, H. Zheng, X. Wei, H. Ren, L. Xiao, J. B. Wang, D. A. Muller, H. D. Abruña, B. J. Hwang, J. T. Lu, L. Zhuang, *Nat. Commun.* 2019, 10, 1506.
- [4] A. K. Tareen, G. S. Priyanga, K. Khan, E. Pervaiz, T. Thomas, M. Yang, ChemSusChem 2019, 12, 3941–3954.

- [5] L. Trotochaud, S. L. Young, J. K. Ranney, S. W. Boettcher, J. Am. Chem. Soc. 2014, 136, 6744-6753.
- [6] L.-A. Stern, X. Hu, Faraday Discuss. 2014, 176, 363-379.
- [7] J. Nai, Y. Lu, L. Yu, X. Wang, X. W. D. Lou, Adv. Mater. 2017, 29, 1703870– 1703879.
- [8] X. Li, X. Hao, A. Abudula, G. Guan, J. Mater. Chem. A 2016, 4, 11973-12000.
- [9] M. Q. Yang, J. Wang, H. Wu, G. W. Ho, Small 2018, 14, 1703323.
- [10] F. L. Lyu, Q. F. Wang, S. M. Choi, Y. D. Yin, Small 2019, 15, 1804201.
- [11] P. C. Wang, B. G. Wang, ChemSusChem 2020, 4795-4811.
- [12] J. Zhang, L. Yu, Y. Chen, X. F. Lu, S. Gao, X. W. Lou, Adv. Mater. 2020, 32, 1906432.
- [13] X. Wang, L. Yu, B. Y. Guan, S. Song, X. W. Lou, Adv. Mater. 2018, 30, 1801211.
- [14] A. Bergmann, T. E. Jones, E. Martinez Moreno, D. Teschner, P. Chernev, M. Gliech, T. Reier, H. Dau, P. Strasser, Nat. Catal. 2018, 1, 711-719.
- [15] J. Chi, H. Yu, G. Jiang, J. Jia, B. Qin, B. Yi, Z. Shao, J. Mater. Chem. A 2018, 6. 3397-3401.
- [16] P. Chakthranont, J. Kibsgaard, A. Gallo, J. Park, M. Mitani, D. Sokaras, T. Kroll, R. Sinclair, M. B. Mogensen, T. F. Jaramillo, ACS Catal. 2017, 7, 5399-5409.
- [17] W. Moschkowitsch, K. Dhaka, S. Gonen, R. Attias, Y. Tsur, M. Caspary Toroker, L. Elbaz, ACS Catal. 2020, 10, 4879-4887.
- [18] Z. Chen, C. X. Kronawitter, B. E. Koel, Phys. Chem. Chem. Phys. 2015, 17, 29387-29393
- [19] M. K. Bates, Q. Jia, H. Doan, W. Liang, S. Mukerjee, ACS Catal. 2016, 6, 155-161
- [20] J. Yan, L. Kong, Y. Ji, J. White, Y. Li, J. Zhang, P. An, S. Liu, S. T. Lee, T. Ma, Nat. Commun. 2019, 10, 2149.
- [21] T. Kou, S. Wang, J. L. Hauser, M. Chen, S. R. J. Oliver, Y. Ye, J. Guo, Y. Li, ACS Energy Lett. 2019, 4, 622-628.
- [22] H. Yuan, S. Wei, B. Tang, Z. Ma, J. Li, M. Kundu, X. Wang, ChemSusChem 2020. 13. 3662-3670.
- [23] K. Yao, M. Zhai, Y. Ni, Electrochim. Acta 2019, 301, 87-96.
- [24] G. Lin, Y. Wang, J. Hong, K. Suenaga, L. Liu, L. Y. Chang, C. W. Pao, T. Zhang, W. Zhao, F. Huang, M. Yang, Y. Y. Sun, J. Wang, ChemSusChem 2020, 13, 2739-2744.
- [25] S. Sivakumar, S. Yugeswaran, K. Vijaya Sankar, L. Kumaresan, G. Shanmugavelayutham, Y. Tsur, J. Zhu, J. Power Sources 2020, 473, 228526
- [26] J. Xiang, B. Xiang, X. Cui, New J. Chem. 2018, 42, 10791–10797.
- [27] S. B. Y. T. S. Hershkovitz, S. Tomer, ECS Trans. 2011, 33, 67–73.
- [28] Z. Drach, S. Hershkovitz, D. Ferrero, P. Leone, A. Lanzini, M. Santarelli, Y. Tsur, Solid State Ionics 2016, 288, 307-310.
- [29] S. Hershkovitz, S. Baltianski, Y. Tsur, Solid State Ionics 2011, 188, 104-
- [30] A. Oz, D. Gelman, E. Goren, N. Shomrat, S. Baltianski, Y. Tsur, J. Power Sources 2017, 355, 74-82.
- [31] D. Gelman, B. Shvartsev, I. Wallwater, S. Kozokaro, V. Fidelsky, A. Sagy, A. Oz, S. Baltianski, Y. Tsur, Y. Ein-Eli, J. Power Sources 2017, 364, 110-120.
- [32] V. S. Kalimuthu, R. Attias, Y. Tsur, Electrochem. Commun. 2020, 110, 106641.
- [33] M. Fei, H. Shi, J. Zhao, N. Kang, W. He, H. Li, F. Yang, ChemCatChem **2018**, 10, 5174-5181.
- [34] D. Wang, R. Xu, X. Wang, Y. Li, Nanotechnology 2006, 17, 979–983.
- [35] C. Bin Wang, G. Y. Gau, S. J. Gau, C. W. Tang, J. L. Bi, Catal. Lett. 2005, 101, 241-247.
- [36] F. Basharat, U. A. Rana, M. Shahid, M. Serwar, RSC Adv. 2015, 5, 86713-86722

- [37] H. Zhang, X. Li, A. Hähnel, V. Naumann, C. Lin, S. Azimi, S. L. Schweizer, A. W. Maijenburg, R. B. Wehrspohn, Adv. Funct. Mater. 2018, 28, 1706847
- [38] S. Dutta, A. Indra, Y. Feng, T. Song, U. Paik, ACS Appl. Mater. Interfaces **2017**, 9, 33766-33774.
- [39] N. Hao, Y. Wei, J. Wang, Z. Wang, Z. Zhu, S. Zhao, M. Han, X. Huang, RSC Adv. 2018, 8, 20576-20584.
- [40] V. Bachvarov, E. Lefterova, R. Rashkov, Int. J. Hydrogen Energy 2016, 41, 12762-12771.
- [41] T. Yamashita, P. Hayes, Appl. Surf. Sci. 2008, 254, 2441–2449.
- [42] A. Kumar, T. Shripathi, P. C. Srivastava, J. Sci. Adv. Mater. Devices 2016, 1, 290-294.
- [43] D. Cabrera-German, G. Gomez-Sosa, A. Herrera-Gomez, Surf. Interface Anal. 2016, 48, 252-256.
- [44] P. F. Liu, S. Yang, B. Zhang, H. G. Yang, ACS Appl. Mater. Interfaces 2016, 8, 34474-34481.
- [45] D. Chen, M. Qiao, Y. R. Lu, L. Hao, D. Liu, C. L. Dong, Y. Li, S. Wang, Angew. Chem. Int. Ed. 2018, 57, 8691-8696; Angew. Chem. 2018, 130, 8827-8832.
- [46] S. Hirai, K. Morita, K. Yasuoka, T. Shibuya, Y. Tojo, Y. Kamihara, A. Miura, H. Suzuki, T. Ohno, T. Matsuda, S. Yagi, J. Mater. Chem. A 2018, 6, 15102-15109.
- [47] Y. Zhu, L. Zhang, B. Zhao, H. Chen, X. Liu, R. Zhao, X. Wang, J. Liu, Y. Chen, M. Liu, Adv. Funct. Mater. 2019, 29, 1–12.
- [48] S. Liu, H. Zhang, Q. Zhao, X. Zhang, R. Liu, X. Ge, G. Wang, H. Zhao, W. Cai, Carbon 2016, 106, 74-83.
- [49] S. Klaus, Y. Cai, M. W. Louie, L. Trotochaud, A. T. Bell, J. Phys. Chem. C 2015, 119, 7243-7254.
- [50] B. S. Yeo, A. T. Bell, J. Am. Chem. Soc. 2011, 133, 5587–5593.
- [51] S. Anantharaj, S. R. Ede, K. Karthick, S. Sam Sankar, K. Sangeetha, P. E. Karthik, S. Kundu, Energy Environ. Sci. 2018, 11, 744-771.
- [52] A. Xie, J. Du, F. Tao, Y. Tao, Z. Xiong, S. Luo, X. Li, C. Yao, Electrochim. Acta 2019, 305, 338-348.
- [53] M. Yang, W. Lu, R. Jin, X.-C. Liu, S. Song, Y. Xing, ACS Sustainable Chem. Eng. 2019, 7, 12214-12221.
- [54] S. Kocabas, A. Cetin, A. M. Önal, E. N. Esenturk, J. Nanopart. Res. 2019, 21, 143.
- [55] L. Li, T. Tian, J. Jiang, L. Ai, J. Power Sources 2015, 294, 103-111.
- [56] J. Jiang, A. Zhang, L. Li, L. Ai, J. Power Sources 2015, 278, 445-451.
- [57] G. A. Ferrero, K. Preuss, A. B. Fuertes, M. Sevilla, M. M. Titirici, J. Mater. Chem. A 2016, 4, 2581-2589.
- [58] Y. Qian, Z. Hu, X. Ge, S. Yang, Y. Peng, Z. Kang, Z. Liu, J. Y. Lee, D. Zhao, Carbon 2017, 111, 641-650.
- [59] Z. P. Wu, X. F. Lu, S. Q. Zang, X. W. Lou, Adv. Funct. Mater. 2020, 30, 1910274.
- [60] J. Li, M. Yan, X. Zhou, Z. Q. Huang, Z. Xia, C. R. Chang, Y. Ma, Y. Qu, Adv. Funct. Mater. 2016, 26, 6785-6796.
- [61] T. Reier, M. Oezaslan, P. Strasser, ACS Catal. 2012, 2, 1765–1772.
- [62] T. Lim, M. Sung, J. Kim, Sci. Rep. 2017, 7, 5-10
- [63] R. Chen, C. Yang, W. Cai, H. Y. Wang, J. Miao, L. Zhang, S. Chen, B. Liu, ACS Energy Lett. 2017, 2, 1070-1075.
- [64] K. Momma, F. Izumi, J. Appl. Crystallogr. 2011, 44, 1272-1276.

Manuscript received: December 24, 2020 Revised manuscript received: February 9, 2021 Accepted manuscript online: February 9, 2021 Version of record online: February 24, 2021