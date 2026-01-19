---
source: Yang 等 - 2022 - Coordination Engineering of Single‐Atom Iron Catalysts for Oxygen Evolution Reaction.pdf
tool: marker
duration: 114.512s
generated: 2026-01-09T08:22:44.435722Z
---

www.chemcatchem.org

# **Coordination Engineering of Single-Atom Iron Catalysts for Oxygen Evolution Reaction**

Weijie Yang,[a, b] Binghui Zhou,[a, b] Zhenhe Jia,[a, b] Chongchong Wu,[c] Li Wei,[d] Zhengyang Gao,\*[a, b] and [Hao](http://orcid.org/0000-0002-7577-1366) Li\*[e]

Developing highly active oxygen evolution reaction (OER) catalyst is essential to improve the performance of a water electrolyzer, where single-atom catalysts (SACs) have shown promising performance in recent years. However, while SACs with various coordination environment have become experimentally feasible, knowledge about the structure-performance relationship of SACs is still very limited, especially for the emerging multiple *p*-block element-doped SACs substrates. Herein, by adjusting the coordination environment of singleatom iron catalysts, 122 SACs with various substrates were designed for comprehensive analysis. Through spin-polarized density functional theory calculations with van der Waals corrections, 52 stable single-atom iron catalysts were identified.

To analyze their OER performance, an OER volcano activity model was derived to predict their performance as the function of O\* and HO\* binding free energies. Interestingly, a Fe1B1C1N2 pen structure was found to have an outstanding OER activity (with a theoretical overpotential of 0.40 V *vs.* reversible hydrogen electrode) due to its unique adsorption mode that strengthens HO-bonding by forming the Fe OH B bond. Based on these results, the OER performance of 26 TM1/B1C1N2-pen (TM=Ti Zn, Zr Cd, and Hf Au) SACs were determined based on this unique coordination environment by B-doping. Most importantly, this study shows that the OER performance of SACs can be significantly improved by tuning the coordination environment of an active metal center.

# **Introduction**

The development of water-splitting technology provides a new avenue toward the efficient and clean utilization of renewable energy.[1] In a water-splitting process through water electrocatalysis, oxygen evolution reaction (OER) takes place on the anode of a water electrolyzer. However, compared to the cathode reaction (*i. e.*, hydrogen evolution reaction, HER), OER on the anode is much more sluggish, lowering the overall water-splitting efficiency. Therefore, developing promising OER catalysts is particularly important but challenging for industry and society.

Designing promising oxygen electrocatalysts is one of the keys to realizing a sustainable future. Among many emerging catalysts reported to date, single-atom catalysts (SACs) have attracted board attentions in the catalyst community due to their high catalytic activity, selectivity, and near-100% atom utilization for many reactions.[2] Because of the large specific surface area and unique physicochemical properties of graphene, graphene-based SACs consisting of a metal active center coordinating with a defective graphene substrate have been widely studied.[3] Recently, a number of studies showed that the catalytic activity and stability of SACs can be further improved by introducing defects and heteroatoms (*e.g.*, *p*-block elements) into graphene.[3e] Among them, the most common SACs structure is to form M1Nx by introducing N to coordinate with a metal atom, where M is the active metal center.[4] The most widely studied active center of SACs include transition metals (TM) such as Fe, Co, Ni, and Cu. Among them, Fe was widely considered for SACs due to its high earth-abundance and low cost. Fe1N4 catalysts have shown excellent performance in both thermal catalysis and electrocatalysis.[5] However, while they usually have high oxygen reduction reaction (ORR) performance,[6] the activities of OER (which can be approximately regarded as its reverse reaction) of Fe1Nx catalysts are usually not ideal. Doping of *p*-block elements (*e.g.*, B, O, P, and S) will change the electronic properties of the metal atoms in the catalyst. It reported that B heteroatoms have great potential to redistribute the inhomogeneous spin and charge densities caused by the coordination of metal and N atoms, making the metal center more favorable for intermediate adsorption, thereby enhancing the catalytic activity.[7] P has a weaker electro-

- [a] *Prof. W. Yang, B. Zhou, Z. Jia, Prof. Z. Gao Department of Power Engineering School of Energy, Power and Mechanical Engineering North China Electric Power University 071003 Baoding (P. R. China) E-mail: gaozhyan@163.com*
- [b] *Prof. W. Yang, B. Zhou, Z. Jia, Prof. Z. Gao Hebei Key Laboratory of Low Carbon and High Efficiency Power Generation Technology North China Electric Power University 071003 Baoding (P. R. China)*
- [c] *Dr. C. Wu CNOOC Institute of Chemicals and Advanced Materials Beijing 102200 (P. R. China)*
- [d] *Dr. L. Wei School of Chemical and Biomolecule Engineering The University of Sydney 2006 Darlington, NSW (Australia)*
- [e] *Prof. H. Li Advanced Institute for Materials Research (WPI-AIMR) Tohoku University 980-8577 Sendai (Japan) E-mail: li.hao.b8@tohoku.ac.jp*
- Supporting information for this article is available on the WWW under <https://doi.org/10.1002/cctc.202201016>

negativity and a larger atomic radius, which leads to a richer electron density concentrated on the metal sites in the M<sub>1</sub>P<sub>x</sub> configuration compared to the  $M_1N_x$  configuration. In some cases, the P ligands may even behave as electron transfer channels, transferring electrons from the support to the metal, further promoting the accumulation of electrons at individual metal sites.<sup>[8]</sup> When Fe<sub>1</sub>N<sub>x</sub>C<sub>y</sub> is doped with S element, the relatively large S atomic radius makes it possible to induce defects on the carbon substrate, while the low S electronegativity (N(3.04) > S(2.58) > C(2.55) ) will change the electronic structure of the Fe-N active center. [9] By tuning the coordination environment of SACs, it is beneficial to adjust the adsorption strength of the metal atoms in the catalyst center to the intermediates during the OER process, thereby improving the catalyst activity. Overall, due to the difference between the atomic radius and electronegativity among p-block elements, their doping in single-atom iron catalysts leads to the redistribution of charges around the Fe atoms in the center of the catalysts, which in turn flexibly tunes the adsorption of intermediates free energy to adjust the catalyst activity. Therefore, tuning the coordination environment in SACs is of great significance to improve OER catalytic activity.

Theoretical studies on doping SACs with p-block elements other than N are continuously being reported. Tang et al.[10] showed through DFT studies that the coordination of B<sub>x</sub>N<sub>y</sub> atoms can promote the charge transfer between the catalyst center Co atom and the neighboring carbon atoms, adjust their sensitivity to the reaction gas, and thus improve the catalytic oxidation activity of the catalyst for CO/NO. Through DFT calculations, Wang et al.[11] showed that the O and N bicomponent assignments can tune the d-band center of molybdenum, thereby optimizing its binding ability to the reaction intermediates (O\*, HO\*, and HOO\*), thereby accelerating the entire ORR process. Ren et al.[12] theoretically demonstrated that by rationally tuning the coordination B atoms in single-atom iron catalysts, the d-band center and magnetic moment of the central Fe atoms can be controlled, thereby improving CO<sub>2</sub> reduction performance.

The successful preparation of SACs by doping graphene with p-block elements has also been reported in very recent years. Tang et al.[13] prepared a graphene-based single-atom molybdenum catalyst co-doped with O and S, and found that this type of SAC can significantly promote ORR. Li et al.[14] prepared N and O co-coordinated graphene-based single-atom platinum catalysts with high electrocatalytic HER activities. Using a cold-plasma technique, they adjusted the ratio of N and O coordination in the catalyst by changing the gas and synthesis duration. Zhang et al.[15] prepared N and S cocoordinated single-atom iron catalysts, which exhibited high activities in oxygen electrocatalysis compared to many conventional catalysts. Yuan et al.[16] realized the preparation of N and P co-doped single-atom iron catalysts with good ORR performance. Hou et al.[17] synthesized a graphene-based single-atom nickel catalyst co-coordinated with N and S and exhibited excellent OER activity and durability at 10 mA/cm<sup>2</sup>. Chen et al.[18] introduced N, S, and P into graphene-based single-atom iron catalysts, and found that the Tafel slope of the heteroatom-doped catalyst could reach 51 mV/dec, with a significantly improved ORR performance. Shi et al. [19] synthesized B, N co-doped porous carbon nanotube-supported single-atom molybdenum catalyst by B and N co-doping (Mo/BCN); they found that the Mo/BCN exhibited high catalytic activity for the reduction of  $N_2$  to  $NH_3$ , with a Faradaic efficiency of 13.27% in 0.1 M KOH. From the above reports, the doping of B, O, P, S, and other p-block elements into SACs has become experimentally feasible along with advanced synthetic and characterization strategies. After doping of p-block elements in SACs, the catalytic performance will change significantly. However, systematic studies on the regulation of OER activity of single-atom iron catalysts by the doping of p-block element (e.g., B, N, O, P, and S) are rarely reported.

Motivated by the above landscape, herein, we aim to analyze the O\* and HO\* adsorption properties of single-atom iron catalysts with various coordination environment and study how their OER performance would change. We constructed 122 single atom iron catalysts for spin-polarized density functional theory calculations with van der Waals corrections (DFT-D3). First, 122 single-atom iron catalysts based on different coordination environments with B, N, O, P, and S were designed. Second, 52 stable configurations were identified by stability analysis. Third, by analyzing the adsorption free energies of these structurally stable catalysts for O\* and HO\*, we found that a typical Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen structure has special adsorption properties for HO\* and excellent OER catalytic activity based on an OER volcano activity model. Finally, we extensively analyzed the adsorption free energies of O\* and HO\* on the TM<sub>1</sub>/B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen catalysts composed of 26 transition metals based on the B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen configuration. This "design & screening" study by tuning the local coordination environment of single-atom iron provides important guidelines for experimental synthesis.

#### **Computational and Modeling Methods**

In this work, all DFT calculations were performed using the Vienna ab initio simulation package (VASP 5.4.4).[20] In detail, the projected enhanced wave (PAW) method was used to describe the interaction between the nucleus and valence electrons, and the Perdew-Burke-Ernzerhof (PBE) functional was used to describe the electronic exchange and correlation. [21] Spin polarization was considered to obtain the precise electron ground state energy.[22] To accurately describe the interaction between the gas and the surface, dipole corrections and DFT-D3 were both considered. [23] We constructed a  $5 \times \sqrt{3} \times 1$  (12.33×12.88×20.00 Å) graphene as the catalyst carrier and set the vacuum layer to 20.00 Å, which can effectively avoid the interaction between mirror images. The kinetic energy cutoff was set to 450 eV for all calculations. A k-point grid of  $2\times2\times1$  was selected for geometry optimizations. The force convergence criterion in geometric optimization was set to -0.02 eV/Å. At the same time, a k-point grid of  $4\times4\times1$  was used for electronic selfconsistent calculations. For the electron self-consistent field calculations, the convergence criterion was set to 10<sup>-5</sup> eV. The projected crystal orbital Hamiltonian population (pCOHP) was analyzed using the LOBSTER<sup>[24]</sup> package to study the strength between chemical bonds.

8673899,

The equation for calculating the binding energy ( $E_{\text{bind}}$ ) is defined as (Eq. 1):

$$E_{\text{bind}} = E_{\text{sur}} - E_{\text{sub}} - E_{\text{M}} \tag{1}$$

where  $E_{\text{sur}}$ ,  $E_{\text{sub}}$ , and  $E_{\text{M}}$  are the electronic energies of the catalyst, graphene substrate, and single metal atom, respectively.

The equation for calculating the formation energy ( $E_f$ ) is defined as (Eq. 2):<sup>[25]</sup>

$$E_{\rm f} = E_{\rm sur} - E_{\rm M} - m\mu_{\rm X} - n\mu_{\rm C} \tag{2}$$

where m and n respectively represent the total numbers for p-block elements and C atoms.  $\mu_{\rm X}$  (e.g.,  $\mu_{\rm B}$ ,  $\mu_{\rm Nr}$ ,  $\mu_{\rm Or}$ ,  $\mu_{\rm P}$ , and  $\mu_{\rm S}$ ) and  $\mu_{\rm C}$  denote the chemical potentials of p-block and C atoms.  $\mu_{\rm B}$ ,  $\mu_{\rm C}$ ,  $\mu_{\rm N}$ ,  $\mu_{\rm O}$ ,  $\mu_{\rm P}$ , and  $\mu_{\rm S}$  were obtained from single atoms of B<sub>36</sub>, pristine graphene, N<sub>2</sub> molecular, O<sub>2</sub> molecular, P<sub>4</sub>, and S<sub>8</sub>, respectively. [26]

The adsorption energies were calculated by the following equations (Eqs. 3–5):

$$\Delta E_{HO*} = E(HO^*) - E(^*) - (E_{H2O} - 1/2E_{H2})$$
 (3)

$$\Delta E_{O*} = E(O^*) - E(^*) - (E_{H2O} - E_{H2})$$
 (4)

$$\Delta E_{\text{HOO}*} = E(\text{HOO}^*) - E(^*) - (2E_{\text{H2O}} - 3/2E_{\text{H2}})$$
 (5)

where E(\*), E(HO\*), E(O\*), and E(HOO\*) are energies of the clean catalyst surface, and surface adsorbed by HO\*, O\*, and HOO\* species, respectively.  $E_{H2O}$  and  $E_{H2}$  are the energies of H<sub>2</sub>O and H<sub>2</sub> molecules in gas phases.

OER is a four-electron reaction process with detailed reaction steps. Under acidic conditions, the general reaction equation can be described as (Eq. 6):<sup>[27]</sup>

$$2H_2O \to O_2 + 4H^+ + 4e^- \tag{6}$$

In this paper, we analyzed the classic OER model as proposed by Nørskov et al., $^{[27-28]}$  which was also widely considered for OER studies at SACs (Eqs. 7–10): $^{[29]}$ 

$$H_2O + * \rightarrow HO^* + H^+ + e^-$$
 (7)

$$HO^* \to O^* + H^+ + e^-$$
 (8)

$$H_2O + O^* \to HOO^* + H^+ + e^-$$
 (9)

$$HOO^* \rightarrow {}^* + O_2 + H^+ + e^-$$
 (10)

where \* represents the catalytic site on the catalyst surface. HO\*, O\*, and HOO\* represent the corresponding adsorption intermediates, respectively. Based on these four elementary steps, the change of free energies  $\Delta G_i$  (i = 1, 2, 3, 4) can be expressed by the following equation (Eq. 11):<sup>[30]</sup>

$$\Delta \textit{G}_{i} = \Delta \textit{E} + \Delta \textit{ZPE} - T\Delta \textit{S} + \Delta \textit{G}_{U} + \Delta \textit{G}_{pH} \tag{11}$$

where  $\Delta E$  represents the adsorption energy of adsorbed intermediates.  $\Delta ZPE$  and  $\Delta S$  are the changes of zero-point energy and the entropy, respectively. For  $\Delta G_{\rm U}$ , U is the electrode potential.  $\Delta G_{\rm pH}$  is equal to  $k_{\rm B} {\rm TIn10} \times {\rm pH}$ . Because the potential and pH shift in the same way in a standard hydrogen electrode (SHE) scale, pH = 0 was

employed in this study, but the results are considered independent to the reaction pH.

The Gibbs free energy of each elementary step was calculated by the following equations (Eqs. 12–15):

$$\Delta G_1 = \Delta G_{\text{HO*}} - eU \tag{12}$$

$$\Delta G_2 = \Delta G_{0*} - \Delta G_{H0*} - eU \tag{13}$$

$$\Delta G_3 = \Delta G_{\text{HOO}*} - \Delta G_{\text{O}*} - eU \tag{14}$$

$$\Delta G_4 = 4.92 - \Delta G_{\text{HOO}*} - eU \tag{15}$$

where  $\Delta G_{\text{HO}^*}$ ,  $\Delta G_{\text{O}^*}$ , and  $\Delta G_{\text{HOO}^*}$  are the adsorption free energies ( $\Delta G_{\text{species}}$ ) of HO\*, O\*, and HOO\*, respectively. The  $\Delta G_{\text{species}}$  were calculated by the correction-included equations of  $\Delta G_{\text{HO}^*} = \Delta E_{\text{HO}^*} + 0.37$ ,  $\Delta G_{\text{O}^*} = \Delta E_{\text{O}^*} + 0.07$ , and  $G_{\text{HOO}^*} = \Delta E_{\text{HOO}^*} + 0.44$ . The theoretical overpotential OER ( $\eta_{\text{OER}}$ ) for a electrocatalyst was evaluated using the method described in Ref. [27] (Eq. 16):

$$\eta_{\text{OER}} = \max\{\Delta G_1, \Delta G_2, \Delta G_3, \Delta G_4\}/e - 1.23 \text{ V}$$
(16)

#### **Results and Discussion**

## Catalyst model

Two-dimensional graphene-based SACs have been extensively studied in the field of catalysis. Considering the feasibility of experimental synthesis and the stability of catalyst structure, we analyzed a graphene structure with two adjacent-carbon vacancies. Herein, we used different numbers of p-block element (e.g., B, N, O, P, and S) to replace the carbon atoms coordinated with the single-atom iron. It is worth noting that when doping two identical p-block elements, three different coordination configurations will be generated.[32] Taking the Nand O- doped systems as an example (Figure 1), it can be seen that when two nitrogen and two oxygen coordinate with the single-atom iron, there will be different configurations (Fe<sub>1</sub>N<sub>2</sub>O<sub>2</sub>pen, Fe<sub>1</sub>N<sub>2</sub>O<sub>2</sub>-hex, and Fe<sub>1</sub>N<sub>2</sub>O<sub>2</sub>-opp). Based on these, we constructed in total 122 single-atom iron catalysts by adjusting the type and number of coordinating p-block atoms. Detailed configurations of these structurally optimized catalysts are shown in Figures S1-S18.

We further investigated the stability of these 122 single-atom iron catalysts. Binding energy is an important indicator to reflect the stability of SACs, which is of great significance to evaluate the difficulty of catalyst synthesis. Therefore, we calculated the binding energies of these 122 catalysts (Figure 2 and Table S1). The number of each different *p*-block atoms doping system on the horizontal axis in the figure represents the number of catalyst configurations produced under this coordination system, and the detailed coordination configuration under each different doping system is shown in Figures S1–S18. The more negative value of a binding energy, the higher the structural stability of the catalyst is revealed. According to previous reports, the experimental and theoretical values of cohesive energy of iron clusters are -4.28 and -4.87 eV, respectively. (33) When the calculated binding energy is

2. 22. Downloaded from https://chemistry-europe.onlinelblary.wiely.com/doi/10.1002cctc.202201016 by University Of Science, Wiley Online Library on [07/01/206]. See the Terms and Conditions (https://onlinelbrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licenses

Figure 1. Schematic diagram of different coordination configurations. The iron, oxygen, and nitrogen atoms are represented in brown, red, and blue, respectively.

Figure 2. Calculated binding energies of 122 single-atom iron catalysts with different coordination environments. The dashed line represents the binding energy at -5.0 eV.

more negative than the cohesive energy of iron clusters, the catalyst is considered thermodynamically stable. Therefore, we screened out those SACs with the binding energy more negative than -5.0 eV. As a result, 52 single-atom iron catalysts with stable structures were identified.

It can be seen from Figure 2 that the SACs generally exhibit lower binding energies in the coordination environments of B and O, P and O, and S and O, which may indicate their poorer stability. Meanwhile, when the number of coordaining O increases, the binding energy gradually decreases. Therefore, the coordination of O is not conducive to the stable formation of single-atom iron catalysts, especially when the number of coordinating O is high.

The formation energy is also an important indicator for evaluating catalyst stability, and negative formation energy indicates higher stability of the structure.<sup>[34]</sup> The calculated results of the formation energies of the 52 catalysts are shown in Table 1.

# Adsorption and catalytic properties

For the 52 stable SACs, we calculated their adsorption free energies of O\* and HO\* (Table 1). Interestingly, we found that Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen has a relatively large HO\* adsorption free energy (-0.90 eV), suggesting that Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen may possess special properties for HO\* adsorption. To determine the HOO\* adsorption free energies on these SACs, we considered a linear relationship of  $\Delta G_{\text{HOO}^*} = \Delta G_{\text{HO}^*} + 3.2$ . This scaling relation is considered universal among various catalysts, [1e,27,36] which is widely used in analyzing oxygen electrocatalysis. Subsequently, we determined the overpotential ( $\eta_{\rm OER}$ ) of 52 single-atom iron catalysts for OER based on a derived classic volcano activity model (Figure 3 and Table 1). By tuning the coordination environment of single-atom iron catalysts, the OER overpotential can change from 0.4 to 2.19 V vs. reversible hydrogen electrode (RHE). It can be found that Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen locates near the theoretical optimum of the volcano model, exhibiting an outstanding catalytic activity ( $\eta_{\text{OER}} = 0.40 \text{ V}_{\text{RHE}}$ ) for OER. There-

**Table 1.** Formation energies, coordinating environment, adsorption free energies of O\* and HO\*, and the predicted OER performance of the 52 identified stable single-atom iron catalysts.

| stable single-atom iron catalysts.                                |                  |      |        |             |   |        |        |                       |                        |                                                                         |
|-------------------------------------------------------------------|------------------|------|--------|-------------|---|--------|--------|-----------------------|------------------------|-------------------------------------------------------------------------|
| Catalyst                                                          | $E_{\rm f}$ [eV] | Numb |        | dinating at |   |        |        | $\Delta G_{0^*}$ [eV] | $\Delta G_{HO^*}$ [eV] | $\eta_{\scriptscriptstyle{OER}}\left[V_{\scriptscriptstyle{RHE}} ight]$ |
|                                                                   |                  | В    | С      | N           | 0 | Р      | S      |                       |                        |                                                                         |
| Fe <sub>1</sub> B <sub>1</sub> C <sub>3</sub>                     | 1.29             | 1    | 3      | 0           | 0 | 0      | 0      | 0.73                  | 0.11                   | 1.35                                                                    |
| Fe <sub>1</sub> B <sub>2</sub> C <sub>2</sub> -hex                | 0.54             | 2    | 2      | 0           | 0 | 0      | 0      | 0.79                  | 0.20                   | 1.38                                                                    |
| $Fe_1N_3B_1$                                                      | -2.01            | 1    | 0      | 3           | 0 | 0      | 0      | -0.22                 | 0.00                   | 2.19                                                                    |
| Fe <sub>1</sub> N <sub>2</sub> B <sub>2</sub> -hex                | -1.80            | 2    | 0      | 2           | 0 | 0      | 0      | 0.59                  | -0.07                  | 1.30                                                                    |
| Fe <sub>1</sub> B <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -pen | -0.05            | 1    | 2      | 1           | 0 | 0      | 0      | 0.76                  | 0.11                   | 1.32                                                                    |
| Fe <sub>1</sub> B <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -hex | 0.20             | 1    | 2      | 1           | 0 | 0      | 0      | 0.76                  | 0.48                   | 1.69                                                                    |
| Fe <sub>1</sub> B <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -opp | 0.37             | 1    | 2      | 1           | 0 | 0      | 0      | 0.36                  | -0.05                  | 1.57                                                                    |
| Fe <sub>1</sub> B <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -pen | -0.73            | 1    | 1      | 2           | 0 | 0      | 0      | 0.67                  | -0.90                  | 0.40                                                                    |
| Fe <sub>1</sub> B <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -hex | -1.18            | 1    | 1      | 2           | 0 | 0      | 0      | -0.20                 | -0.08                  | 2.09                                                                    |
| Fe <sub>1</sub> B <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -opp | -0.91            | 1    | 1      | 2           | 0 | 0      | 0      | 0.75                  | -0.05                  | 1.16                                                                    |
| $Fe_1N_1C_1B_2$ -hex                                              | -0.50            | 2    | 1      | 1           | 0 | 0      | 0      | 0.55                  | -0.21                  | 1.21                                                                    |
| Fe <sub>1</sub> O <sub>1</sub> C <sub>3</sub>                     | 0.01             | 0    | 3      | 0           | 1 | 0      | 0      | 0.65                  | 0.03                   | 1.35                                                                    |
| Fe <sub>1</sub> O <sub>2</sub> C <sub>2</sub> -pen                | -1.41            | 0    | 2      | 0           | 2 | 0      | 0      | 0.88                  | 0.13                   | 1.22                                                                    |
| Fe <sub>1</sub> O <sub>2</sub> C <sub>2</sub> -opp                | -1.04            | 0    | 2      | 0           | 2 | 0      | 0      | 0.75                  | 0.17                   | 1.38                                                                    |
| Fe <sub>1</sub> N <sub>3</sub> O <sub>1</sub>                     | -3.38            | 0    | 0      | 3           | 1 | 0      | 0      | 1.41                  | 0.63                   | 1.19                                                                    |
| Fe <sub>1</sub> O <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -pen | -1.16            | 0    | 2      | 1           | 1 | 0      | 0      | 0.94                  | 0.24                   | 1.28                                                                    |
| $Fe_1O_1N_1C_2$ -hex                                              | -1.46            | 0    | 2      | 1           | 1 | 0      | 0      | 0.88                  | 0.07                   | 1.16                                                                    |
| $Fe_1O_1N_1C_2$ -opp                                              | -0.88            | 0    | 2      | 1           | 1 | 0      | 0      | 0.46                  | 0.07                   | 1.58                                                                    |
| $Fe_1O_1C_1N_2$ -pen                                              | -2.36            | 0    | 1      | 2           | 1 | 0      | 0      | 1.09                  | 0.31                   | 1.19                                                                    |
| $Fe_1O_1C_1N_2$ -hex                                              | -2.35            | 0    | 1      | 2           | 1 | 0      | 0      | 1.20                  | 0.46                   | 1.23                                                                    |
| $Fe_1O_1C_1N_2$ -nex                                              | -2.45            | 0    | 1      | 2           | 1 | 0      | 0      | 1.14                  | 0.44                   | 1.28                                                                    |
| $Fe_1N_1C_1N_2$ -opp<br>$Fe_1N_1C_1O_2$ -hex                      | -2.43<br>-2.43   | 0    | 1      | 1           | 2 | 0      | 0      | 0.83                  | 0.46                   | 1.59                                                                    |
| $Fe_1P_1C_3$                                                      | 1.68             | 0    | 3      | 0           | 0 | 1      | 0      | 0.23                  | -0.02                  | 1.72                                                                    |
|                                                                   | 0.71             | 0    | 2      | 0           | 0 | 2      | 0      | 1.06                  | 0.36                   | 1.28                                                                    |
| Fe <sub>1</sub> P <sub>2</sub> C <sub>2</sub> -pen                | 1.65             | 0    | 2      | 0           | 0 | 2      | 0      | 0.20                  | -0.32                  | 1.45                                                                    |
| Fe <sub>1</sub> P <sub>2</sub> C <sub>2</sub> -hex                | 0.63             | 0    |        | 0           | 0 | 3      |        |                       |                        |                                                                         |
| Fe <sub>1</sub> P <sub>3</sub> C <sub>1</sub>                     | 0.63             | 0    | 1<br>0 | 0           | 0 | 3<br>4 | 0<br>0 | 1.37                  | 0.53                   | 1.12<br>0.85                                                            |
| Fe <sub>1</sub> P <sub>4</sub>                                    | 0.53<br>1.19     | 0    | 0      | 3           | 0 | 1      | 0      | 1.53<br>1.08          | 0.42<br>0.80           | 1.69                                                                    |
| Fe <sub>1</sub> N <sub>3</sub> P <sub>1</sub>                     |                  |      |        | 2           |   | 2      |        |                       |                        |                                                                         |
| Fe <sub>1</sub> N <sub>2</sub> P <sub>2</sub> -pen                | -0.62            | 0    | 0      |             | 0 |        | 0      | 1.41                  | 0.44                   | 0.99                                                                    |
| Fe <sub>1</sub> N <sub>1</sub> P <sub>3</sub>                     | -0.08            | 0    | 0      | 1           | 0 | 3      | 0      | 1.60                  | 0.48                   | 0.84                                                                    |
| Fe <sub>1</sub> P <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -pen | 0.59             | 0    | 2      | 1           | 0 | 1      | 0      | 0.86                  | -0.25                  | 0.86                                                                    |
| Fe <sub>1</sub> P <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -hex | 0.59             | 0    | 2      | 1           | 0 | 1      | 0      | 0.92                  | 0.83                   | 1.88                                                                    |
| Fe <sub>1</sub> P <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -opp | 0.34             | 0    | 2      | 1           | 0 | 1      | 0      | 0.52                  | 0.09                   | 1.54                                                                    |
| Fe <sub>1</sub> P <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -pen | -0.14            | 0    | 1      | 2           | 0 | 1      | 0      | 0.56                  | -0.26                  | 1.15                                                                    |
| Fe <sub>1</sub> P <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -opp | -0.37            | 0    | 1      | 2           | 0 | 1      | 0      | 0.32                  | 0.21                   | 1.86                                                                    |
| Fe <sub>1</sub> N <sub>1</sub> C <sub>1</sub> P <sub>2</sub> -hex | 0.08             | 0    | 1      | 1           | 0 | 2      | 0      | 0.83                  | 0.11                   | 1.25                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> C <sub>3</sub>                     | 1.78             | 0    | 3      | 0           | 0 | 0      | 1      | 0.87                  | 0.33                   | 1.43                                                                    |
| Fe <sub>1</sub> S <sub>2</sub> C <sub>2</sub> -hex                | 2.28             | 0    | 2      | 0           | 0 | 0      | 2      | 0.83                  | 0.02                   | 1.16                                                                    |
| Fe <sub>1</sub> N <sub>3</sub> S <sub>1</sub>                     | -1.43            | 0    | 0      | 3           | 0 | 0      | 1      | 1.53                  | 0.57                   | 1.01                                                                    |
| Fe <sub>1</sub> N <sub>2</sub> S <sub>2</sub> -hex                | 0.14             | 0    | 0      | 2           | 0 | 0      | 2      | 1.38                  | 0.63                   | 1.22                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -pen | 0.63             | 0    | 2      | 1           | 0 | 0      | 1      | 1.30                  | 0.52                   | 1.19                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -hex | 0.52             | 0    | 2      | 1           | 0 | 0      | 1      | 1.21                  | 0.40                   | 1.16                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> N <sub>1</sub> C <sub>2</sub> -opp | 0.77             | 0    | 2      | 1           | 0 | 0      | 1      | 0.73                  | 0.18                   | 1.42                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -pen | -0.51            | 0    | 1      | 2           | 0 | 0      | 1      | 1.37                  | 0.73                   | 1.34                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -hex | -0.68            | 0    | 1      | 2           | 0 | 0      | 1      | 1.34                  | 0.70                   | 1.33                                                                    |
| Fe <sub>1</sub> S <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -opp | -0.46            | 0    | 1      | 2           | 0 | 0      | 1      | 1.51                  | 0.73                   | 1.19                                                                    |
| Fe <sub>1</sub> N <sub>1</sub> C <sub>1</sub> S <sub>2</sub> -hex | 1.33             | 0    | 1      | 1           | 0 | 0      | 2      | 0.96                  | 0.24                   | 1.25                                                                    |
| $Fe_1O_1B_1C_2$ -hex                                              | -0.03            | 1    | 2      | 0           | 1 | 0      | 0      | 0.56                  | -0.35                  | 1.06                                                                    |
| $Fe_1O_1B_1C_2$ -opp                                              | -0.34            | 1    | 2      | 0           | 1 | 0      | 0      | 0.69                  | 0.07                   | 1.35                                                                    |
| Fe <sub>1</sub> O <sub>1</sub> P <sub>1</sub> C <sub>2</sub> -hex | 0.36             | 0    | 2      | 0           | 1 | 1      | 0      | 0.34                  | -0.38                  | 1.25                                                                    |
| Fe <sub>1</sub> O <sub>1</sub> S <sub>1</sub> C <sub>2</sub> -pen | 0.94             | 0    | 2      | 0           | 1 | 0      | 1      | 0.22                  | -0.40                  | 1.34                                                                    |
| Fe <sub>1</sub> O <sub>1</sub> S <sub>1</sub> C <sub>2</sub> -hex | 0.59             | 0    | 2      | 0           | 1 | 0      | 1      | 0.76                  | -0.01                  | 1.21                                                                    |

fore, SACs with a  $B_1C_1N_2$ -pen coordination environment may play an essential role in improving the OER of single-atom iron, which may be due to the unique HO\* adsorption characteristics of Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen.

The calculated formation energy of  $Fe_1B_1C_1N_2$ -pen is -0.73 eV, which is a negative value confirming its structural stability. Meanwhile, ab initio molecular dynamics (AIMD) simulations<sup>[37]</sup> showed that  $Fe_1B_1C_1N_2$ -pen did not significantly change in the average bond length of the four bonds coordinated to Fe atoms within 12 ps at room temperature (298.15 K), this indicates that single-atom Fe can be stably

anchored on the graphene substrate, further revealing the stability of its structure (Figure S19).

Based on the predicted performance of  $Fe_1B_1C_1N_2$ -pen, we further analyzed the HO\* adsorption configuration of  $Fe_1B_1C_1N_2$ -pen (Figure 4a). It can be seen that the O atom of HO\* not only forms a bond with the single-atom Fe but also interacts with the coordinating B site. That is to say, the Fe—O and B—O bonds are formed in the HO\* adsorption at  $Fe_1B_1C_1N_2$ -pen. The lengths of the Fe—O and B—O bonds are 1.95 and 1.47 Å, respectively. We speculate that this co-bonding effect of Fe and B leads to a relatively large HO\* free energy, leading to a  $\Delta G_{O^*}$ — $\Delta G_{HO^*}$  value

Chemistry Europe

European Chemical Societies Publishing

**Figure 3.** Volcano activity model of  $-\eta_{OER}$  vs.  $(\Delta G_{O^*} - \Delta G_{HO^*})$  plotted with the 52 stable single-atom iron catalysts. Some typical structures are marked on the volcano.

close to the theoretical optimum for OER. To determine the adsorption of various reactants at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen, we derived the surface Pourbaix diagrams of 1H\*, 2H\*, 3H\*, 4H\*, 1O\*, 1HO\*, and 1H<sub>2</sub>O\* on the Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen surface at pH = 0 (Figure 4b). It can be seen that at OER potentials, the catalyst surface is only covered by either HO\* or O\*, which are the typical OER intermediates. This suggests that the catalyst will not be poisoned by atomic hydrogen at OER potentials.

To further analyze the HO\* adsorption mechanism, we calculated the projected density of states (PDOS) of the adsorption of HO\* at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen, as shown in Figure 4c. In the whole adsorption system, there is no obvious hybridization between Fe d-orbital and O, or between B p-orbital and O. This indicates that the binding strength of HO\* to the Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen may not be determined by orbital hybridization. Therefore, we analyzed the plotted electron density difference (EDD) maps of HO\* adsorption at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen, as shown in Figure 4d. The yellow and cyan regions in Figure 4d represent the increase and decrease in electron density, respectively. During the HO\* adsorption process of Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen, the electron density around the O atom of HO\* increases and the electron density around the Fe atom decreases, indicating that the electrons of Fe transferred to the O atom of HO\*. Meanwhile, the electron density around the coordinating B also decreases and is mainly concentrated at the B-O bond, suggesting that electrons of B atom are also transferred to the O atom of HO\*. These phenomena suggest that the main mechanism of HO\* adsorption on the catalyst is electron transfer.

Projected crystal orbital Hamiltonian population (pCOHP) analysis can quantitatively describe the strength of interatomic bonds. [24a] Herein, the integrated pCOHP (IpCOHP) of atom pairs was obtained by integrating pCOHP below the Fermi level to more quantitatively analyze the binding strengths. [38] A more negative IpCOHP corresponds to higher bonding and less antibonding contribution. To analyze the adsorption strength of HO\* at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen, we also chose the HO\* adsorption at

Figure 4. (a) Optimized adsorption configuration of HO\* at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen. (b) Stability of 1H\*, 2H\*, 3H\*, 4H\*, 1O\*, 1HO\*, and 1H<sub>2</sub>O\* on Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen at pH = 0. (c) Calculated PDOS for HO\* adsorption at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen. (d) Calculated EDD for HO\* adsorption at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen. The contour lines in the plot were drawn at 0.002 e/Å<sup>3</sup> intervals.

 $Fe_1N_3O_1$  and  $Fe_1B_1C_1N_2$ -pen in the pCOHP analyses for comparison. In the configuration in which HO\* is adsorbed at  $Fe_1N_3O_1$ ,

**Figure 5.** (a) pCOHP of the Fe–O interaction upon HO\* adsorption at Fe $_1$ N $_3$ O $_1$ . (b–c) pCOHP of the Fe–O and B–O interactions upon HO\* adsorption at Fe $_1$ B $_1$ C $_1$ N $_2$ -pen, respectively.

only the Fe atom forms the bonds with the O atom of HO\*, so we analyzed the strength of interaction at Fe-O bonds (Figure 5a). It can be seen that there is a considerable contribution of antibonding orbitals below the Fermi level, which is unfavorable for bonding, and the IpCOHP value is -2.52 eV. However, in the configuration where HO\* is adsorbed at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen, the O atom of HO\* forms both the Fe-O and B-O bonds at the catalyst. Therefore, the strengths of Fe-O and B-O bonds generated in this configuration were analyzed separately, as shown in Figure 5b-c. In this adsorption configuration, the contribution of antibonding orbital occupancy in the formation of Fe-O and B-O bonds is smaller than that in Figure 5a. This is advantageous for an increase in bond strength. Meanwhile, the average IpCOHP value (-5.29 eV) of Fe-O and B-O is much larger than that of the IpCOHP value (-2.52 eV) (Figure 5a), further confirming that it is the synergistic effects of B and Fe that lead to a relatively negative HO\* adsorption free energy at Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen.

#### Catalytic activities of TM<sub>1</sub>/B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen

To analyze the OER activity of SACs formed by the  $B_1C_1N_2$ -pen coordination environment combined with other transition metal single atoms, we calculated the O\* and HO\* adsorption free energies of  $TM_1/B_1C_1N_2$ -pen, where TM includes 3d, 4d, and 5d transition metals (i.e., TM = Ti-Zn, Zr-Cd, and Hf-Au). Hg atoms could not be stably anchored on the graphene substrate and were therefore excluded. Therefore, a total of  $26\ TM_1/B_1C_1N_2$ -pen catalysts were modelled for extensive analysis. The linear correlation between the adsorption free energies of  $TM_1/B_1C_1N_2$ -pen for  $HO^*$  and  $O^*$  is shown in Figure 6a, with detailed results tabulated in Table S2, the gray area in the figure is the upper and lower limits of the linear fit. The linear relationship between adsorption free energies of  $O^*$  and  $HO^*$  on the  $TM_1/B_1C_1N_2$ -pen catalysts is relatively discrete.

Previous studies<sup>[39]</sup> have pointed out that the fitted lines of  $\Delta G_{0^+}$  and  $\Delta G_{H0^+}$  are highly discrete, which is due to the different electron requirements of carbon-based electrocatalysts for

Figure 6. (a) Correlation between the adsorption free energies of HO\* and O\* at  $TM_1/B_1C_1N_2$ -pen. Blue, green, and red spheres represent 3d, 4d, and 5d transition metals, respectively. (b) OER volcano activity model of  $-\eta_{OER}$  vs. ( $\Delta G_{O^*} - \Delta G_{HO^*}$ ) plotted with the  $TM_1/B_1C_1N_2$ -pen systems.

different adsorbates. Therefore, this may also be one of the important reasons why Figure 6a presents a relatively discrete linear relationship. We further carefully examined the adsorption configurations of 26 TM<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen for HO\*, as shown in Figure S20. We found that catalysts with several special adsorption configurations (*i.e.*, Fe, Co, Ni, Cu, Pd, and Pt) were close to the fitted line in Figure 6a, while catalysts with a general adsorption configuration (*i.e.*, Zn, Ag, Hf, and Au) for HO\* deviates more severely from the fitted line. This means that the linear relationship dispersion in Figure 6a is mainly due to the different electron requirements for carbon-based electrocatalysts for different adsorbates.

With the volcano model, the  $\eta_{OER}$  of  $TM_1/B_1C_1N_2$ -pen can be determined (Figure 6b and Table S2). Interestingly,  $Fe_1B_1C_1N_2$ -pen still showed the most excellent catalytic performance for OER relative to other  $TM_1/B_1C_1N_2$ -pen catalysts.

To further show the activity performance of  $Fe_1B_1C_1N_2$ -pen for OER, we compared its activity with some single-atom iron catalysts that have been reported so far, as shown in Table 2. It can be found that at a similar DFT accuracy level, the catalytic activity of  $Fe_1B_1C_1N_2$ -pen for OER is higher than those of other single-atom iron catalysts reported so far.

It is worth noting that Fe<sub>1</sub>N<sub>4</sub> is widely used in various catalytic fields but has relatively poor catalytic activity for OER. We predicted an overpotential of 1.21 V for Fe<sub>1</sub>N<sub>4</sub> based on our volcano model, this is consistent with the OER activity of Fe<sub>1</sub>N<sub>4</sub> reported so far. Xue et al. [29a] it was pointed out that Fe<sub>1</sub>N<sub>4</sub> showed poor OER activity because of its weak adsorption strength to HO\*. We further analyzed the EDD and pCOHP of Fe<sub>1</sub>N<sub>4</sub> for HO\* adsorption to evaluate its electronic structure characteristics and bonding strength (Figure S21). EDD (Figure S21a) shows that when Fe<sub>1</sub>N<sub>4</sub> adsorbs HO\*, the electron density around the four coordinated N atoms and Fe atoms decreases, while the electron density around O atoms increases significantly. This indicates that the coordinating atoms in the catalyst are electron donors and O atoms are electron acceptors. pCOHP analysis (Figure S21b) showed that the binding strength between HO\* and Fe<sub>1</sub>N<sub>4</sub> (IpCOHP = -2.93 eV) was significantly weaker than that between HO\* and Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen (the average IpCOHP value -5.29 eV), this further revealed the reason for the lower OER activity of Fe<sub>1</sub>N<sub>4</sub>.

| <b>Table 2.</b> Predicted OER activities of various single-atom iron catalysts reported in literature. |                          |            |  |  |  |  |  |
|--------------------------------------------------------------------------------------------------------|--------------------------|------------|--|--|--|--|--|
| SACs                                                                                                   | $\eta_{OER} \ [V_{RHE}]$ | Functional |  |  |  |  |  |
| Fe <sub>1</sub> WO <sub>2</sub> <sup>[40]</sup>                                                        | 0.63                     | PBE        |  |  |  |  |  |
| Fe <sub>1</sub> Pc <sup>[41]</sup>                                                                     | 0.85                     | PBE-vdW    |  |  |  |  |  |
| Fe <sub>1</sub> DW <sup>[42]</sup>                                                                     | 0.78                     | BEEF-vdW   |  |  |  |  |  |
| Fe <sub>1</sub> VS <sub>2</sub> <sup>[43]</sup>                                                        | 0.84                     | PBE-vdW    |  |  |  |  |  |
| Fe <sub>1</sub> CN <sup>[44]</sup>                                                                     | 0.95                     | PBE-vdW    |  |  |  |  |  |
| Fe <sub>1</sub> N <sub>3</sub> <sup>[34]</sup>                                                         | 0.93                     | PBE-vdW    |  |  |  |  |  |
| Fe <sub>1</sub> N <sub>4</sub> <sup>[45]</sup>                                                         | 1.03~1.25                | PBE        |  |  |  |  |  |
| Fe₁PMA <sup>[46]</sup>                                                                                 | 0.75                     | PBE-vdW    |  |  |  |  |  |
| Fe₁TCNQ <sup>[47]</sup>                                                                                | 0.86                     | RPBE       |  |  |  |  |  |
| Fe <sub>1</sub> B <sub>1</sub> C <sub>1</sub> N <sub>2</sub> -pen <sup>[This work]</sup>               | 0.40                     | PBE-vdW    |  |  |  |  |  |

#### Conclusion

In summary, after screening 122 single-atom iron catalysts with various coordination environments, we found that single-atom iron catalyst with a Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen structure has a promising theoretical activity for OER. By comparing the single-atom binding and cohesive energies, 52 thermodynamically stable catalysts were identified. Their stability was further evaluated by calculating the formation energies. Through modulating the coordination environment of single-atom iron, the OER overpotentials can be effectively tailored in the range from 0.4 to 2.19 V<sub>RHF</sub>. Among these 52 single-atom iron catalysts, Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>pen has the highest catalytic activity due to a relatively large adsorption free energy for  $HO^*$  (-0.90 eV). The synergistic effect provided by B and Fe promotes the binding interaction with HO\*, which was further analyzed by electron transfer and pCOHP analysis. Furthermore, to analyze the catalytic activity of SACs based on the B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen coordination environment, the OER activities of 26 TM<sub>1</sub>/B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen were analyzed based on an OER volcano activity model. Interestingly, Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen still has the highest catalytic activity ( $\eta_{OER}$ =0.40 V) for OER among these TM<sub>1</sub>/B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen catalysts. Compared to the OER activities of other single-atom iron catalysts reported so far, this Fe<sub>1</sub>B<sub>1</sub>C<sub>1</sub>N<sub>2</sub>-pen has a relatively lower overpotential. Most importantly, this study shows that regulating the coordination environment of SACs can help promote catalytic performance. In future work, we expect that the combination of transition metals with other coordination substrates can lead to more exciting discoveries.

#### **Acknowledgements**

This work was funded by the National Natural Science Foundation of China (Nos. 52006073 and 52176104), Natural Science Foundation of Hebei (No. E2020502023), and Australian Research Council under the Future Fellowship (FT210100218). Li Wei and Hao Li acknowledge the University of Sydney under the International SDG Collaboration Program. The authors acknowledge Beijng PARATERA Tech CO.,Ltd. for providing HPC resources that have contributed to the research results reported within this paper.

## **Conflict of Interest**

The authors declare no conflict of interest.

#### **Data Availability Statement**

The data that support the findings of this study are available in the supplementary material of this article.

**Keywords:** coordination environment  $\cdot$  electrocatalysis  $\cdot$  oxygen evolution  $\cdot$  single-atom iron catalysts  $\cdot$  volcano model

18673899

- a) M.-J. Kim, J. E. Park, S. Kim, M. S. Lim, A. Jin, O.-H. Kim, M. J. Kim, K.-S. Lee, J. Kim, S.-S. Kim, Y.-H. Cho, Y.-E. Sung, ACS Catal. 2019, 9, 3389–3398; b) M. Li, X. Bi, R. Wang, Y. Li, G. Jiang, L. Li, C. Zhong, Z. Chen, J. Lu, Matter. 2020, 2, 32–49; c) E. Wang, Z. Yan, Q. Liu, J. Gao, M. Liu, G. Sun, in Anion Exchange Membrane Fuel Cells, 2018, pp. 285–323; d) S. Zhang, M. Chen, X. Zhao, J. Cai, W. Yan, J. C. Yen, S. Chen, Y. Yu, J. Zhang, Electrochem. Energy Rev. 2021, 4, 336–381; e) X. Liao, R. Lu, L. Xia, Q. Liu, H. Wang, K. Zhao, Z. Wang, Y. Zhao, Energy Environ. Mater. 2021, 5, 157–185.
- [2] a) H. Hu, J. Wang, P. Tao, C. Song, W. Shang, T. Deng, J. Wu, J. Mater. Chem. A 2022, 10, 5835–5849; b) Y. Shang, X. Duan, S. Wang, Q. Yue, B. Gao, X. Xu, Chin. Chem. Lett. 2022, 33, 663–673; c) C. Liu, H. Li, F. Liu, J. Chen, Z. Yu, Z. Yuan, C. Wang, H. Zheng, G. Henkelman, L. Wei, Y. Chen, J. Am. Chem. Soc. 2020, 142, 21861–21871; d) H. Li, B. Yu, Z. Zhuang, W. Sun, B. Jia, T. Ma, J. Mater. Chem. A 2021, 9, 4184–4192.
- [3] a) U. K. Sur, Int. J. Electrochem. 2012, 2012, 1–12; b) S. Ren, Q. Yu, X. Yu, P. Rong, L. Jiang, J. Jiang, Sci. China Mater. 2020, 63, 903–920; c) W. Yang, S. Xu, K. Ma, C. Wu, I. D. Gates, X. Ding, W. Meng, Z. Gao, Nano Mater. Sci. 2020, 2, 120–131; d) H. Y. Zhuo, X. Zhang, J. X. Liang, Q. Yu, H. Xiao, J. Li, Chem. Rev. 2020, 120, 12315–12341; e) B. Zhang, T. Fan, N. Xie, G. Nie, H. Zhang, Adv. Sci. 2019, 6, 1901787.
- [4] a) X. Yan, K. Liu, T. Wang, Y. You, J. Liu, P. Wang, X. Pan, G. Wang, J. Luo, J. Zhu, J. Mater. Chem. A 2017, 5, 3336–3345; b) F. Chen, X. L. Wu, C. Shi, H. Lin, J. Chen, Y. Shi, S. Wang, X. Duan, Adv. Funct. Mater. 2021, 31; c) H. Shen, T. Thomas, S. A. Rasaki, A. Saad, C. Hu, J. Wang, M. Yang, Electrochem. Energy Rev. 2019, 2, 252–276; d) Y. Pan, Y. Chen, K. Wu, Z. Chen, S. Liu, X. Cao, W. C. Cheong, T. Meng, J. Luo, L. Zheng, C. Liu, D. Wang, Q. Peng, J. Li, C. Chen, Nat. Commun. 2019, 10, 4290.
- [5] a) W. Yang, X. Liu, X. Chen, Y. Cao, S. Cui, L. Jiao, C. Wu, C. Chen, D. Fu, I. D. Gates, Z. Gao, H. L. Jiang, Adv. Mater. 2022, 34, e2110123; b) J. Wang, B. Li, Y. Li, X. Fan, F. Zhang, G. Zhang, W. Peng, Adv. Sci. 2021, 8, e2101824; c) E. Ashori, F. Nazari, F. Illas, Phys. Chem. Chem. Phys. 2017, 19, 3201–3213; d) L. Jiao, J. Li, L. L. Richard, Q. Sun, T. Stracensky, E. Lim, M. T. Sougrati, Z. Zhao, F. Yang, S. Zhong, H. Xu, S. Mukerjee, Y. Huang, D. A. Cullen, J. H. Park, M. Ferrandon, D. J. Myers, F. Jaouen, Q. Jia, Nat. Mater. 2021, 20, 1385–1391.
- [6] S. Kattel, G. Wang, J. Phys. Chem. Lett. 2014, 5, 452-456.
- [7] B. He, J. Shen, D. Ma, Z. Lu, Z. Yang, J. Phys. Chem. C 2018, 122, 20312– 20322.
- [8] H. Sun, Y. Ma, Q. Zhang, C. Su, *Trans. Tianjin Univ.* **2021**, *27*, 313–330.
- [9] a) K. Qu, Y. Zheng, S. Dai, S. Z. Qiao, Nano Energy 2016, 19, 373–381;
  b) R. Zhang, Y. Fang, T. Chen, F. Qu, Z. Liu, G. Du, A. M. Asiri, T. Gao, X. Sun, ACS Sustainable Chem. Eng. 2017, 5, 7502–7506.
