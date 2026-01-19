---
source: Wu 等 - 2025 - Dynamic Site Induced Self‐Adaptive Adsorption on Bifunctional Catalysts for Highly Selective Oxidati.pdf
tool: marker
duration: 74.849s
generated: 2026-01-09T20:42:03.613089Z
---

# **Dynamic Site Induced Self-Adaptive Adsorption on Bifunctional Catalysts for Highly Selective Oxidative Switching from Urea-to-Water Electrolysis**

*Kai Wu, Weibin Chen, Shurui Zhu, Hongqin Liu, Dongsheng Wen, Ruqiang Zou,\* and Bingjun Zhu\**

**The adsorption strength of hydroxide ions affects the catalytic activities of the oxygen evolution reaction (OER) and urea oxidation reaction (UOR). Inspired by the "for" loop function in computer programming, this work proposes a dynamic active site strategy to modulate "self-adaptive" adsorption of OH<sup>−</sup> to achieve a continuous urea-to-water electrolysis for the first time, with a highly selective switching from UOR to OER. Specifically, MoO4 <sup>2</sup><sup>−</sup>-doped NiCo-based layered double hydroxide (NiCo-LDH-MO) is developed as the UOR/OER bifunctional catalyst through the hydrothermal doping and electrochemical reconstruction of Prussian blue analogs. With the aid of density functional theory (DFT) calculation and the in situ characterizations, it suggests that OH<sup>−</sup> is preferentially adsorbed on Co sites to generate CoOOH for UOR in the presence of urea, and then self-adaptively adsorbs on Ni sites to generate NiOOH for OER after the removal of urea. As a result, the reconstructed electrode exhibits remarkably low potentials of 1.27/1.36 V for UOR at 10/100 mA cm<sup>−</sup>2, respectively, and only 347 mV overpotential for OER at 100 mA cm<sup>−</sup>2. This work demonstrates a new pathway for the effective hydrogen and oxygen production from urea-contaminated water, such as human urine and industrial wastewater.**

K. Wu, S. Zhu, H. Liu, B. Zhu School of Aeronautic Science and Engineering Beihang University Beijing 100191, P. R. China E-mail: [zhubingjun@buaa.edu.cn](mailto:zhubingjun@buaa.edu.cn)

W. Chen, R. Zou

School of Materials Science and Engineering

Peking University Beijing 100871, P. R. China E-mail: [rzou@pku.edu.cn](mailto:rzou@pku.edu.cn)

K. Wu

Sino-French Carbon Neutrality Research Center Ecole Centrale de Pekin/School of General Engineering

Beihang University Beijing 100191, P. R. China

D. Wen

Institute of Thermodynamics Technical University of Munich 80333 Munich, Germany

The ORCID identification number(s) for the author(s) of this article can be found under <https://doi.org/10.1002/adfm.202520435>

**DOI: 10.1002/adfm.202520435**

# **1. Introduction**

The massive consumption of fossil fuels raises concern over the energy and environmental crisis, where electrolytic hydrogen production is a pivotal foundation for the future utilization of clean energy technologies.[\[1–3\]](#page-9-0) Electrocatalytic water splitting by the combination of cathodic hydrogen evolution reaction (HER) and anodic oxygen evolution reaction (OER) is one of the most critical technologies for largescale H2 production.[\[4,5\]](#page-9-0) However, the high overpotentials and sluggish kinetics of OER hinder the practical application.[\[6,7\]](#page-9-0) Therefore, the urea oxidation reaction (UOR) was applied as a favorable alternative to OER, benefitting from the lower theoretical cell voltage of urea electrolysis (0.37 V) when compared with that of water splitting (1.23 V).[\[8–11\]](#page-9-0) In addition, urea electrolysis is valuable in treating urea-rich wastewater from the fertilizer industry and biological excretions, along with efficient

and low-cost H2 production.[\[10,12,13\]](#page-9-0) Nevertheless, UOR remains mediocre in kinetics due to the six-electron transfer process and the occurrence of competitive water electrolysis.[\[14,15\]](#page-9-0) Furthermore, many earlier studies did not take the variation of urea concentration in the process of electrolysis into consideration, which may result in the cutoff of H2 production performance, particularly approaching the stage of urea depletion.[\[16–19\]](#page-9-0) To realize H2 production through continuous urea-to-water electrolysis, UOR and OER need to take place at the anode side continuously before and after urea depletion, respectively.[\[17\]](#page-9-0) In this case, it is inevitable to develop UOR/OER bifunctional catalysts to achieve this goal.[\[20,21\]](#page-9-0)

Urea-to-water electrolysis is a dynamic process with a continuously varying reaction environment, which requires UOR/OER bifunctional catalysts to possess "self-adaptive" catalytic activities.[\[22\]](#page-9-0) However, many earlier studies on UOR/OER bifunctional catalysts only focused on the performance improvement in their individual half-reactions, respectively.[\[17,23\]](#page-9-0) Previous studies revealed that the competitive adsorption of OH<sup>−</sup> severely affects the rivalry between UOR and OER.[\[24–27\]](#page-9-0) Under alkaline conditions, OH<sup>−</sup> is indispensable for a series of protoncoupled electron transfers as well as the C─N bond cleavage in

<span id="page-1-0"></span>**Figure 1.** a) A schematic of the fabrication process of NiCo-LDH-MO/NF electrode. XRD patterns of b) NiCo-PBA processor and NiCo-LDH-MO/NF electrode before activation, c) NiCo-LDH-MO/NF electrode before and after activation in 1 m KOH with and without 0.33 m urea solution.

