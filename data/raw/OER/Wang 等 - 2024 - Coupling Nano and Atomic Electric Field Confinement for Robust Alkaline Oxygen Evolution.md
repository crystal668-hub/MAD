---
source: Wang 等 - 2024 - Coupling Nano and Atomic Electric Field Confinement for Robust Alkaline Oxygen Evolution.pdf
tool: marker
duration: 11.970s
generated: 2026-01-09T08:09:32.601691Z
---

## Zuschriften

Oxygen Evolution

Zitierweise: Angew. Chem. Int. Ed. 2024, 63, e202405438 doi.org/10.1002/anie.202405438

# **Coupling Nano and Atomic Electric Field Confinement for Robust Alkaline Oxygen Evolution**

Qiyou Wang<sup>+</sup>, Yujie Gong<sup>+</sup>, Xin Zi<sup>+</sup>, Lei Gan, Evangelina Pensa, Yuxiang Liu, Yusen Xiao, Hongmei Li, Kang Liu, Junwei Fu, Jun Liu,\* Andrei Stefancu, Chao Cai, Shanyong Chen, Shiguo Zhang, Ying-Rui Lu, Ting-Shan Chan, Chao Ma, Xueying Cao,\* Emiliano Cortés,\* and Min Liu\*

**Abstract:** The alkaline oxygen evolution reaction (OER) is a promising avenue for producing clean fuels and storing intermittent energy. However, challenges such as excessive OH- consumption and strong adsorption of oxygen-containing intermediates hinder the development of alkaline OER. In this study, we propose a cooperative strategy by leveraging both nano-scale and atomically local electric fields for alkaline OER, demonstrated through the synthesis of Mn single atom doped CoP nanoneedles (Mn SA-CoP NNs). Finite element method simulations and density functional theory calculations predict that the nano-scale local electric field enriches OH- around the catalyst surface, while the atomically local electric field improves \*O desorption. Experimental validation using in situ attenuated total reflection infrared and Raman spectroscopy confirms the effectiveness of the nano-scale and atomically electric fields. Mn SA-CoP NNs exhibit an ultra-low overpotential of 189 mV at 10 mA cm<sup>-2</sup> and stable operation over 100 hours at ~100 mA cm<sup>-2</sup> during alkaline OER. This innovative strategy provides new insights for enhancing catalyst performance in energy conversion reactions.

#### Introduction

Water electrolysis, driven by intermittent energy sources, holds promise for hydrogen production, offering a solution to both energy and environmental challenges. [1-2] The advancement of transition metal catalysts (TMC) and anion exchange membranes (AEM) has notably boosted alkaline water electrolysis systems. [3] However, progress in electrolysis technology is hindered by the slow kinetics of the oxygen evolution reaction (OER) at the anode. This is attributed to the delayed replenishment of overconsumed OH<sup>-</sup> reactants (step 1) and the sluggish transformation or desorption of oxygen-containing intermediates (mainly \*O in steps 2 to 4) on transition metal sites (\*).[4-6]

\* 
$$+4OH^{-} \rightarrow$$
 \*  $OH + 3OH^{-} + e^{-}$  (1)

\*OH + 3 OH
$$^- \rightarrow$$
 \*O + 2 OH $^- + H_2O + e^-$  (2)

\*O + 2 OH<sup>-</sup> + H<sub>2</sub>O 
$$\rightarrow$$
\* OOH + OH<sup>-</sup> + H<sub>2</sub>O + e<sup>-</sup> (3)

$$*OOH + OH^- \rightarrow H_2O + O_2 + e^- + *$$
 (4)

[\*] Q. Wang, X. Zi, Y. Liu, Y. Xiao, H. Li, K. Liu, J. Fu, C. Cai,

Hunan Joint International Research Center for Carbon Dioxide Resource Utilization, State Key Laboratory of Powder Metallurgy School of Physics, Central South University, Changsha 410083, P. R.

E-mail: minliu@csu.edu.cn

Y. Gong,+ Prof. J. Liu

Engineering and Research Center for Integrated New Energy Photovoltaics and Energy Storage Systems of Hunan Province, School of Electrical Engineering

University of South China, Hengyang 421001, Hunan, P.R. China E-mail: 2021000103@usc.edu

L. Gan, S. Chen