- [10] Y. Tang, W. Chen, J. Shi, Z. Wang, Y. Cui, D. Teng, Y. Li, Z. Feng, X. Dai, J. Mater. Chem. A 2021, 9, 15329–15345.
- [11] C. Wang, D. Wang, S. Liu, P. Jiang, Z. Lin, P. Xu, K. Yang, J. Lu, H. Tong, L. Hu, W. Zhang, Q. Chen, J. Catal. 2020, 389, 150–156.
- [12] M. Ren, X. Guo, S. Huang, Chem. Eng. J. 2022, 433.
- [13] C. Tang, Y. Jiao, B. Shi, J. N. Liu, Z. Xie, X. Chen, Q. Zhang, S. Z. Qiao, Angew. Chem. Int. Ed. Engl. 2020, 59, 9171–9176.
- [14] J. Li, Y. Zhou, W. Tang, J. Zheng, X. Gao, N. Wang, X. Chen, M. Wei, X. Xiao, W. Chu, *Appl. Catal. B* **2021**, *285*.
- [15] J. Zhang, M. Zhang, Y. Zeng, J. Chen, L. Qiu, H. Zhou, C. Sun, Y. Yu, C. Zhu, Z. Zhu, Small 2019, 15, e1900307.
- [16] K. Yuan, D. Lutzenkirchen-Hecht, L. Li, L. Shuai, Y. Li, R. Cao, M. Qiu, X. Zhuang, M. K. H. Leung, Y. Chen, U. Scherf, J. Am. Chem. Soc. 2020, 142, 2404–2412.
- [17] Y. Hou, M. Qiu, M. G. Kim, P. Liu, G. Nam, T. Zhang, X. Zhuang, B. Yang, J. Cho, M. Chen, C. Yuan, L. Lei, X. Feng, Nat. Commun. 2019, 10, 1392.
- [18] Y. Chen, S. Ji, S. Zhao, W. Chen, J. Dong, W. C. Cheong, R. Shen, X. Wen, L. Zheng, A. I. Rykov, S. Cai, H. Tang, Z. Zhuang, C. Chen, Q. Peng, D. Wang, Y. Li, *Nat. Commun.* 2018, 9, 5422.
- [19] L. Shi, S. Bi, Y. Qi, R. He, K. Ren, L. Zheng, J. Wang, G. Ning, J. Ye, ACS Catal. 2022, 12, 7655–7663.
- [20] a) F. J. Kresse G, Comput. Mater. Sci. 1996, 6, 15–50; b) J. D. Kresse G, Phys. Rev. B 1999, 59, 1758–1775.
- [21] F. J. Kresse G, Phys. Rev. B 1996, 54, 11169–11186.
- [22] A. D. Becke, E. R. Johnson, J. Chem. Phys. 2005, 122, 154104.
- [23] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, J. Chem. Phys. 2010, 132, 154104.