the urea molecule during UOR.[\[26,28\]](#page-9-0) However, excessive OH<sup>−</sup> will occupy the active sites instead of urea, stimulate competitive OER over UOR as well.[\[29\]](#page-9-0) In this regard, Qiao et al. first proposed the strategy of inhibiting OH<sup>−</sup> adsorption to enhance urea coverage.[\[27\]](#page-9-0) Yin's group ensured the high coverage of urea at NiCo sites by tailoring the oxygenophilic OH<sup>−</sup> adsorption sites for efficient UOR-assisted H2 production.[\[25\]](#page-9-0) Nevertheless, the inhibition of OH<sup>−</sup> adsorption achieved enhanced UOR at the expense of OER, but ignored the demand for OH<sup>−</sup> adsorption of OER, especially when approaching the depletion of urea for continuous H2 production through water electrolysis.[\[30\]](#page-9-0) Thereby, to realize continuous electrolytic H2 production through urea-towater electrolysis, dynamic active sites can be introduced in the UOR/OER bifunctional catalysts for the self-adaptive response to OH<sup>−</sup> adsorption in the presence/absence of urea to achieve optimized performance in both reactions.[\[31–33\]](#page-9-0)

We note that the above-mentioned dynamic response possesses a cyclic character for the occurrence of oxidation and selection for UOR/OER in the presence/absence of urea, which is similar to the "for" loop function in computer programming.[\[34,35\]](#page-9-0) Previous works show that the introduction of MoO4 <sup>2</sup><sup>−</sup> has a positive effect on enhancing the strength of the 3D framework, the electronic regulation, and rapid catalyst reconstruction.[\[36,37\]](#page-9-0) Herein, we propose a strategy of the in situ reconstructive growth of MoO4 <sup>2</sup><sup>−</sup>-doped NiCo-based layered double hydroxide, to construct dynamic Co/Ni active sites and facilitate adaptive OH<sup>−</sup> adsorption in the presence/absence of urea, respectively. The assynthesized catalyst exhibits excellent bifunctional performance, requiring potentials of 1.27/1.36 V to reach 10/100 mA cm<sup>−</sup><sup>2</sup> for UOR and only overpotential of 347 mV at 100 mA cm<sup>−</sup><sup>2</sup> for OER. More importantly, with our developed catalyst, we demonstrate a continuous urea-to-water electrolytic process with an autonomous potential switching from UOR to OER by chronopotentiometry at 100 mA cm<sup>−</sup><sup>2</sup> for the first time. The incorporation of MoO4 <sup>2</sup><sup>−</sup> on Co sites can effectively modulate the electronic structure of NiCo layered double hydroxide (NiCo-LDH) to facilitate OH<sup>−</sup> adsorption, which also promotes the formation of the amorphous phase to expose more active sites.[\[38,39\]](#page-9-0) In this case,

<span id="page-2-0"></span>**Figure 2.** SEM images of a,b) NiCo-LDH-MO/NF electrode before activation; c,d) after UOR activation; e,f) after OER activation. HRTEM images of g) NiCo-LDH-MO/NF electrode before activation, after h) UOR and i) OER activation.

OH<sup>−</sup> is preferentially adsorbed on the Co sites, regardless of the presence or absence of urea. If urea is present, it directly contributes to the formation of CoOOH with comparatively higher UOR activity. Approaching the depletion of urea, OH<sup>−</sup> turns to promote the formation of NiOOH active sites for OER. This "selfadaptive" adsorption is the origin of UOR/OER bifunctionality and leads to H2 production through continuous urea-to-water electrolysis.

#### **2. Results and Discussion**

#### **2.1. Structure and Morphology**

The synthesis process of the NiCo-LDH-MO/NF electrode is shown in **Figure <sup>1</sup>**[a,](#page-1-0) where NiCo-LDH-MO denotes MoO4 <sup>2</sup><sup>−</sup> doped NiCo-based layered double hydroxide, and NF refers to the nickel foam substrate. First, the precursor bimetallic NiCo Prussian blue analogue (NiCo-PBA) was synthesized by a typical 24 h precipitation method.[\[40\]](#page-9-0) Subsequently, MoO4 <sup>2</sup><sup>−</sup> was doped into the structure of NiCo-PBA by a hydrothermal reaction process to obtain the initial electrode.[\[41\]](#page-9-0) The final active electrode NiCo-LDH-MO/NF was derived after electrochemical activation.

X-ray diffraction (XRD) patterns were measured to identify the NiCo-PBA precursor and NiCo-LDH-MO/NF before and after activation (Figure [1b,c\)](#page-1-0). The characteristic peaks of NiCo-LDH-MO/NF at≈17.4°, 24.7°, 35.2°, and 39.6° can be assigned to NiCo-PBA (PDF#01-089-3738), which indicates that the precursor catalyst is loaded onto NF after the hydrothermal reaction. The strongest peaks of NiCo-LDH-MO/NF at 44.5°, 51.9°, and 76.4° are ascribed to the base nickel foam (PDF#04-0850).[\[29\]](#page-9-0) However, after undergoing electrochemical activation in the electrolytes both with and without urea, the intensity of the characteristic peaks of NiCo-PBA in the XRD patterns (Figure [1c\)](#page-1-0) decreased dramatically, indicating an in situ electrochemical conversion of NiCo-PBA.[\[29,42\]](#page-9-0) Earlier studies have shown that the doping of MoO4 <sup>2</sup><sup>−</sup> is favorable for inducing catalyst reconstruction.[\[37,43\]](#page-9-0) To confirm this, SEM images (**Figure 2**a,b) reveal that the catalyst is loaded on the surface of the nickel foam in the form of cubes

<span id="page-3-0"></span>Figure 3. XPS spectra of a) full spectrum, b) Ni 2p, c) Co 2p, and d) Mo 3d spectra of NiCo-LDH-MO/NF electrode before and after UOR and OER activation.

before activation. However, through activation, these cubes rapidly convert into a layer of protruding structure, covering the surface of the nickel foam (Figure 2c-f). This dense protruding layer exposes more internal active sites of the catalyst and contributes to enhanced reactant diffusion. As a result, the apparent color of the electrode changes from purple to black.