College of Chemistry and Chemical Engineering Central South University, Changsha 410083, Hunan, P.R. China

E. Pensa, A. Stefancu, Prof. E. Cortés Nanoinstitut München, Fakultät für Physik Ludwig-Maximilians-Universität München, München 80539, Ger-

E-mail: Emiliano.Cortes@lmu.de

S. Zhang, C. Ma College of Materials Science and Engineering Hunan University, Changsha 410082, P.R. China

Y.-R. Lu, T.-S. Chan

National Synchrotron Radiation Research Center 300092 Hsinchu, Taiwan

College of Materials Science and Engineering Linyi University, Linyi 276000, Shandong, P.R. China

E-mail: caoxueying@lyu.edu.cn

[+] These authors contributed equally to this work.

© 2024 The Authors. Angewandte Chemie published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

15213757, 2024, 28, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ange.202405438 by University Of Science, Wiley Online Library on [07/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Numerous efforts have been dedicated to addressing the challenge of the excessively low concentration of OH on the catalyst surface during the OER in alkaline environments. This challenge primarily involves two aspects: enhancing the local OH concentration in the catalyst's microenvironment and increasing OH adsorption on the active site. For instance, He et al. designed an amorphous NiFe-nanoreactor oxide to optimize surface charge distribution and increase OH concentration on the catalyst surface, resulting in a low overpotential of 228 mV at 10 mA cm <sup>2</sup> . [7] Lu et al. developed a built-in electric field between Ni FeWO4 and WO3 to regulate asymmetric interfacial electron distribution, enhancing OH adsorption and achieving a low overpotential of 235 mV at 10 mA cm <sup>2</sup> . [8]

Addressing the issue of strong adsorption or difficult transformation of \*O on TMC is equally crucial. The regulation of oxygen-affinity ability for TMC often relies on electronic structure modulation. For instance, the insertion of an adjacent Fe atom into a Co single-atom catalyst has a synergistic effect, decreasing the energy barrier of the rate-determining step (RDS), resulting in a low overpotential of 240 mV at 10 mA cm <sup>2</sup> . [9] Additionally, Mai et al. found that the coordination of 2-methylimidazole on (Fe,Co)OOH weakens the adsorption to oxygen-containing intermediates, yielding an overpotential of 230 mV at 10 mA cm <sup>2</sup> . [10] However, achieving satisfactory energy efficiency in alkaline OER remains challenging, since the usual structural strategies often struggle to simultaneously enhance OH adsorption and inhibit \*O adsorption due to the very similar adsorption behavior of OH and \*O on active sites.

In this study, we introduce a synergic strategy to establish nano-scale and atomically local electric fields by incorporating atomically dispersed Mn sites in CoP nanoneedles. This strategy aims to enrich OH concentration and simultaneously promote \*O desorption. Theoretical predictions, using Finite Element Method (FEM) simulations and Density Functional Theory (DFT) calculations, suggest that the nano-scale local electric field enhances OH concentration around the catalyst's surface, while the atomically local electric field facilitates \*O desorption. Experimental validation involves the preparation of Mn single-atom-doped CoP nanoneedles (Mn SA-CoP NNs) through a scalable method combining wet chemistry and vapor reduction. In situ attenuated total reflection infrared (ATR-IR) and Raman spectroscopy confirm the effectiveness of the nano-scale and atomically local electric fields in enriching OH and promoting \*O desorption, respectively. Consequently, Mn SA-CoP NNs exhibit an ultra-low overpotential of 189 mV at 10 mA cm <sup>2</sup> and demonstrate durability over 100 hours at around 100 mA cm <sup>2</sup> during alkaline OER, surpassing the performance of most reported catalysts to date.

#### *Results and Discussion*

To validate the impact of the nano-scale local electric field on the OER presented schematically in Figure 1a, FEM simulations were conducted.[11] Initially, we designed high-curvature CoP nanoneedles (NNs) to induce high nano-scale local electric field, due to electron migration to the charged metallic tip (Figures S1 and S2). As shown in Figure S3, the maximum electric field intensity on highcurvature CoP NNs (curvature radius of ~3.7 nm) is ~2.11×10<sup>6</sup> V m <sup>1</sup> , significantly stronger than that on lowcurvature CoP nanowires (NWs, curvature radius of ~50 nm, maximum electric field intensity of ~1.16×10<sup>5</sup> V m <sup>1</sup> ). Consequently, the concentration of OH around the surface of CoP NNs (~ 6.32 molL <sup>1</sup> ) on the anode is much higher than that around CoP NWs (~ 2.82 molL <sup>1</sup> ), attributed to the electrostatic adsorption between OH and the anode (Figures 1b and 1c).

To demonstrate that the induced atomically local electric field can enhance \*O desorption and transformation for the OER, we constructed Mn single-atom-doped CoP (Mn SA-CoP), as illustrated in Figure S4. The morphological change at the nanoscale (~100 nm) does not influence the atomical fine structure (*<*0.5 nm) therefore Mn SA-CoP NNs and NWs could be theoretically characterized by the same model. The charge density difference analysis (Figure 1d) reveals a significant electron depletion at the Mn site and electron accumulation at the Co site. This indicates that the atomically local electric field around the Mn site can supply electrons to the Co active center.[12] Additionally, the projected density of states (PDOS) (Figure 1e) shows a downshift of the *d*band center for Mn SA-CoP ( 2.30 eV) compared to that of CoP ( 2.11 eV) due to the electron contribution from the Mn atom. This change indicates that fewer electrons are available for \*O adsorption after doping Mn SA, facilitating \*O desorption on the Co active site.[13] As a

*Figure 1.* Theoretical calculation. a) Schematic diagram of nano-scale and atomically local electric field for alkaline OER. (b–c) OH concentration distributions around the surface of (b) high-curvature CoP and (c) low-curvature CoP. d) The charge density differences analysis. Color-coding: Yellow, charge density depletion; green, charge density accumulation. Blue, cobalt; red, manganese; grey, phosphorus; brown, oxygen. e) PDOS and d-band center for Co active site. f) Free energy diagram.