- [24] a) V. L. Deringer, A. L. Tchougreeff, R. Dronskowski, J. Phys. Chem. A 2011, 115, 5461–5466; b) S. Maintz, V. L. Deringer, A. L. Tchougreeff, R. Dronskowski, J. Comput. Chem. 2013, 34, 2557–2567; c) S. Maintz, V. L. Deringer, A. L. Tchougreeff, R. Dronskowski, J. Comput. Chem. 2016, 37, 1030–1035.
- [25] L. Li, R. Huang, X. Cao, Y. Wen, *J. Mater. Chem. A* **2020**, *8*, 19319–19327.
- [26] a) Z. A. Piazza, H. S. Hu, W. L. Li, Y. F. Zhao, J. Li, L. S. Wang, Nat. Commun. 2014, 5, 3113; b) N. Yang, X. Zheng, L. Li, J. Li, Z. Wei, J. Phys. Chem. C 2017, 121, 19321–19328; c) L. Zhang, J. Niu, M. Li, Z. Xia, J. Phys. Chem. C 2014, 118, 3545–3553.
- [27] I. C. Man, H. Y. Su, F. Calle-Vallejo, H. A. Hansen, J. I. Martínez, N. G. Inoglu, J. Kitchin, T. F. Jaramillo, J. K. Nørskov, J. Rossmeisl, *ChemCatChem* 2011, 3, 1159–1165.
- [28] J. Rossmeisl, Z. W. Qu, H. Zhu, G. J. Kroes, J. K. Nørskov, J. Electroanal. Chem. 2007, 607, 83–89.
- [29] a) Z. Xue, X. Zhang, J. Qin, R. Liu, J. Energy Chem. 2021, 55, 437–443;
  b) C. Zhang, S. Qin, B. Li, P. Jin, J. Mater. Chem. A 2022, 10, 8309–8323;
  c) X. Zhang, A. Chen, Z. Zhang, M. Jiao, Z. Zhou, J. Mater. Chem. A 2018, 6, 11446–11452.