TEM imaging was carried out to further clarify the reconstructed microstructure and composition after activation. Highresolution TEM images show that the lattice fringe of NiCo-LDH-MO/NF possesses a d-spacing of 0.234 nm, which corresponds to the (331) plane of the NiCo-PBA phase (Figure 2g). After electrochemical activation, the d-spacings of the lattice fringes change into 0.208, 0.239, and 0.260 nm, which correspond to the (107), (104), and (012) planes of the NiCo-LDH phase (Figure 2h,i; Figure S1, Supporting Information), respectively. This suggests that the restructuring of NiCo-PBA generated NiCo-LDH after UOR and OER activation. The elemental mapping (Figure S2, Supporting Information) indicates the uniform distribution of Ni, Co, Mo, and N elements on the cubic structure before and

after activation, while Mo is present as dispersedly doped. In contrast, the distribution of N is even sparser than that of Mo after the activated reconstruction, owing to the substitution of -CNligand by -OH- in the NiCo-PBA structure.

#### 2.2. Surface Chemistry Analysis

X-ray photoelectron spectroscopy (XPS) characterization further reveals information about electrochemical reconstruction on surface elemental composition and oxidation valence states. The XPS survey scan spectrum demonstrates the presence of Ni, Co, Mo, N, O, and C elements (Figure 3a). Relative to the initial electrode, the content of N decreased significantly after activation, while the content of O increased dramatically. This further evidence that CV activation under alkaline conditions leads to a rapid reconstruction of the NiCo-LDH-MO/NF electrode, prompting the replacement of a single -CN- by two -OH- in the NiCo-PBA framework. The peaks at 855.68 and 873.16 eV

16163028, 0, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.20250435 by University Of Science, Wiley Online Library on [06(01/2005)]. See the Terms and Conditions (https://onlinelibrary.wiley.com/rems-and-conditions) on Wiley Online Library for rules of use; OA article are governed by the applicable Creative Commons Leense and Conditions (https://onlinelibrary.wiley.com/rems-and-conditions) on Wiley Online Library for rules of use; OA article are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable Creative Commons Leense are governed by the applicable C

<span id="page-4-0"></span>Figure 4. a) LSV curves and b) Tafel slope of UOR. c) LSV curves and d) Tafel slope of OER. e) LSVs of NiCo-LDH-MO/NF||Pt/C/NF for overall urea and water splitting. f) Comparison of UOR and OER performance with other recently reported catalysts at 10 and 100 mA cm<sup>-2</sup>, respectively.

of the initial electrode can be ascribed to Ni<sup>2+</sup>, whereas those at 856.81 and 875.09 eV can be attributed to Ni<sup>3+</sup> (Figure 3b).<sup>[44]</sup> The result suggests that Ni exists mainly in the form of Ni<sup>2+</sup>, and a small portion of Ni<sup>3+</sup> may be formed by the oxidation of high valence Mo during hydrothermal processes. The Co 2p spectra indicate the presence of single-component valence Co<sup>3+</sup>, matching the peaks at 781.66 and 796.75 eV (Figure 3c), respectively.<sup>[45]</sup> In addition, the Mo 3d spectra display the coexistence of Mo<sup>6+</sup> and Mo<sup>6+</sup> (4<  $\delta$  <6), where the peaks at 232.04 and 235.22 eV can be attributed to Mo<sup>6+</sup> in MoO<sub>4</sub><sup>2-</sup>, while the peaks at 230.30 and 233.53 eV can be ascribed to Mo<sup>6+</sup> (Figure 3d).<sup>[46,47]</sup> The formation of Mo<sup>6+</sup> may be related to the oxidation of Ni during the hydrothermal process and the formation of oxygen vacancies (Figure S3, Supporting Information), which contributed to the enhancement of the oxidation performance.

Upon activation in alkaline solutions with/without urea, the Co 2p and Mo 3d peaks significantly shift to negative and positive binding energies (Figure 3c,d). This is due to the drastic deformation of the crystal structure caused by the reconstruction, facilitating the electron jump from Mo atoms to the vicinity of Co atoms. [48,49] This can also be collateral evidence that MoO<sub>4</sub> <sup>2-</sup> is doped on the Co site. In addition, it is noted that the valence state of Co changes from Co3+ alone to mixed oxidation states  $(Co^{3+}/Co^{2+})$ . This occurs because the  $Co^{3+}$  in  $[Co(CN)_6]^{3-}$  undergoes partial reduction to Co<sup>2+</sup> in NiCo-LDH during activation and reconstruction, while MoO<sub>4</sub><sup>2-</sup> leaching leads to the formation of oxygen vacancies.<sup>[50]</sup> When UOR activation was carried out, the content of Co<sup>3+</sup> was significantly higher than that after OER activation, indicating that the reconstituted Co2+ was oxidized again by OH- during UOR (Figure 3c). After UOR activation, the characteristic peaks of Ni<sup>2+</sup>/Ni<sup>3+</sup> shift to higher/lower binding energies by 0.06 and 0.09 eV (Figure 3b), respectively, which were not significantly different from those before activation.<sup>[51]</sup> In contrast, after OER activation, the peaks of Ni<sup>2+</sup>/ Ni<sup>3+</sup> were both shifted to low binding energies of 0.23 and 0.22 eV, respectively, suggesting an increase in the localized electron density of Ni, which may be due to OH<sup>-</sup> adsorption. This demonstrates the response of Co and Ni to the adsorption of OH<sup>-</sup> during UOR and OER, respectively. In this way, the adaptive adsorption of OH<sup>-</sup> by Ni/Co induces a dynamic change in the active sites in terms of UOR and OER competition.

#### 2.3. Electrochemical Performance of UOR and OER