result, Mn SA-CoP (2.03 eV) exhibits a much lower energy barrier for \*O!\*OOH compared to pristine CoP (2.80 eV), confirming that the atomically local electric field enhances the \*O desorption and transformation (Figure 1f). These results substantiate the effectiveness of our strategy, which involves coupling nano-scale and atomically local electric fields for alkaline OER.

To validate experimentally the theoretical predictions, we utilized a scalable method that combines wet chemistry and vapor reduction to synthesize the catalysts (Figure 2a). The resulting Mn SA-CoP NNs and nanowires (Mn SA-CoP NWs) both exhibit low specific resistances (*<*0.16 Ω·m), in line with the conditions employed in the FEM simulations (Figure S5). Furthermore, scanning electron microscopy (SEM) and transmission electron microscopy (TEM) reveal that Mn SA-CoP NNs have a higher curvature (curvature radius of ~3.8 nm) than Mn SA-CoP NWs (curvature radius of ~50 nm), consistent with the theoretical model (Figures 2b–2f, S6–11). The high-resolution TEM and aberration-corrected high-angle annular dark-field scanning transmission electron microscopy (AC HAADF-STEM) images show the (011) and (211) planes of CoP (Figures 2d, S6), and the brightness of Co is similar to that of Mn atom, due to their close atomic number. The electron energy loss spectroscopy (EELS) spectra demonstrate the existence of Mn single atoms both in Mn SA-CoP NNs and Mn SA-CoP NWs (Figures 2g, S6).

We also conducted an analysis of the catalyst composition. The Mn content in Mn SA-CoP NNs and Mn SA-

*Figure 2.* Physical characterization of catalysts. a) Schematic illustration of the preparation for Mn SA-CoP NNs. (b–c) SEM images of (b) Mn SA-CoP NNs and (c) Mn SA-CoP NWs. d) AC HAADF-STEM image of Mn SA-CoP NNs. (e–f) TEM image of (e) Mn SA-CoP NNs and (f) Mn SA-CoP NWs. g) EELS spectra Mn SA-CoP NNs.

CoP NWs is 3.0 wt% and 2.8 wt%, respectively. X-ray diffraction (XRD) patterns indicate that the phase of CoP NNs and NWs remains unchanged after Mn SA doping, suggesting that Mn is effectively atomically embedded in CoP, in agreement with the energy-dispersive X-ray spectroscopy (EDS) mapping image (Figures S6 and S12).[14–15]