- [30] M. Li, L. Zhang, Q. Xu, J. Niu, Z. Xia, J. Catal. 2014, 314, 66-72.
- [31] M. Bajdich, M. Garcia-Mota, A. Vojvodic, J. K. Norskov, A. T. Bell, J. Am. Chem. Soc. 2013, 135, 13521–13530.
- [32] M. Liu, C. Liu, S. Gouse Peera, T. Liang, Chem. Phys. 2022, 559.
- [33] P. Janthon, S. M. Kozlov, F. Vines, J. Limtrakul, F. Illas, J. Chem. Theory Comput. 2013, 9, 1631–1640.
- [34] G. Xiao, R. Lu, J. Liu, X. Liao, Z. Wang, Y. Zhao, Nano Res. 2021, 15, 3073–3081.
- [35] a) M. García-Mota, M. Bajdich, V. Viswanathan, A. Vojvodic, A. T. Bell, J. K. Nørskov, J. Phys. Chem. C 2012, 116, 21077–21082; b) G. T. K. K. Gunasooriya, J. K. Nørskov, ACS Energy Lett. 2020, 5, 3778–3787; c) R. Christensen, H. A. Hansen, C. F. Dickens, J. K. Nørskov, T. Vegge, J. Phys. Chem. C 2016, 120, 24910–24916.
- [36] H. Li, S. Kelly, D. Guevarra, Z. Wang, Y. Wang, J. A. Haber, M. Anand, G. T. K. K. Gunasooriya, C. S. Abraham, S. Vijay, J. M. Gregoire, J. K. Nørskov, Nat. Catal. 2021, 4, 463–468.
- [37] W. Zou, R. Lu, X. Liu, G. Xiao, X. Liao, Z. Wang, Y. Zhao, J. Mater. Chem. A 2022, 10, 9150–9160.
- [38] X. Han, Z. Zhang, X. Xu, J. Mater. Chem. A 2021, 9, 12225–12235.
- [39] a) F. Calle-Vallejo, J. I. Martinez, J. Rossmeisl, *Phys. Chem. Chem. Phys.* **2011**, *13*, 15639–15643; b) J. D. Baran, H. Gronbeck, A. Hellman, *J. Am. Chem. Soc.* **2014**, *136*, 1320–1326; c) B. B. Xiao, H. Y. Liu, L. Yang, E. H. Song, X. B. Jiang, Q. Jiang, *ACS Appl. Energ. Mater.* **2019**, *3*, 260–267.
- [40] Y. Ma, F. Jin, Y. H. Hu, Phys. Chem. Chem. Phys. 2021, 23, 13687-13695.
- [41] X. Li, Z. Wang, Z. Su, Z. Zhao, Q. Cai, J. Zhao, ChemPhysMater 2022, 1, 237–245.
- [42] Q. Deng, J. Han, J. Zhao, G. Chen, T. Vegge, H. Anton Hansen, J. Catal. 2021, 393, 140–148.
- [43] Z. Qin, Z. Wang, J. Zhao, Nanoscale 2022, 14, 6902–6911.
- [44] X. Lv, W. Wei, H. Wang, B. Huang, Y. Dai, Appl. Catal. B 2020, 264.
- [45] a) X. Zhang, Q. Zhang, J. Cui, J. Yan, J. Liu, Y. Wu, Nanoscale 2022, 14, 3212–3223; b) C. Lei, H. Chen, J. Cao, J. Yang, M. Qiu, Y. Xia, C. Yuan, B. Yang, Z. Li, X. Zhang, L. Lei, J. Abbott, Y. Zhong, X. Xia, G. Wu, Q. He, Y. Hou, Adv. Energy Mater. 2018, 8; c) X. Li, Z. Su, Z. Zhao, Q. Cai, Y. Li, J. Zhao, J. Colloid Interface Sci. 2022, 607, 1005–1013; d) Y. Li, R. Hu, Z. Chen, X. Wan, J.-X. Shang, F.-H. Wang, J. Shui, Nano Res. 2020, 14, 611–619; e) C. Zheng, X. Zhang, Z. Zhou, Z. Hu, eScience 2022, 2, 219–226; f) Y. Zhou, G. Gao, Y. Li, W. Chu, L. W. Wang, Phys. Chem. Chem. Phys. 2019, 21, 3024–3032.
- [46] S. H. Talib, Z. Lu, X. Yu, K. Ahmad, B. Bashir, Z. Yang, J. Li, ACS Catal. 2021, 11, 8929–8941.
- [47] Q. Deng, J. Zhao, T. Wu, G. Chen, H. A. Hansen, T. Vegge, ACS Catal. 2019, 370, 378–384.

Manuscript received: August 11, 2022 Revised manuscript received: September 18, 2022 Version of record online: October 26, 2022