The electrochemical performance of the as-prepared catalysts in both UOR and OER was tested in 1 m KOH with or without 0.33 m urea using a standard three-electrode configuration (Figure S4, Supporting Information). As depicted in Figure 4a, the NiCo-LDH-MO/NF electrode exhibits best performance for UOR, requiring only 1.27 and 1.36 V to achieve 10 and 100 mA cm $^{-2}$ , respectively, better than those of CoCo-LDH-MO/NF (1.30, 1.39 V), NiCo-PBA/NF (1.40, >1.83 V), RuO $_2$ /NF (1.37, 1.53 V) and NF (1.42, >1.83 V). This demonstrates that the doping of MoO $_4$  and the synergistic effect of Ni/Co effectively reduced the potential of the reaction and improved the UOR activity of NiCo-LDH-MO/NF.

Meanwhile, NiCo-LDH-MO/NF possesses the smallest Tafel slope value (68.8 mV dec<sup>-1</sup>) for UOR, compared to CoCo-LDH-MO/NF (95.8 mV dec<sup>-1</sup>), NiCo-PBA/NF (96.1 mV dec<sup>-1</sup>), RuO<sub>2</sub>/NF (73.5 mV dec<sup>-1</sup>) and NF (120.4 mV dec<sup>-1</sup>), confirming that the modified electrode has a faster charge transfer and

<span id="page-5-0"></span>Figure 5. a) Separated long-term stability tests of NiCo-LDH-MO/NF for UOR and OER, respectively, with a constant current density of 10 mA cm<sup>-2</sup>. b) LSV curves of NiCo-LDH-MO/NF for UOR and OER. c) Long-term UOR-to-OER continuous electrolysis test of NiCo-LDH-MO/NF in 40 mL electrolyte. d) Schematic diagram of the reactions varying with urea concentration during continuous electrolysis.

reaction kinetic speed (Figure 4b). The electrochemical impedance spectroscopy (EIS) in Figure S5 (Supporting Information) shows that NiCo-LDH-MO/NF has the smallest semicircle compared with other electrodes, indicating a significantly lower charge transfer resistance  $(R_{ct})$  and faster electron transfer rate. Furthermore, we calculated the  $C_{dl}$  to evaluate electrochemically active surface area (ECSA), of which the MoO<sub>4</sub><sup>2-</sup>-doped NiCo-LDH-MO/NF (7.29 mF cm<sup>-2</sup>) and CoCo-LDH-MO/NF (10.94 mF cm<sup>-2</sup>) have higher values than that of the unmodified NiCo-PBA/NF (3.7 mF cm<sup>-2</sup>), suggesting that the coordinated effect of doped MoO<sub>4</sub><sup>2-</sup> and intrinsic Co is significantly favorable for the growth of active sites (Figures S6 and \$7, Supporting Information).

As shown in Figure 4c, NiCo-LDH-MO/NF also carries a decent OER catalytic ability with a lower overpotential of 347 mV at a current density of 100 mA cm<sup>-2</sup>, compared to CoCo-LDH-MO/NF (367 mV), NiCo-PBA/NF (613 mV), RuO<sub>2</sub>/NF (461 mV), and NF (627 mV). The corresponding Tafel slope of 104.1 mV dec<sup>-1</sup> reflects the rapid OER rate of NiCo-LDH-MO/NF, whereas the other electrocatalysts show higher values of 117.2, 112.0, 106.3, and 136.8 mV dec<sup>-1</sup>, respectively (Figure 4d). Figure 4f and Table S1 (Supporting Information) compare the UOR and OER performance of bifunctional NiCo-LDH-MO/NF with other recently reported catalysts.

To further explore the prospect of practical application of NiCo-LDH-MO/NF, we assembled an overall water and urea splitting

<span id="page-6-0"></span>**Figure 6.** In suit Raman spectra measured in 1 m KOH, a) without and b) with 0.33 m urea.