To gather information about the chemical structure, high-resolution X-ray photoelectron spectroscopy (XPS) measurements were performed (Figures 3 and S13). The peaks at 653.3 eV (Mn 2*p*1/2) and 642.1 eV (Mn 2*p*3/2) in Figure 3a indicate the successful doping of Mn into Mn SA-CoP NNs and NWs.[16–17] The O 1s peak of Mn SA-CoP NNs and NWs can be deconvoluted into three peaks, Mn O (531.0 eV), H O (531.6 eV), and C O (532.8 eV) (Figure 3b).[18–19] Furthermore, the positive shift of P 2*p*1/2 and 2*p*3/2 also confirms the presence of Mn P (Figure S14).[20–21] These results confirm the presence of Mn O and Mn P in the coordination environment of Mn SA. Additionally, a negative shift occurs in Co 2*p* of Mn SA-CoP NNs and NWs, indicating electron transfer from Mn atom to Co atom (Figure 3c) consistent with the theoretical prediction.[22–23]

To further confirm the structure of Mn SA-CoP, X-ray absorption spectra (XAS) were recorded. The Mn K-edge X-ray absorption near-edge structure (XANES) spectra of Mn SA-CoP NNs and NWs are located between those of Mn foil and MnO2 references, indicating that Mn is in an oxidation state between 0 and 4 (Figure 3d).[24] The Fourier-transformed extended X-ray absorption fine structure (EXAFS) spectra reveal the atomically dispersed states of the Mn atom and the absence of Mn Mn bonds in Mn SA-CoP NNs and NWs (Figure 3e).[25] The calculated P and O coordination numbers with Mn atoms are ~1 and ~5 in Mn SA-CoP NNs and NWs, respectively (Table S1), consistent with the models of the DFT calculations. Further, high-resolution wavelet transforms (WT) EXAFS plots in K space further verify the configuration of Mn single atoms in Mn SA-CoP NNs and NWs (Figures 3f and

*Figure 3.* Chemical structure characterization of catalysts. a-c) Highresolution XPS of (a) Mn 2*p*, (b) O 1s, and (c) Co 2*p.* d) Mn K-edge of catalysts. e) k3 weighted Fourier transform spectra from EXAFS of catalysts. f) WT-EXAFS plot for Mn SA-CoP NNs and Mn foil.

S15).[26] These results demonstrate that Mn SA-CoP NNs and NWs have common fine chemical structure despite the different morphology.

To assess the alkaline OER performance of catalysts, electrochemical tests were conducted. As shown in Figures 4a and S16, Mn SA-CoP NNs exhibit much smaller overpotentials (189 mV at 10 mA cm <sup>2</sup> and 258 mV at 100 mA cm <sup>2</sup> ) than those of Mn SA-CoP NWs (287 mV at 10 mA cm <sup>2</sup> and 370 mV at 100 mA cm <sup>2</sup> ) and CoP NNs (259 mV at 10 mA cm <sup>2</sup> and 350 mV at 100 mA cm <sup>2</sup> ). Moreover, the current density was normalized to eliminate the effect of electrochemical double-layer capacitance (Cdl, Figure S17), further verifying the effectiveness of our strategy for alkaline OER.

To explore the kinetics of alkaline OER, Tafel slope and electrochemical impedance spectra were conducted. Figure 4b shows that Mn SA-CoP NNs exhibit the smallest Tafel slope value (69.4 mVdec <sup>1</sup> ) among the examined catalysts, surpassing the values observed for CoP NNs

*Figure 4.* Electrochemical OER performances. a) OER polarization curves with a scan rate of 2 mVs <sup>1</sup> in 1.0 mol L <sup>1</sup> KOH solution. b) Tafel plots originated from the corresponding polarization curves. c) Comparison of performance for Co/Mn-based catalysts or transition metal phosphide catalysts at a current density of 10 mAcm <sup>2</sup> for OER. d–e) In situ ATR-IR spectra of (d) Mn SA-CoP NNs and (e) Mn SA-CoP NWs. f–g) In situ Raman spectra of (f) Mn SA-CoP NNs and (g) CoP NNs. h) Stability test for Mn SA-CoP NNs at 1.50 V vs. RHE in 1.0 mol L <sup>1</sup> KOH solution.