device using NiCo-LDH-MO/NF as the anode and commercial Pt/C/NF as the cathode. According to Figure [4e,](#page-4-0) the cell voltage of urea electrolysis and water splitting is only 1.324 and 1.517 V at 10 mA cm<sup>−</sup>2, respectively, which is superior to most recently reported catalysts (Table S2, Supporting Information). Additionally, urea electrolysis is more energy efficient with a lower voltage of 193 mV than that of water electrolysis. Therefore, how to selectively perform urea electrolysis and suppress water electrolysis during long-term electrolysis is particularly important for efficient H2 production.[\[52\]](#page-9-0)

**Figure 5**[a](#page-5-0) shows the remarkable stability of NiCo-LDH-MO/NF for UOR and OER by separated chronopotentiometry tests. However, despite the ideal UOR/OER bifunctional catalytic performance of the NiCo-LDH-MO/NF electrode, competition between the two reactions is inevitably accompanied by the thermodynamic advantages of UOR over OER when treating urea-rich real solutions.[\[27\]](#page-9-0) At a current density of 100 mA cm<sup>−</sup>2, the potential required for OER is 220 mV, which is higher than that of UOR (Figure [5b\)](#page-5-0), and thus, alleviation of OER competition is crucial for energy-efficient H2 production.[\[17\]](#page-9-0) In practice, the continuous electrolysis of the urea-containing solution leads to a continuously reduced urea concentration and ultimately reaches the depletion of urea in the electrolyte. However, in most of the earlier reported works, separated UOR/OER bifunctional performance tests were carried out in an approximately constant urea concentration for UOR or a urea-free solution for OER, which is different from the potentially practical electrolysis process with varied urea concentration.

In this regard, we propose a quantitative measurement method, in which 40 mL of urea-containing solution (1 m KOH + 0.33 m urea) is subjected to a continuous UOR-to-OER test at a constant current density of 100 mA cm<sup>−</sup>2. As shown in Figure [5c,](#page-5-0) the continuous electrolytic process demonstrates an apparent 3 stage reaction: 1) UOR stage; 2) UOR-to-OER transfer stage; 3) OER stage. At the first stage, UOR dominates the reaction with lower reaction potentials due to the presence of high urea concentration. At the second stage, as the urea concentration continues to decrease in the electrolyte, the reaction potential gradually increases. With the decreasing urea concentration, since the local urea concentration around the electrode is insufficient to sustain UOR, the reaction potential rises significantly due to the presence of OER competition. However, when urea molecules are replenished around the electrode again due to diffusion, it reactivates UOR, resulting in oscillating potentials at this intermediate UOR-to-OER stage. At the third stage, OER starts to dominate the reaction with higher reaction potentials due to the depletion of urea (Figure [5d\)](#page-5-0). Liquid chromatography was used to identify the variation of urea concentrations during the above-mentioned continuous UOR-to-OER process. The corresponding test result shows that the urea concentration after 10 h reaction was essentially the same as the theoretical value (Figure S8, Table S3, Supporting Information). In addition, although the theoretical time for urea depletion is ≈20.17 h after the start of reaction, very small amounts of urea still remain in the electrolyte after 25, 33, and 45 h, which may be explained by the incomplete UOR due to the alternating UOR/OER at the oscillating potential stage.

In contrast, this potential oscillation phenomenon did not occur with a pure NF electrode in the continuous electrolysis test (Figure S9, Supporting Information), as the reaction potential range overlaps for UOR and OER. The NiCo-PBA/NF electrode without MoO4 <sup>2</sup><sup>−</sup> doping, however, rapidly underwent potential oscillation before stabilizing at a high potential (Figure S10, Supporting Information). To further demonstrate the universality of the continuous electrolysis test, we additionally tested WO4 <sup>2</sup><sup>−</sup>-doped electrodes, whose potential behavior resembled that of MoO4 <sup>2</sup><sup>−</sup>-doped electrodes due to the bifunctional capability (Figure S11, Supporting Information). These tests provide additional evidence for the adaptive selectivity of our electrodes across different reaction stages.

To investigate the differences in reconstruction in UOR and OER, respectively, in suit Raman spectroscopy was applied. As shown in **Figure 6**a, after the activation of NiCo-LDH-MO/NF

<span id="page-7-0"></span>Figure 7. a) Adsorption energy of OH<sup>-</sup> at Ni, Co, and Mo sites of MoO<sub>4</sub><sup>2-</sup>-NiCoOOH. Gibbs free energy profiles of b) OER and c) UOR over Ni and Co sites of MoO<sub>4</sub><sup>2-</sup>-NiCoOOH. d) Illustration of the reaction kinetics of MoO<sub>4</sub><sup>2-</sup>-NiCoOOH during the OER and UOR process.

in 1 M KOH, two apparent peaks  $\approx$ 470 and 553 cm<sup>-1</sup> appeared and remained as the applied potential rises from 1.1 to 1.6 V versus RHE, indicating the generation of NiOOH. [53–55] In comparison, in the Raman spectra of NiCo-LDH-MO/NF in 1 M KOH with 0.33 M urea (Figure 6b), the peaks  $\approx$ 522 and 585 cm<sup>-1</sup> appeared after activation were ascribed to Ni(OH)<sub>2</sub> and CoOOH, respectively, [56–59] while the peak at 1004 cm<sup>-1</sup> originates from C–N in urea. [60] Then, when the potential is increased to 1.3 V,

the newly emerged peaks  $\approx$ 462 and 543 cm<sup>-1</sup> were attributed to CoOOH. [43,61] This result suggests that NiOOH, originated by deprotonation of NiCo-LDH, plays a key role in OER as the true active site, whereas Ni(OH)<sub>2</sub> and CoOOH contribute to the decomposition of urea in UOR. [53,58] Furthermore, combined with the aforementioned XPS analysis, the unique peak  $\approx$ 522 cm<sup>-1</sup> for Ni(OH)<sub>2</sub> during UOR indicates that Ni is occupied by the urea molecule, which disfavors the adsorption of OH<sup>-</sup> and thus avoids