(71.4 mVdec <sup>1</sup> ), Mn SA-CoP NWs (73.3 mVdec <sup>1</sup> ), and CoP NWs (94.9 mVdec <sup>1</sup> ). This observation indicates that the OER is facilitated, due to OH adsorption and the transformation of \*O to \*OOH. Moreover, as shown in Figure S18, the charge transfer resistance (*R*ct) of Mn SA-CoP NNs (80.9 Ω) is much smaller than that of Mn SA-CoP NWs (314.3 Ω) and CoP NNs (164.2 Ω), highlighting the superior charge transfer ability of Mn-CoP NNs for accelerating the transformation of OH and \*O during alkaline OER. As a result, the Mn SA-CoP NNs electrocatalyst outperforms other recently developed OER catalysts (Figure 4c and Table S2).

To understand further the evolution of intermediates, in situ ATR-IR was employed (Figure S19). As the voltage becomes more positive, the O H vibration of OH at 3200–3400 cm <sup>1</sup> increases in intensity, mainly due to the electrostatic adsorption of OH on the anode and the increased local concentration of OH (Figures 4d– e).[27–28] Most noticeably, the increase of the OH vibration intensity on Mn SA-CoP NNs is higher than that on Mn SA-CoP NWs, indicating the stronger enriching effect of the nano-scale local electric field induced by NNs. To further highlight the higher local OH concentration on Mn SA-CoP NNs, we indirectly measured the local OH concentration by determining the local pH of the solution (Figure S20).[29–30] The concentration of OH around Mn SA-CoP NNs (5.4 molL <sup>1</sup> ) is much higher than that around Mn SA-CoP NWs (3.0 molL <sup>1</sup> ), proving that the local electric field facilitates OH diffusion from the bulk electrolyte to the surface of the electrode (Figure S21). Figures 4f–g show the in situ Raman spectra of Mn SA-CoP NNs and CoP NNs. Both show the characteristic peaks of CoP, located at 492 and 687 cm <sup>1</sup> . [31–32] The peak of Co-OOH (~594 cm <sup>1</sup> ) for Mn SA-CoP NNs increases in intensity at ~1.30 V, much earlier than for CoP NNs (~1.46 V), which indicates that the doped Mn atom facilitates the transformation from \*O to \*OOH.[32–34] In addition, the Mn SA-CoP NNs display long-time durability over 100 h at around 100 mA cm <sup>2</sup> and maintain a robust morphology after the test (Figures 4h, S22–25). Furthermore, the Membrane Electrode Assembly (MEA) test shows that the Mn SA-CoP NNsj jMn SA-CoP NNs couple possesses a small cell voltage (1.89 V) at 500 mA cm <sup>2</sup> for water-splitting performance and a high stability at 500 mA cm <sup>2</sup> after 50 h (Figure S26). The nearly 100% faradaic efficiency of H2 and O2 production demonstrates that almost all electrons contribute to the desired water splitting during electrocatalysis representing a favorable prospect in industrial applications (Figure S27).

#### *Conclusion*

In summary, we have presented a strategy involving the coupling of nano-scale and atomically local electric fields for alkaline OER. FEM simulations and DFT calculations were initially employed to predict the nano-scale local electric field for enriching the OH concentration around