**[www.advancedsciencenews.com](http://www.advancedsciencenews.com) [www.afm-journal.de](http://www.afm-journal.de)**

16163028, 0, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202520435 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

the competition with OER. The formation of CoOOH suggests that part of the OH<sup>−</sup> groups are adsorbed to the Co(OH)2 sites and deprotonated to form \*O in CoOOH, but do not further take part in the formation of O2. This can be attributed to the lower reaction potentials of UOR, where newly adsorbed OH<sup>−</sup> prefers to take part in UOR and thus inhibits OER. Moreover, once the diffusion rate of hydroxide ions could not match the UOR reaction rate at higher potentials, the formation of Co oxyhydroxides was also impeded. Therefore, the intensities of both CoOOH peaks decreased at 1.6 V, and the intensities of the NiOOH peaks in OER decreased as well (Figure [6a,b\)](#page-6-0).

#### **2.4. Theoretical Study on the Selective Mechanism between UOR and OER**

To understand the adsorption properties and reaction competition of the bifunctional NiCo-LDH-MO/NF electrode, we further analyze the UOR and OER processes through density functional theory (DFT) calculations. The NiCoOOH (001) surface was used as a base and doped in equal proportions of Ni/Co. First, we selected Ni and Co neighboring positions to test the preferential adsorption sites of MoO4 <sup>2</sup><sup>−</sup>, respectively, and the most stable adsorption model (MoO4 <sup>2</sup><sup>−</sup>-NiCoOOH) obtained indicated that MoO4 <sup>2</sup><sup>−</sup> adsorbed on Co sites (Figure S12, Supporting Information). Then, we evaluated the Gibbs free energies of OER and UOR cycles on the structurally optimized MoO4 <sup>2</sup><sup>−</sup>-NiCoOOH surface with Ni and Co as reaction sites, respectively (Figure [7b,c;](#page-7-0) Figure S13–S16, Supporting Information). From the free energy diagrams, we can find that the energy barriers of 1.67 and 2.44 eV for the OER cycle with Ni and Co as the reaction sites, respectively, are significantly different from those of 2.11 and 1.91 eV for the UOR cycle. This suggests that Ni and Co are more active in OER and UOR, respectively, in agreement with the XPS and in situ Raman results. Then, we examined the adsorption of OH<sup>−</sup> by Co, Ni, and Mo, respectively, and the results showed that Co adsorbed OH<sup>−</sup>

more obviously (**Figure 7**[a\)](#page-7-0). Furthermore, compared to undoped NiCoOOH, MoO4 <sup>2</sup><sup>−</sup>- NiCoOOH exhibits lower reaction energy barriers for both the UOR and OER at the Co and Ni sites, respectively (Figures S17–S19, Supporting Information). Combined with the differential adsorption capacity and reactivity of Ni/Co sites for urea and OH<sup>−</sup> in MoO4 <sup>2</sup><sup>−</sup>-NiCoOOH, a rational explanation for the excellent bifunctional UOR/OER performance and selectivity of the NiCo-LDH-MO/NF electrodes after activated reconstruction is provided (Figure [7d\)](#page-7-0). The reconstruction and MoO4 <sup>2</sup><sup>−</sup> modifies the electronic structure of NiCo-LDH, facilitating charge transfer during reactions and optimizing intermediate adsorption (Figure S20, Supporting Information), thereby endowing NiCo-LDH-MO/NF with outstanding bifunctional properties. After the reconstruction of NiCo-PBA to NiCo-LDH, although Ni exhibits enhanced OER performance due to MoO4 <sup>2</sup><sup>−</sup> doping, OH<sup>−</sup> is preferentially adsorbed to the Co site in urea-containing solutions. But the high energy barrier of the OER (2.44 eV, step 3: \*O → \*OOH) leads to the formation of CoOOH only (Figure [7b\)](#page-7-0). The generated CoOOH possesses a stronger UOR activity and promotes the oxidation of urea (Figure [7c\)](#page-7-0). However, the Ni sites can only release and adsorb OH<sup>−</sup> to form NiOOH with high OER activity in the absence of urea or after urea consumption. As shown in Figure [7d,](#page-7-0) the whole oxidation system can be regarded as a "for" cyclic selection function, and each competition of urea or OH<sup>−</sup> is a selectivity judgment function. The continuous adsorption and electrolysis of OH<sup>−</sup> correspond to the iteration of the "for" loop, while the occurrence of UOR or OER based on the presence or absence of urea corresponds to the conditional judgment statement (Figure S21, Supporting Information). This switching of reaction sites is the key to realizing the self-adaptive selective switching of UOR and OER.

## **3. Conclusion**

In summary, NiCo-LDH-MO/NF electrodes with different active sites toward UOR and OER were reconstructed via hydrothermal and electrochemical activation, inspired by the "for" loop function in computer programming. The modulation of doped MoO4 <sup>2</sup><sup>−</sup> promoted the catalyst reconstruction, increased the active area of the materials, and facilitated the conductivity and electron transfer. With the synergistic effect of Ni/Co, excellent bifunctional UOR/OER catalytic performance and selectivity were achieved. The assembled NiCo-LDH-MO/NF||Pt/C/NF only requires 1.324 and 1.517 V of cell voltage for water electrolysis and urea splitting to reach a current density of 10 mA cm<sup>−</sup>2. Additionally, the electrode not only features long-term bifunctional stability but also remarkable selectivity during continuous electrolysis of a urea-containing solution. This study provides an efficient reconstruction strategy to enhance the bifunctional catalytic capability of the catalyst and presents a new method of evaluating the selectivity in response to the competition between UOR and OER during continuous electrolysis.

#### **Supporting Information**

Supporting Information is available from the Wiley Online Library or from the author.

### **Acknowledgements**

This research was supported by the National Natural Science Foundation of China (Grant Nos. 52332007 and 52227802), the Fundamental Research Funds for the Central Universities, "Zhuoyue 100" Talent Program, and 111 Center (B18002).

#### **Conflict of Interest**

The authors declare no conflict of interest.

#### **Author Contributions**

K.W. and W.C. are the co-first authors and equally contributed to this work. K.W. and B.Z. conceived the project and designed the experiments. K.W. carried out the experiments. W.C. performed DFT calculations. R.Z., H.L., S.Z., and D.W. supported the experimental ideal and participated in the data analysis. B.Z. and R.Z. supervised the project. K.W., B.Z., and W.C. drafted the manuscript and revised the manuscript. All authors discussed the results.

# <span id="page-9-0"></span>**Data Availability Statement**

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# **Keywords**

dynamic active site, urea electrolysis, urea oxidation reaction, water electrolysis

> Received: August 5, 2025 Revised: September 8, 2025 Published online:

- [1] S. Sanati, A. Morsali, H. Garcías, *J. Energy Chem.* **2023**, *87*, 540.
- [2] Y. Lei, Z. Wang, A. Bao, X. Tang, X. Huang, H. Yi, S. Zhao, T. Sun, J. Wang, F. Gao, *Chem. Eng. J.* **2023**, *453*, 139663.
- [3] N. K. Shrestha, S. A. Patil, A. S. Salunke, A. I. Inamdar, H. Im, *J. Mater. Chem.A* **2023**, *11*, 14870.
- [4] B. Zhou, Y. Shao, Z. Li, W. Yang, X. Ren, Y. Hao, *Int. J. Hydrogen Energy* **2024**, *51*, 1022.
- [5] Y. Li, W. Bao, J. Zhang, T. Ai, D. Wu, H. Wang, C. Yang, L. Feng, *J. Ind. Eng Chem.* **2023**, *121*, 510.
- [6] T. Zhou, S. N. Jagadeesan, L. Zhang, N. A. Deskins, X. Teng, *J. Phys. Chem. Lett.* **2024**, *15*, 81.
- [7] J. Kim, M. Kim, S. S. Han, K. Cho, *Adv Funct Materials* **2024**, *34*, 2315625.
- [8] M. Chen, W. D. Zhang, Q. Gong, J. Liu, X. Yang, J. Wang, X. Yan, *Chem. Commun.* **2025**, *61*, 6364.
- [9] F. O. Boakye, M. G. Sendeku, A. Kumar, S. Ajmal, K. A. Owusu, K. B. Ibrahim, M. Tabish, F. uz Zaman, M. A. Mushtaq, K. M. Alotaibi, M. Z. Ansari, G. Yasin, *Appl. Catal. B: Environ. and Energy* **2024**, *352*, 124013.
- [10] X. Gao, S. Zhang, P. Wang, M. Jaroniec, Y. Zheng, S.-Z. Qiao, *Chem. Soc. Rev.* **2024**, *53*, 1552.
- [11] M. Chen, Y. Zou, H. Zhao, W.-D. Zhang, Q. Gong, J. Liu, J. Wang, X. Yan, *Chem. Eng. J.* **2024**, *497*, 154525.
- [12] Q. Chen, X. Deng, H. He, L. Jiang, C. Liang, J. Zhang, R. Wang, J. Chen, *Chem. Eng. J.* **2024**, *484*, 149561.
- [13] Q. N. Bian, B. S. Guo, D. X. Tan, D. Zhang, W. Q. Kong, C. B. Wang, Y. Y. Feng, *ACS Appl. Mater. Interfaces* **2024**, *16*, 14742.
- [14] M. Du, Y. Ji, Y. Li, S. Liu, J. Yan, *Adv. Funct. Mater.* **2024**, *34*, 2402776.
- [15] X. Jia, H. Kang, X. Yang, Y. Li, K. Cui, X. Wu, W. Qin, G. Wu, *Appl. Catal. B* **2022**, *312*, 121389.
- [16] K. Wang, M. Pei, Y. Shuai, Y. Liu, S. Deng, Z. Zhuang, K. Sun, W. Yan, J. Zhang, *ACS Energy Lett.* **2024**, *9*, 4682.
- [17] L. Fei, H. Sun, X. Xu, Y. Li, R. Ran, W. Zhou, Z. Shao, *Chem. Eng. J.* **2023**, *471*, 144660.
- [18] H. Zhang, X. Meng, J. Zhang, Y. Huang, *ACS Sustain. Chem. Eng.* **2021**, *9*, 12584.
- [19] X. Yang, L. Kang, Z. Wei, S. Lou, F. Lei, P. Hao, J. Xie, B. Tang, *Chem. Eng. J.* **2021**, *422*, 130139.
- [20] Q. Zheng, Y. Yan, J. Zhong, S. Yan, Z. Zou, *Energy Environ. Sci.* **2024**, *17*, 748.
- [21] M. Li, X. Wu, K. Liu, Y. Zhang, X. Jiang, D. Sun, Y. Tang, K. Huang, G. Fu, *J. Energy Chem.* **2022**, *69*, 506.
- [22] M. Melchionna, P. Fornasiero, *J. Am. Chem. Soc.* **2025**, *147*, 2275.

- [23] Y. Cheng, L. Zhu, Y. Gong, *Int. J. Hydrogen Energy* **2024**, *58*, 416.
- [24] W. Jiang, X. Zhuo, T. Yu, J. Lu, Z. Zhai, H. Wen, S. Yin, *ACS Sustain. Chem. Eng.* **2024**, *12*, 998.
- [25] J. Lu, W. Jiang, R. Deng, B. Feng, S. Yin, P. Tsiakaras, *J. Colloid Interface Sci.* **2024**, *667*, 249.
- [26] R. Li, Y. Li, P. Yang, P. Ren, D. Wang, X. Lu, H. Zhang, Z. Zhang, P. Yan, J. Zhang, M. An, B. Wang, H. Liu, S. Dou, *Small* **2023**, *19*, 2302151.
- [27] X. Gao, X. Bai, P. Wang, Y. Jiao, K. Davey, Y. Zheng, S. Z. Qiao, *Nat. Commun.* **2023**, *14*, 5842.
- [28] J. Li, J. Li, T. Liu, L. Chen, Y. Li, H. Wang, X. Chen, M. Gong, Z. P. Liu, X. Yang, *Angew. Chem., Int. Ed.* **2021**, *60*, 26656.
- [29] J. Du, S. You, X. Li, B. Tang, B. Jiang, Y. Yu, Z. Cai, N. Ren, J. Zou, *ACS Appl. Mater. Interfaces* **2020**, *12*, 686.
- [30] H. Du, H. Hu, X. Wang, N. Ran, W. Chen, H. Zhu, Y. Zhou, M. Yang, J. Wang, J. Liu, *Small* **2024**, *20*, 2401053.
- [31] X. Qin, J. Luo, Z. Yu, Z. Qin, R. Jiang, S. Yao, J. Huang, Y. Hou, H. Pang, P. Sun, *J. Colloid Interface Sci.* **2023**, *652*, 23.
- [32] Y. Wang, Y. Lu, Y. Shi, J. Wang, Y. Zheng, J. Pan, C. Li, J. Cao, *Appl. Surf. Sci.* **2023**, *640*, 158391.
- [33] W. Yang, X. Yang, C. Hou, B. Li, H. Gao, J. Lin, X. Luo, *Appl. Catal. B* **2019**, *259*, 118020.
- [34] A. Navarro, F. Corbera, R. Asenjo, R. Castillo, E. L. Zapata, *J. Parallel Distrib. Comput.* **2012**, *72*, 1547.
- [35] A. Mili, S. Aharon, C. Nadkarni, *Sci. Compu. Program.* **2009**, *74*, 989.
- [36] G. Fu, X. Kang, Y. Zhang, X. Yang, L. Wang, X. Z. Fu, J. Zhang, J. L. Luo, J. Liu, *Nano-Micro Lett.* **2022**, *14*, 200.
- [37] Y. Gan, Y. Ye, X. Dai, X. Yin, Y. Cao, R. Cai, X. Zhang, *J. Colloid Interface Sci.* **2023**, *629*, 896.
- [38] J. Zhou, L. Liu, H. Ren, L. Li, W. Song, N. Li, X. Shi, C. Kou, Y. Sun, M. Han, H. Wang, J. Han, K. Liu, C. D. Momo, Y. Liu, D. Feng, W. Zhu, S. Chen, H. Jiang, Y. Liu, H. Liang, *Inorg. Chem. Front.* **2024**, *11*, 498.
- [39] L. Xu, Y. Li, M. Li, N. Yu, W. Wang, F. Wei, J. Qi, Y. Sui, L. Li, L. Zhang, *J. Energy Storage* **2024**, *77*, 109781.
- [40] H. Liu, D. Wen, B. Zhu, *J. Electroanal. Chem.* **2023**, *928*, 117082.
- [41] Y. Lin, Y. Wang, X. Li, J. Zhao, H. Liu, C. Wu, L. Yang, G. Li, Z. Qi, L. Shan, Y. Jiang, L. Song, *Small* **2024**, *20*, 2311452.
- [42] X. Fu, B. Pu, L. Pan, R. Ming, Q. Lv, X. Chen, L. Tian, *Mater. Chem. Front.* **2024**, *8*, 3272.
- [43] Y. Zhang, H. Guo, P. Yuan, K. Pang, B. Cao, X. Wu, L. Zheng, R. Song, *J. Power Sources* **2019**, *442*, 227252.
- [44] H. Rong, T. Chen, R. Shi, Y. Zhang, Z. Wang, *ACS Omega* **2018**, *3*, 5634.
- [45] H. Wang, L. Wang, Y. Jia, X. Li, H. Yang, X. Zhu, Q. Bu, Q. Liu, *Inorg. Chem.* **2023**, *62*, 11256.
- [46] M. Morales-Luna, S. A. Tomás, M. A. Arvizu, M. Pérez-González, E. Campos-Gonzalez, *J. Alloys Compd.* **2017**, *722*, 938.
- [47] S. Decanio, M. Cataldo, E. DeCanio, D. Storm, *J. Catal.* **1989**, *119*, 256.
- [48] Y. Dou, C. T. He, L. Zhang, M. Al-Mamun, H. Guo, W. Zhang, Q. Xia, J. Xu, L. Jiang, Y. Wang, P. Liu, X. M. Chen, H. Yin, H. Zhao, *Cell Rep. Phys. Sci.* **2020**, *1*, 100077.
- [49] Y. Dou, T. Liao, Z. Ma, D. Tian, Q. Liu, F. Xiao, Z. Sun, J. Ho Kim, S. Xue Dou, *Nano Energy* **2016**, *30*, 267.
- [50] Y. L. Meng, Y. Li, Z. Tan, X. Chen, L. L. Wu, L. W. Ji, Q.-S. Wang, X.-Z. Song, S. Song, *Energy Fuels* **2021**, *35*, 2775.
- [51] P. Guo, S. Cao, W. Huang, X. Lu, W. Chen, Y. Zhang, Y. Wang, X. Xin, R. Zou, S. Liu, X. Li, *Adv. Mater.* **2024**, *36*, 2311766.
- [52] S. Hu, H. Wu, C. Feng, Y. Ding, *Int. J. Hydrogen Energy* **2020**, *45*, 21040.
- [53] Z. Zheng, D. Wu, L. Chen, S. Chen, H. Wan, G. Chen, N. Zhang, X. Liu, R. Ma, *Appl. Catal. B* **2024**, *340*, 123214.

<span id="page-10-0"></span>**[www.advancedsciencenews.com](http://www.advancedsciencenews.com) [www.afm-journal.de](http://www.afm-journal.de)**

16163028, 0, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202520435 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

- [54] L. Dai, C. Fang, F. Yao, X. Zhang, X. Xu, S. Han, J. Deng, J. Zhu, J. Sun, *Appl. Surf. Sci.* **2023**, *623*, 156991.
- [55] H. Liao, G. Ni, P. Tan, Y. Liu, K. Chen, G. Wang, M. Liu, J. Pan, *Appl. Catal. B* **2022**, *317*, 121713.
- [56] P. Gao, Y. Zeng, P. Tang, Z. Wang, J. Yang, A. Hu, J. Liu, *Adv. Funct. Mater.* **2022**, *32*, 2108644.
- [57] W. Lai, L. Ge, H. Li, Y. Deng, B. Xu, B. Ouyang, E. Kan, *Int. J. Hydrogen Energy* **2021**, *46*, 26861.
- [58] L. Aguilera, Y. Leyet, A. Almeida, J. A. Moreira, J. P. de la Cruz, E. A. Milán-Garcés, R. R. Passos, L. A. Pocrifka, *J. Alloys Compd.* **2021**, *874*, 159858.
- [59] D. S. Hall, D. J. Lockwood, S. Poirier, C. Bock, B. R. MacDougall, *J. Phys. Chem. A* **2012**, *116*, 6771.
- [60] X. Yang, H. Zhang, B. Yu, Y. Liu, W. Xu, Z. Wu, *Energy Technol.* **2022**, *10*, 2101010.
- [61] Y. Lee, J. Theerthagiri, A. Min, C. J. Moon, M. Y. Choi, *EcoMat* **2023**, *5*, 12417.