15213757, 2024, 28, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ange.202405438 by University Of Science, Wiley Online Library on [07/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

*Angewandte*

the catalyst's surface and the atomically local electric field for facilitating \*O desorption. Subsequently, we prepared the target catalysts using a scalable approach. In situ ATR-IR and Raman spectroscopy further confirmed the significant abilities of nano-scale and local electric fields to enrich OH and facilitate \*O desorption, respectively. Consequently, Mn SA-CoP NNs exhibit a low overpotential of 189 mV at 10 mA cm <sup>2</sup> and stability over 100 hours at around 100 mA cm <sup>2</sup> during alkaline OER, representing a promising application prospect. Furthermore, besides the excellent electrocatalytic properties, the developed Mn SA-CoP NNs could also be coupled to plasmonic nanostructures which sustain localized surface plasmon resonances upon broadband light excitation. This opens the possibility of using sunlight to drive the OER, contributing to the development of sustainable solar-tochemical energy conversion catalysts. The plasmonic EM near-fields could further enhance the local OH concentration and the desorption or transformation of \*O, increasing the OER efficiency. The ability of the NNs to shape the local electric field, and thus the local ionic concentration at the interface, can be used to control the selectivity of plasmon-driven chemical reactions[35–36] while the single-atom sites could be used to tune the adsorption energy of the target analyte,[37] highlighting the inherent flexibility of the developed catalyst for both photo- and electro-catalysis.[38]

### *Acknowledgements*

We gratefully thank the Natural Science Foundation of China (Grant No. 22002189, 22376222 52372253, 52202125), Science and Technology Innovation Program of Hunan Province (Grant No. 2023RC1012), Central South University Research Pro-gramme of Advanced Interdisciplinary Studies (Grant No. 2023QYJC012), Central South University Innovation-Driven Research Programme (Grant No. 2023CXQD042). We acknowledge funding and support from the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany's Excellence Strategy—EXC 2089/1—390776260, the Bavarian program Solar Technologies Go Hybrid (SolTech), the Center for Nano-Science (CeNS) and the European Commission through the ERC Starting Grant CATALIGHT (802989). A.S. acknowledges support from the Alexander von Humboldt foundation. We are grateful for resources from the High-Performance Computing Center of Central South University. We would like to acknowledge the help from the TLS 01C1 and TLS 16A1 beam lines of National Synchrotron Radiation Research Center (NSRRC, Taiwan) for various synchrotron-based measurements. Open Access funding enabled and organized by Projekt DEAL.

### *Conflict of Interest*

The authors declare no conflict of interest.

**Keywords:** Nanoneedles **·** single atom **·** local electric field **·** alkaline oxygen evolution

- [1] S. J. Zhang, Y. Zhao, W. Zhao, J. Wang, Y. Hu, C. Huang, X. Zou, Y. Liu, D. Zhang, X. Lu, H. Fan, Y. Hou, *Angew. Chem. Int. Ed.* **2023**, *62*, e202314303.
- [2] T. Shen, X. Huang, S. Xi, W. Li, S. Sun, Y. Hou, *J. [Energy](https://doi.org/10.1016/j.jechem.2021.10.027) Chem.* **2022**, *68*, [184–194.](https://doi.org/10.1016/j.jechem.2021.10.027)
- [3] J. Wang, Y. Gao, H. Kong, J. Kim, S. Choi, F. Ciucci, Y. Hao, S. Yang, Z. Shao, J. Lim, *Chem. Soc. Rev.* **2020**, *49*, [9154–9196.](https://doi.org/10.1039/D0CS00575D)
- [4] C. J. Huang, H. M. Xu, T. Y. Shuai, Q. N. Zhan, Z. J. Zhang, G. R. Li, *Appl. Catal. B* **2023**, *325*, [122313.](https://doi.org/10.1016/j.apcatb.2022.122313)
- [5] Z. Y. Yu, Y. Duan, X. Y. Feng, X. Yu, M.-R. Gao, S. H. Yu, *Adv. Mater.* **2021**, *33*, 2007100.
- [6] P. Liu, B. Chen, C. Liang, W. Yao, Y. Cui, S. Hu, P. Zou, H. Zhang, H. J. Fan, C. Yang, *Adv. Mater.* **2021**, *33*, 2007377.
- [7] X. Li, H. Zhang, Q. Hu, W. Zhou, J. Shao, X. Jiang, C. Feng, H. Yang, C. He, *Angew. Chem. Int. Ed.* **2023**, *62*, e202300478.
- [8] S. Zhao, Y. Wang, Y. Hao, L. Yin, C. H. Kuo, H. Y. Chen, L. Li, S. Peng, *Adv. Mater.* **2023**, 2308925.
- [9] C. Chen, M. Sun, F. Zhang, H. Li, M. Sun, P. Fang, T. Song, W. Chen, J. Dong, B. Rosen, P. Chen, B. Huang, Y. Li, *[Energy](https://doi.org/10.1039/D2EE03930C) Environ. Sci.* **2023**, *16*, [1685–1696](https://doi.org/10.1039/D2EE03930C).
- [10] W. Huang, J. Li, X. Liao, R. Lu, C. Ling, X. Liu, J. Meng, L. Qu, M. Lin, X. Hong, X. Zhou, S. Liu, Y. Zhao, L. Zhou, L. Mai, *Adv. Mater.* **2022**, *34*, 2200270.
- [11] Q. Wang, Y. Gong, Y. Tan, X. Zi, R. Abazari, H. Li, C. Cai, K. Liu, J. Fu, S. Chen, T. Luo, S. Zhang, W. Li, Y. Sheng, J. Liu, M. Liu, *Chin. J. Catal.* **2023**, *54*, [229–237](https://doi.org/10.1016/S1872-2067(23)64532-2).
- [12] C. Cai, K. Liu, L. Zhang, F. Li, Y. Tan, P. Li, Y. Wang, M. Wang, Z. Feng, D. Motta Meira, W. Qu, A. Stefancu, W. Li, H. Li, J. Fu, H. Wang, D. Zhang, E. Cortés, M. Liu, *Angew. Chem. Int. Ed.* **2023**, *62*, e202300873.
- [13] S. Jiao, X. Fu, H. Huang, *Adv. Funct. Mater.* **2022**, *32*, 2107651.
- [14] H. Song, M. Wu, Z. Tang, J. S. Tse, B. Yang, S. Lu, *[Angew.](https://doi.org/10.1002/anie.202017102) Chem. Int. Ed.* **2021**, *60*, [7234–7244](https://doi.org/10.1002/anie.202017102).
- [15] H. Chen, S. Chen, Z. Zhang, L. Sheng, J. Zhao, W. Fu, S. Xi, R. Si, L. Wang, M. Fan, B. Yang, *ACS Catal.* **2022**, *12*, [13482–](https://doi.org/10.1021/acscatal.2c03189) [13491](https://doi.org/10.1021/acscatal.2c03189).
- [16] C. Walter, P. W. Menezes, S. Orthmann, J. Schuch, P. Connor, B. Kaiser, M. Lerch, M. Driess, *[Angew.](https://doi.org/10.1002/anie.201710460) Chem. Int. Ed.* **2018**, *57*, [698–702](https://doi.org/10.1002/anie.201710460).
- [17] K. L. Pickrahn, S. W. Park, Y. Gorlin, H. B. R. Lee, T. F. Jaramillo, S. F. Bent, *Adv. Energy Mater.* **2012**, *2*, [1269–1277](https://doi.org/10.1002/aenm.201200230).
- [18] W. Li, J. Liu, P. Guo, H. Li, B. Fei, Y. Guo, H. Pan, D. Sun, F. Fang, R. Wu, *Adv. Energy Mater.* **2021**, *11*, 2102134.
- [19] Z. Wang, P. Cai, Q. Chen, X. Yin, K. Chen, Z. Lu, Z. Wen, *[J.](https://doi.org/10.1016/j.jcis.2023.01.076) Colloid [Interface](https://doi.org/10.1016/j.jcis.2023.01.076) Sci.* **2023**, *636*, 610–617.
- [20] J. Wang, R. Gao, L. Zheng, Z. Chen, Z. Wu, L. Sun, Z. Hu, X. Liu, *ACS Catal.* **2018**, *8*, [8953–8960.](https://doi.org/10.1021/acscatal.8b01023)
- [21] L. M. Cao, Y. W. Hu, S. F. Tang, A. Iljin, J. W. Wang, Z. M. Zhang, T. B. Lu, *Adv. Sci.* **2018**, *5*, 1800949.
- [22] J. Yu, Y. Zhong, X. Wu, J. Sunarso, M. Ni, W. Zhou, Z. Shao, *Adv. Sci.* **2018**, *5*, 1800514.
- [23] C. Guan, W. Xiao, H. Wu, X. Liu, W. Zang, H. Zhang, J. Ding, Y. P. Feng, S. J. Pennycook, J. Wang, *Nano [Energy](https://doi.org/10.1016/j.nanoen.2018.03.034)* **2018**, *48*, [73–80](https://doi.org/10.1016/j.nanoen.2018.03.034).
- [24] Y. Zhu, W. Wang, J. Cheng, Y. Qu, Y. Dai, M. Liu, J. Yu, C. Wang, H. Wang, S. Wang, C. Zhao, Y. Wu, Y. Liu, *[Angew.](https://doi.org/10.1002/anie.202017152) Chem. Int. Ed.* **2021**, *60*, [9480–9488](https://doi.org/10.1002/anie.202017152).
- [25] J. Feng, H. Gao, L. Zheng, Z. Chen, S. Zeng, C. Jiang, H. Dong, L. Liu, S. Zhang, X. Zhang, *Nat. Commun.* **2020**, *11*, 4341.
- [26] Z. Guo, Y. Xie, J. Xiao, Z. J. Zhao, Y. Wang, Z. Xu, Y. Zhang, L. Yin, H. Cao, J. Gong, *J. Am. Chem. Soc.* **2019**, *141*, [12005–](https://doi.org/10.1021/jacs.9b04569) [12010](https://doi.org/10.1021/jacs.9b04569).

15213757, 2024, 28, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ange.202405438 by University Of Science, Wiley Online Library on [07/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

- [27] Y. Katayama, T. Okanishi, H. Muroyama, T. Matsui, K. Eguchi, *ACS Catal.* **2016**, *6*, [2026–2034.](https://doi.org/10.1021/acscatal.6b00108)
- [28] K. Koichumanova, K. B. Sai Sankar Gupta, L. Lefferts, B. L. Mojet, K. Seshan, *Phys. Chem. Chem. Phys.* **2015**, *17*, [23795–](https://doi.org/10.1039/C5CP02168E) [23804.](https://doi.org/10.1039/C5CP02168E)
- [29] X. Zi, Y. Zhou, L. Zhu, Q. Chen, Y. Tan, X. Wang, M. Sayed, E. Pensa, R. A. Geioushy, K. Liu, J. Fu, E. Cortés, M. Liu, *Angew. Chem. Int. Ed.* **2023**, *62*, e202309351.
- [30] F. Xue, C. Zhang, H. Peng, F. Liu, X. Yan, Q. Yao, Z. Hu, T. S. Chan, M. Liu, J. Zhang, Y. Xu, X. Huang, *[Nano](https://doi.org/10.1021/acs.nanolett.3c03845) Lett.* **2023**, *23*, [11827–11834](https://doi.org/10.1021/acs.nanolett.3c03845).
- [31] E. S. Duran-Uribe, A. Sepúlveda-Escribano, E. V. Ramos-Fernandez, *Chem. Eng. J.* **2023**, *474*, [145897.](https://doi.org/10.1016/j.cej.2023.145897)
- [32] G. Yuan, J. Bai, L. Zhang, X. Chen, L. Ren, *Appl. [Catal.](https://doi.org/10.1016/j.apcatb.2020.119693) B* **2021**, *284*, [119693](https://doi.org/10.1016/j.apcatb.2020.119693).
- [33] L. Huang, H. Shin, W. A. Goddard, J. Wang, *Nano [Energy](https://doi.org/10.1016/j.nanoen.2020.104885)* **2020**, *75*, [104885](https://doi.org/10.1016/j.nanoen.2020.104885).
- [34] H. Chen, J. Chen, H. He, X. Chen, C. Jia, D. Chen, J. Liang, D. Yu, X. Yao, L. Qin, Y. Huang, Z. Wen, *Appl. [Catal.](https://doi.org/10.1016/j.apcatb.2022.122187) B* **2023**, *323*, [122187.](https://doi.org/10.1016/j.apcatb.2022.122187)

- [35] A. Stefancu, J. Gargiulo, G. Laufersky, B. Auguié, V. Chiş, E. C. Le Ru, M. Liu, N. Leopold, E. Cortés, *ACS Nano* **2023**, *17*(3), 3119–3127.
- [36] A. Stefancu, L. Nan, L. Zhu, V. Chiş, I. Bald, M. Liu, N. Leopold, S. A. Maier, E. Cortes, *Adv. Opt. Mater.* **2022**, *10*, 2200397.
- [37] J. Fojt, T. P. Rossi, M. Kuisma, P. Erhart, *Nano Lett.* **2022**, *22*(21), 8786–8792.
- [38] Y. Zeng, C. Li, B. Li, J. Liang, M. J. Zachman, D. A. Cullen, R. P. Hermann, E. E. Alp, B. Lavina, S. Karakalos, M. Lucero, B. Zhang, M. Wang, Z. Feng, G. Wang, J. Xie, D. J. Myers, J. P. Dodelet, G. Wu, *Nat. Catal.* **2023**, *6*, [1215–1227](https://doi.org/10.1038/s41929-023-01062-8).

Manuscript received: March 20, 2024 Accepted manuscript online: April 29, 2024 Version of record online: June 12, 2024