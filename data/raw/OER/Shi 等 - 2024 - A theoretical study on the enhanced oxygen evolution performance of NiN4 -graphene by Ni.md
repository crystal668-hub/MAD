---
source: Shi 等 - 2024 - A theoretical study on the enhanced oxygen evolution performance of NiN4 -graphene by Ni.pdf
tool: marker
duration: 79.265s
generated: 2026-01-09T07:50:26.549175Z
---

#### **PAPER**

# A theoretical study on the enhanced oxygen evolution performance of NiN<sub>4</sub>-graphene by Ni nanoclusters

To cite this article: Runchuan Shi et al 2024 J. Phys. D: Appl. Phys. 57 205301

View the <u>article online</u> for updates and enhancements.

# You may also like

- Enhanced quantum capacitance of MX<sub>4</sub> (M = Fe, Co, Ni, Cu, and Zn; X = N, P) moieties embedded graphene: a DFT study

Babita Rani, Vladimir Bubanja and Vijay K

- <u>Structural</u>, electronic, elastic, thermodynamical and thermoelectric properties of TMN (TM = Co. Ni) A Azouaoui, M El haoua, N Benzakour et al
- Band gap engineering and photoelectronic properties of novel pentagonal materials penta-XN<sub>2</sub> (X = Ni, Pt): a first principle calculations

Keyan Han, Lin Huang, Cheng Luo et al.

# **A theoretical study on the enhanced oxygen evolution performance of NiN4 -graphene by Ni nanoclusters**

**Runchuan Shi**[1](#page-1-0) **, Shihao Feng**[1](#page-1-0) **, Zhaoming Fu**[2](#page-1-1) **, Zongxian Yang**[1,](#page-1-0)*[∗](#page-1-2)* **and Xilin Zhang**[1,](#page-1-0)*[∗](#page-1-2)*

E-mail: [yzx@htu.edu.cn](mailto:yzx@htu.edu.cn) and [xlzhang828@126.com](mailto:xlzhang828@126.com)

Received 11 December 2023 Accepted for publication 14 February 2024 Published 22 February 2024

#### **Abstract**

Isolated metal-coordinated nitrogen embedded carbon (M–N–C) materials are potential alternatives to noble catalysts for oxygen evolution reaction (OER), and the activity of metal centers can be further modulated by adjusting the coordination environment. Recently, experimental studies have shown that the aggregation of metal atoms into small clusters or particles is inevitable during the high temperature pyrolysis, while the influences of metal clusters on the OER activity of single metal atoms in M–N–C are unclear. Herein, taking Ni-based single atom as examples, the interaction characters of NiN<sup>4</sup> doped graphene (NiN4-graphene) with different Ni clusters were studied. The modulation effects of Ni clusters to the NiN4-graphene were systematically investigated from the geometric configurations, electronic structures, and the OER activity of the Ni single atom. It was found that the OER performance of NiN4-graphene can be remarkably improved through the addition of Ni clusters, and the lowest overpotential of 0.43 V is achieved on NiN4-graphene with the modification of Ni<sup>13</sup> cluster, which is smaller than that of 0.69 V on NiN4-graphene. Electronic properties calculations showed that the charge transfer from Ni clusters to NiN4-graphene will alter the density of states of Ni single atom near the Fermi level, which promotes the charge transfer from NiN4-graphene to oxygen containing products and optimizes the adsorption strength of oxygen intermediate to close to the ideal adsorption free energy of 2.46 eV by enhancing the hybridization interaction between the O-p orbitals and the Ni-*dxz*, Ni-*dyz* orbitals, and finally leading to an enhanced OER activity. The current findings highlight the important role of metal clusters on improving the catalytic performance of M–N–C materials, which benefits for the rational design of M–N–C catalysts with high catalytic activity.

Supplementary material for this article is available [online](http://doi.org/10.1088/1361-6463/ad297c)

Keywords: oxygen evolution reaction (OER), Ni clusters, Ni single atom, density functional theory

<span id="page-1-0"></span><sup>1</sup> School of Physics, Henan Key Laboratory of Photovoltaic Materials, Henan Normal University, Xinxiang 453007, People's Republic of China

<span id="page-1-1"></span><sup>2</sup> College of Physics and Electronic Information, Yunnan Normal University, Kunming 650500, People's Republic of China

<span id="page-1-2"></span>*<sup>∗</sup>* Authors to whom any correspondence should be addressed.

# **1. Introduction**

Electrolyzed water is a clean, sustainable, and efficient method of producing hydrogen, which will become a crucial part of future renewable energy production. Oxygen evolution reaction (OER) plays a key role in water decomposition[[1–](#page-8-0) [6\]](#page-8-1). However, the sluggish dynamics of this process emphasize the importance of the catalyst in accelerating the rate and increasing the desired product selectivity. Consequently, the development of advanced catalysts with high catalytic activity holds immense potential for boosting the efficiency of various catalytic processes.

Single-atom catalysts (SACs) have emerged as promising alternatives to precious metal catalysts for efficient OERs[[7\]](#page-8-2). In recent years, isolated metal-coordinated nitrogen embedded carbon (M–N–C) (where M represents Fe, Co, Cu, Mn, Ni) materials have garnered significant attention in the field of electrocatalysis among various non-precious metal catalysts [\[8](#page-8-3)[–10](#page-8-4)]. In the case of M–N–C catalysts, the OER performance is generally governed by the electronic characteristics of metal single atoms, which can be regulated by tuning the coordination atoms [\[9](#page-8-5)[–12](#page-8-6)]. Zhang *et al* found that the activity of CoN*x*-gra towards OER would be affected by the N-dopant concentration [\[13](#page-8-7)]. Liu *et al* revealed that the central metal and the coordinating atoms strongly influence oxygen electrocatalysis over 3d transition metal SACs [\[14](#page-8-8)]. Using x-ray absorption spectroscopy methods, Zhang *et al* revealed that the effective electronic coupling via the Ni–N coordination can lower the adsorption energy of intermediates, thus resulting in facilitated OER kinetics[[15\]](#page-8-9).

Experimental studies have shown that the aggregation of metal atoms into small clusters or particles is inevitable during the high temperature pyrolysis [\[16](#page-8-10)[–18](#page-8-11)], which can also impact the OER activity of the metal single atom. Han developed a novel and facile strategy to synthesize Ni nanoparticles (NPs) embedded in N doped carbon nanotubes (Ni NPs@N-CNTs) catalyst by using Ni metal organic framework (Ni-MOF) as the precursor and the Ni NPs@N-CNTs catalyst shows an improved OER performance which was 0.46 V vs. RHE [\[19](#page-8-12)]. Liu reported an electrocatalysts of transition metal nanoparticles encapsulated in nitrogen-doped carbon nanotubes (M/N-CNTs, M=Fe, Co, and Ni). The oxygen electrode activity value for Ni/N-CNTs is 0.56 V vs. RHE, superior to the other considered catalysts [\[20](#page-8-13)]. In the previous work, we experimentally prepared the NiN<sup>4</sup> doped carbon (NiN4 graphene) materials and explored the overpotential [\[21](#page-8-14)]. The results indicated that the OER activity of Ni single atom can be enhanced by the Ni nanoparticles due to the synergistic improvement. However, limited by the characterization technologies, it is experimentally difficult to accurately determine the existence of small clusters or single atoms. As a supplement to the experiment, the synergistic effect between metal clusters and metal single atom can be unveiled from the DFT calculations by investigating the atomic structure, electronic structure, and reaction process.

The clusters with different size were chosen in order to explore the modulating effect of clusters on NiN4-graphene better (Next, we will use 'Ni*x*' to represent Ni clusters with different sizes.) It has been observed that NiN4-graphene/Ni*<sup>x</sup>* exhibits higher catalytic activity in comparison with NiN4 graphene. The adsorption strength between the Ni single atom and adsorbates was modulated by the addition of clusters, which enhanced the charge transfer between NiN4-graphene and oxygen containing products, resulting in the adsorption free energy being closer to the desired value of 2.46 eV and ultimately improving the OER activity of the catalyst. To sum up, this study may offer insights into the regulation of catalyst activity and proposes a rational strategy for clusters composite SACs.

# **2. Computational methods**

Density functional theory calculation as implemented in the Vienna ab initio simulation package [\[22](#page-8-15), [23](#page-8-16)] code was carried out to optimize all of the initial geometrical structures. A generalized gradient approximation in the form of the Perdew– Burke–Ernzerhof functional was employed[[24\]](#page-8-17). A plane wave cutoff energy of 520 eV was used for the plane-wave expansion of the wave function, and the convergence thresholds for the total energy and force of the structure optimization are 10*−*<sup>5</sup> eV and 0.02 eV Å*−*<sup>1</sup> , respectively.

The convergence of geometrical parameters was also tested. Brillouin zone integrations were performed using a 3 *×* 3 *×* 1 Gamma-Centered K-point mesh for geometry optimizations as well as density of states calculations. The Brillouin zone was sampled using a 11 *×* 11 *×* 1 Kgrids. Taking into account the clusters size, 4 *×* 4 (NiN4 graphene/Ni4, NiN4-graphene/Ni (111)) and 5 *×* 5 (NiN4 graphene/Ni13) supercells were constructed as adsorption simulation models with a vacuum layer of 20 Å in the *Z* direction to avoid interactions during adjacent periodic images. After examining the effects of Hubbard-U (as shown in figure S2) and comparing with previous results[[2,](#page-8-18) [25](#page-8-19)], the Hubbard-U correction (U = 3 eV)[[3,](#page-8-20) [25,](#page-8-19) [26\]](#page-9-0) is also considered, which approximately compensates for the incomplete elimination of electron self-interactions and the inaccurate description of the strong correlation effects in the standard exchange and associated functionals. Taking the DFT-D3 approach to describe the van der Waals action[[27,](#page-9-1) [28\]](#page-9-2). Also, the spin polarization was applied during the whole calculation. The thermodynamic stability was simulated by ab initio molecular dynamics (AIMD). An implicit solvation model was adopted to simulate the H2O solvent environment, with the corresponding dielectric constant set at 78.54[[29\]](#page-9-3). The determination of the bonding and anti-bonding states between Ni and O atom was obtained by the projected crystal orbital Hamilton population (pCOHP) [[30,](#page-9-4) [31\]](#page-9-5) as employed by the Lobster program. The overpotentials that characterize the catalytic activities for OER at various sites were calculated by the standard hydrogen electrode method developed by Nørskov *et al* [[32\]](#page-9-6).

In acid media, the overall OER could be expressed as:

$$2H_2O \rightarrow O_2 + 4H^+ + 4e^-.$$
 (1)

Since the OER proceeds mainly along 4e *<sup>−</sup>* processes we thus explore the OER reaction via 4e *<sup>−</sup>* pathways. The elementary reaction steps are listed as below:

\* + 
$$H_2O(1) \rightarrow OH^* + H^+ + 4e^-$$
 (a)

$$OH^* \rightarrow O^* + H^+ + e^- \tag{b}$$

$$O^* + H_2O(1) \to OOH^* + H^+ + e^-$$
 (c)

$$OOH^* \to * + O_2(g) + H^+ + e^-$$
 (d)

where *<sup>∗</sup>* stands for an adsorption site on catalysts. l and g refer to liquid and gas phases, respectively. The adsorption energies of oxygen-containing intermediates on NiN4-graphene, NiN4-graphene/Ni*<sup>x</sup>* (*x* = 4,13), NiN4-graphene/Ni (111) were calculated by following equation

$$\Delta E_{O^*} = E_{O^*} - E_* - [E_{H_2O} - E_{H_2}] \eqno(2)$$

$$\Delta E_{OH^*} = E_{OH^*} - E_* - [E_{H_2O} - 1/2E_{H_2}] \tag{3}$$

$$\Delta E_{\text{OOH*}} = E_{\text{OOH*}} - E_* - [2E_{\text{H}_2\text{O}} - 3/2E_{\text{H}_2}]$$
 (4)

in which the E\* is total energies of pristine catalysts. EOOH\*, EOH\*, and EO\* are the total energies of catalyst substrate with the adsorption of OOH, OH and O, respectively. EH2<sup>O</sup> and EH<sup>2</sup> are total energies of free H2O and H<sup>2</sup> molecules in gas phases, respectively. Then the adsorption free energies can be obtained by including the zero-point energy and the entropy (S) corrections in equation:

$$\Delta G = \Delta E + \Delta ZPE - T\Delta S + \Delta G_U - \Delta G_{PH}. \tag{5}$$

The ∆ZPE could be obtained from the calculation of vibrational frequencies for the adsorbed species. Actually, the ∆ZPE and the entropy of the adsorbed oxygenated intermediates on different catalysts are found to have similar values, T is room temperature (298.15 K).

As proposed by Norskov *et al* the catalytic activity of OER catalysts depends on the Gibbs free energies of intermediates (∆GOH*<sup>∗</sup>* , ∆G<sup>O</sup> *<sup>∗</sup>* and ∆GOOH*<sup>∗</sup>* ) [\[33](#page-9-7)]. In an ideal case, the Gibbs free energy change (∆G<sup>i</sup> (i = a, b, c, d)) between two neighboring intermediates should be 1.23 eV under U = 0 V. In reality, the ∆G<sup>i</sup> between two adjacent intermediates is unequal, limiting the OER process. The overpotential (*η*OER) of the OER depends on the maximum ∆G<sup>i</sup> , and could be calculated by:

$$\eta_{\text{OER}} = \max \left\{ \Delta G_{\text{a}}, \Delta G_{\text{b}}, \Delta G_{\text{c}}, \Delta G_{\text{d}} \right\} / \text{e} - 1.23 \text{ V}.$$
(6)

## **3. Results and discussion**

#### *3.1. Simulation model and stability*

The optimized lattice constants of graphene and bulk Ni are 2.47 Å and 2.49 Å, respectively, which coincide with the existing results [\[13](#page-8-7), [34](#page-9-8)]. For NiN4-graphene/Ni (111), a 5 *×* 5 unit cell with a four-layer slab was utilized, with the last two layers being fixed. The distance between the carbon layer and the Ni (111) surface was determined to be 2.12 Å, consistent with the previous work[[34\]](#page-9-8). In order to assess the stability of clusters adsorption, the adsorption energy was calculated using the following expression:

$$E_{ads} = E_{Slab} + E_{Cluster} - E_{tot}$$
 (7)

where Etot represents the total energies of the NiN4 graphene after adsorption, ESlab refers to the energies of the NiN4-graphene and ECluster represents the energies of the clusters as well as Ni (111). According to previous results, the isolated Ni<sup>4</sup> prefer to the regular tetrahedron configuration, while the Ni<sup>13</sup> adopted a regular twentytetrahedron configuration[[35–](#page-9-9)[38\]](#page-9-10). Thus, these most stable structures were adopted as promoters to explore their effects on tuning the OER activity of the Ni single atom (named as NiN4-graphene/Ni*x*). The adsorption energies of NiN4 graphene/Ni4, NiN4-graphene/Ni<sup>13</sup> and NiN4-graphene/Ni (111) were *−*1.74 eV, *−*2.87 eV, and *−*3.38 eV. The formation energies results indicating the stability. The thermodynamic stability of the four configurations was further examined by first-principles AIMD. To simulate the real environment, we amplify the original structure in order to ensure that the number of atoms is more than 100. Then, at 500 K, the evolution curve of the energies of the four configurations over time are shown in figure [1.](#page-4-0) Figures [1](#page-4-0)(b)–(d) shows that the energy within 10 ps fluctuates within a reasonable range at 500 K and remains stable overall. Furthermore, the structure evolution fragments of NiN4-graphene under the MD simulations are illustrated in figure S1. Although the structure of NiN4-graphene fluctuates slightly, but the atoms positions are still within rational ranges, which confirms the stability. Especially, the formation energies of NiN4 graphene are calculated to be *−*4.34 eV according to the follow equation[[39\]](#page-9-11):

$$E_{f} = E_{NiN4-graphene} + 5_{C} - (E_{graphene} + 4\mu_{N} + \mu_{Ni})$$
 (8)

where ENiN4-graphene and Egraphene are the total energy of the NiN4-graphene site and the pristine graphene single layer, respectively. *µ*<sup>C</sup> is the chemical potential of the carbon atom defined as the total energy per carbon atom in a perfect graphene single layer. *µ*<sup>N</sup> is the chemical potential of the doped nitrogen atom defined as one-half energy of the N<sup>2</sup> molecule in the gas phase. *µ*Ni is the chemical potential of the Ni atom defined as the energy of an isolated monatomic

<span id="page-4-0"></span>Figure 1. Time evolution curves of the energy of (a)  $NiN_4$ -graphene, (b)  $NiN_4$ -graphene/ $Ni_4$ , (c)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/Ni (111), respectively.

configuration. The formation energies results indicate the stability. Actually, the  $NiN_4$ -motif embedded in carbon matrix has been experimentally prepared using various methods, confirming the excellent stability again [40, 41].

#### 3.2. Catalytic performance analysis

The OER performance of four simulation models was primarily studied. Figure 2 presents the most stable adsorption configurations of O\*, OH\*, and OOH\* on NiN4-graphene, NiN4graphene/Ni<sub>13</sub>. From table S2, the bond length of Ni and O on NiN<sub>4</sub>-graphene, NiN<sub>4</sub>-graphene/Ni<sub>4</sub>, NiN<sub>4</sub>-graphene/Ni<sub>13</sub>, and NiN<sub>4</sub>-graphene/Ni (111) are 1.75 Å; 1.64 Å; 1.65 Å and 1.73 Å respectively. A shorter bond length usually generates a stronger adsorption. Consequently, NiN<sub>4</sub>-graphene/Ni<sub>4</sub> exhibits the strongest adsorption to the O atom (-4.81 eV), while  $NiN_4$ -graphene has the weakest adsorption (-2.93 eV). The possibility of clusters as active sites was also considered. Figure S3 shows that the adsorption energies of O atom at site1 and site 2 were -5.65 eV and -5.62 eV, respectively, implying a strong adsorption of O atom on Ni cluster. Therefore, it is impractical to use clusters as active sites. Figure 3 shows the reaction free energy diagram of the four configurations at  $\varepsilon = 1.23$  V, (where  $\varepsilon = 1.23$  V is the standard electrode potential.) It is evident that the NiN<sub>4</sub>-graphene has a high overpotential, which is mainly due to the weak adsorption strength between the Ni single atom and the O atom. However, the adsorption strength between the Ni single atom and the O atom was optimized by the addition of clusters, from figure 3(c) the adsorption free energy was reduced from 3.5 eV to 2.45 eV, which close to the ideal adsorption free energy of 2.46 eV, and the reaction barrier of  $OH^* \rightarrow O^*$ 

was reduced to 1.66 eV. As a result, the OER performance of the NiN<sub>4</sub>-graphene was improved from 0.69 V to 0.43 V. The scaling relationship between the adsorption free energies of different adsorption species can also be established to extrapolate the minimum overpotential through the according descriptor. As displayed in figure 4(a) there exists a linear relation  $\Delta G_{OOH^*} = \Delta G_{OH^*} {+} 2.87$  between  $\Delta G_{OOH^*}$  and  $\Delta G_{OH^*}$  with the coefficient of determination (R<sup>2</sup>) of 0.986. The reverse volcano plot of  $\eta^{OER}$  with  $(\Delta G_{O^*} - \Delta G_{OH^*})$ on NiN<sub>4</sub>-graphene, NiN<sub>4</sub>-graphene/Ni<sub>4</sub>, NiN<sub>4</sub>-graphene/Ni<sub>13</sub>, and NiN<sub>4</sub>-graphene/Ni (111) is shown in figure 4(b). In the downhill section of reverse volcano is dominated by reaction of  $O^* + H_2O \rightarrow OOH^* + (H^+ + e^-)$ , and the uphill part by reaction of  $OH^* \rightarrow O^* + (H^+ + e^-)$ . With this relationship, a reasonable hypothesis can be established that the lower limit of OER overpotential ( $\eta^{\rm OER}$ ) is 0.28 eV under the condition  $\Delta G_{O^*} - \Delta G_{OH^*} = 1.5$  eV.

#### 3.3. Electronic structure analysis

3.3.1. Charge transfer. The charge transfer can be conducted to evaluate the binding strength between the Ni single atom and the O atom. According to Bader charge analysis, the amount of charge transfer between the O atom and the Ni single atom in NiN<sub>4</sub>-graphene is 0.56 lel and it increased to 0.69 lel, 0.65 lel, 0.59 lel in NiN<sub>4</sub>-graphene/Ni<sub>4</sub>, NiN<sub>4</sub>-graphene/Ni<sub>13</sub>, and NiN<sub>4</sub>-graphene/Ni (111) respectively, which indicates that the interaction between the O atom and the Ni single atom is enhanced. As shown in figures 5(a)–(d), an electron localization function (ELF) analysis was performed. The value of ELF between two atoms can be in the range of 0–1, where 1, 0.5, and 0 represent covalent, metallic,

<span id="page-5-0"></span>**Figure 2.** The most stable adsorption configurations of O*<sup>∗</sup>* , OH*<sup>∗</sup>* and OOH*<sup>∗</sup>* on NiN4-graphene (a)–(c), NiN4-graphene/Ni<sup>13</sup> (d)–(f), respectively (top view). (Figure S4. The top view of NiN4-graphene/Ni<sup>4</sup> and NiN4-graphene/Ni (111),) and the corresponding side view are summarized in supporting information figure S5. The grey, blue, cyan-blue, red, and white color present C atom, Ni atom, N atom, O atom, and H atom, respectively.

<span id="page-5-1"></span>**Figure 3.** Calculated Gibbs free energy diagrams for (a) NiN4-graphene, (b) NiN4-graphene/Ni4, (c) NiN4-graphene/Ni13, (d) NiN4-graphene/Ni (111), respectively. For the OER process, where the elementary step in red represents the PDS of the whole process.

and no-bonding characters, respectively. It can be seen that the N atoms and the Ni single atom become more localized, indicating that the electrons are more concentrated in NiN4 graphene with the addition of clusters, which benefit for charge transfer between the Ni single atom and the O atom. Next, the charge density difference (CDD) of different configurations <span id="page-5-2"></span>was further analyzed (figures [5\(](#page-6-1)e)–(h)). The yellow part indicates increased charge density, and the cyan part indicates decreased charge density. It can be seen intuitively that the number of electrons obtained by the O atom increases with the addition of clusters, which is consistent with the previous results.

<span id="page-6-0"></span><span id="page-6-1"></span>**Figure 4.** (a) The scaling relationship between ∆GOOH\* and ∆GOH\*, (b) the reverse volcano plot of *η*OER with (∆GO\* *−* ∆GOH\*) on NiN4-graphene, NiN4-graphene/Ni4, NiN4-graphene/Ni<sup>13</sup> and NiN4-graphene/Ni (111).

**Figure 5.** The 2D slices projected along direction of electron localization function (ELF) and the charge density difference (CDD) diagram (yellow: electron accumulation, cyan: electron depletion and the iso-surface levels are 0.0009e Å*<sup>−</sup>*<sup>3</sup> ) of NiN4-graphene (a), (e), NiN4-graphene/Ni<sup>4</sup> (b), (f), NiN4-graphene/Ni<sup>13</sup> (c), (g), NiN4-graphene/Ni (111) (d), (h).

*3.3.2. PDOS analysis.* Figures [6\(](#page-7-0)a)–(d) shows the density of states without oxygen intermediate adsorption, while figures [6](#page-7-0)(e)–(h) shows the density of states after oxygen adsorption. As shown in figures [6](#page-7-0)(a)–(d), in comparison with NiN4-graphene, the peaks gradually move to the Fermi level after the addition of clusters and Ni (111). This means that the electrons from the clusters and Ni (111) have filled the empty orbit of the Ni single atom. As a result, more electrons are involved in the reaction, which is beneficial for the reaction. As shown in figures [6](#page-7-0)(e)–(h), the interaction between the Ni single atom and the O atom was further explore. From figure (e), it can be seen that the Ni single atom has partially empty orbitals near the Fermi level, while the state densities of the O atom and the Ni single atom overlap less from *−*2 eV to 2 eV, which means that the hybridization between the O atom and the Ni single atom is weak, i.e., the NiN4-graphene has a weak adsorption to the O atom. For figures (f)–(h), the empty orbitals of the Ni single atom near the Fermi level are significantly decreased, while the overlap of state densities of the O

atom and the Ni single atom increases remarkable from *−*2 eV to 2 eV, indicating that the hybridization between the O atom and the Ni single atom is enhanced. In general, the electrons provided by the cluster filled the empty orbitals of the Ni single atom, which is beneficial for electron transfer between the Ni single atom and the O atom, thus enhancing the hybridization interaction between the O-p orbitals and the Ni-*d* orbitals, ultimately optimizing the adsorption and improving the catalytic activity.

*3.3.3. COHP analysis.* To further explore the interaction between the Ni single atom and the O atom, the projection orbit Hamiltonian distribution (COHP) calculation was conducted [[30,](#page-9-4) [31](#page-9-5)], as shown in figure [7.](#page-7-1) The right side of the curve represent bonding contribution, the left curves are the antibonding contribution. The bonding and anti-bonding contribution of the four simulation models are under the Fermi level for the spin-up part, so the spin-down part was analyzed. There is an anti-bonding contribution to the occupied states

<span id="page-7-0"></span><span id="page-7-1"></span>**Figure 6.** The density of states of Ni single atom before and after O\* adsorption on the NiN<sub>4</sub>-graphene (a), (e), NiN<sub>4</sub>-graphene/Ni<sub>4</sub> (b), (f), NiN<sub>4</sub>-graphene/Ni<sub>13</sub> (c), (g) and NiN<sub>4</sub>-graphene/Ni (111) (d), (h), respectively.

Figure 7. The COHP diagrams of (a)  $NiN_4$ -graphene, (b)  $NiN_4$ -graphene/ $Ni_4$ , (c)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $Ni_{13}$  and (d)  $NiN_4$ -graphene/ $NiN_4$  and (d)  $NiN_4$ -graphene/ $NiN_4$  and (d)  $NiN_4$ -graphene/ $NiN_4$  and (d)  $NiN_4$ -graphene/ $NiN_4$  and (d)  $NiN_4$ -graphene/ $NiN_4$  and (d)  $NiN_4$ -graphene/ $NiN_4$  an

below the Fermi level of the NiN<sub>4</sub>-graphene, indicating that the interaction between the Ni single atom and the O atom is weak, however, the anti-bonding contribution move up slightly in the NiN<sub>4</sub>-graphene/Ni<sub>4</sub>, NiN<sub>4</sub>-graphene/Ni<sub>13</sub> and NiN<sub>4</sub>graphene/Ni (111), indicating an enhanced interaction. The integral value ICOHP for the part below the Fermi level can be understood as the number of bonded electrons shared between two atoms. To some extent, a larger negative integral value leads to a stronger bond strength. As shown in figure 7, the ICOHP values of the four configurations are -2.21, -3.41, -3.40, and -2.35 respectively, indicating that the Ni-O bond strength is enhanced due to the interaction between Ni single atom and Ni cluster. Next, the contribution of bond formation was analyzed by suborbital COHP. As shown in table 1, the contribution of  $3d_{yz}$  and  $3d_{xz}$  in the remaining configurations is improved compared to the NiN4-graphene. It further illustrates that the enhanced hybridization as mentioned in the 3.3.2 originates from the hybrid interactions between the O-p orbitals and Ni- $d_{xz}$ , Ni- $d_{yz}$  orbitals.

<span id="page-7-2"></span>**Table 1.** The IpCOHP values of the  $O_p$  tracks bonded to the d-orbits of Ni in the four simulation models.

| Species/IPCOHP                              | $O_p > Ni-d_{yz}$ | $O_p > Ni-d_z^2$ | $O_p > Ni-d_{xz}$ |
|---------------------------------------------|-------------------|------------------|-------------------|
| NiN <sub>4</sub> -graphene                  | -0.39             | -0.75            | -0.18             |
| NiN <sub>4</sub> -graphene/Ni <sub>4</sub>  | -0.53             | -0.72            | -0.71             |
| NiN <sub>4</sub> -graphene/Ni <sub>13</sub> | -0.51             | -0.75            | -0.71             |
| NiN <sub>4</sub> -graphene/Ni (111)         | -0.42             | -0.75            | -0.47             |

#### 4. Conclusion

In summary, the modulation effects of Ni clusters on the NiN<sub>4</sub>-graphene are comparatively studied using the first-principles calculations based on DFT. It is found that the OER activity of NiN<sub>4</sub>-graphene can be significantly enhanced by the addition of clusters. Electronic properties calculations showed that the charge transfer from Ni clusters to NiN<sub>4</sub>-graphene increases the density of states of the Ni single atom near the Fermi level,

which promotes the charge transfer from the Ni single atom to the O atom, and thus enhances the hybridization interaction between the O atom and the Ni single atom below the Fermi level. In addition, the COHP result further indicates that this enhanced interaction originates from the hybridization of O-p orbitals with Ni-d*xz* and Ni-d*yz* orbitals, which optimizes the adsorption free energy of O atom on Ni-doped graphene and reduces the reaction barrier of OH*<sup>∗</sup> →* O *∗* , ultimately leading to an enhanced OER activity. This work provides a deep understanding on the synergistic catalysis between the cluster and metal atoms embedded into carbon matrix.

## **Data availability statement**

All data that support the findings of this study are included within the article (and any supplementary files).

# **Acknowledgments**

This work was financially supported by the National Natural Science Foundation of China (Nos. 11874141, 11904084, U1804130 and U2004212), the Henan Overseas Expertise Introduction Center for Discipline Innovation (CXJD2019005), the China Postdoctoral Science Foundation (2021M690933) and the National Natural Science Foundation of China (NSFC) (12264055). The simulations are performed on resources provided by the High Performance Computing Center of Henan Normal University.

# **ORCID iD**

Zongxian Yang <https://orcid.org/0000-0002-3015-3804>

# **References**

- <span id="page-8-0"></span>[1] Zhou Y, Gao G, Li Y, Chu W and Wang L W 2019 Transition-metal single atoms in nitrogen-doped graphenes as efficient active centers for water splitting: a theoretical study *Phys. Chem. Chem. Phys.* **[21](https://doi.org/10.1039/C8CP06755D)** [3024](https://doi.org/10.1039/C8CP06755D)
- <span id="page-8-18"></span>[2] Zhao X and Pei Y 2021 Single metal atom supported on N-Doped 2D nitride black phosphorus: an efficient electrocatalyst for the oxygen evolution and oxygen reduction reactions *J. Phys. Chem.* C **[125](https://doi.org/10.1021/acs.jpcc.1c02193)** [12541](https://doi.org/10.1021/acs.jpcc.1c02193)
- <span id="page-8-20"></span>[3] Niu H, Wan X, Wang X, Shao C R, Robertson J, Zhang Z and Guo Y 2021 Single-atom rhodium on defective g-C3N4: a promising bifunctional oxygen electrocatalyst *ACS Sustain. Chem. Eng.* **[9](https://doi.org/10.1021/acssuschemeng.0c09192)** [3590](https://doi.org/10.1021/acssuschemeng.0c09192)
- [4] Li J 2022 Oxygen evolution reaction in energy conversion and storage: design strategies under and beyond the energy scaling relationship *Nanomicro Lett.* **[14](https://doi.org/10.1007/s40820-022-00857-x)** [112](https://doi.org/10.1007/s40820-022-00857-x)
- [5] Gao C, Rao D, Yang H, Yang S, Ye J J, Yang S K, Zhang C, Zhou X, Jing T and Yan X H 2021 Dual transition-metal atoms doping: an effective route to promote the ORR and OER activity on MoTe<sup>2</sup> *New J. Chem.* **[45](https://doi.org/10.1039/D0NJ05606E)** [5589](https://doi.org/10.1039/D0NJ05606E)
- <span id="page-8-1"></span>[6] Deng Q, Zhao J, Wu T, Chen G, Hansen H A and Vegge T 2019 2D transition metal–TCNQ sheets as bifunctional single-atom catalysts for oxygen reduction and evolution reaction (ORR/OER) *J. Catal.* **[370](https://doi.org/10.1016/j.jcat.2018.12.012)** [378](https://doi.org/10.1016/j.jcat.2018.12.012)
- <span id="page-8-2"></span>[7] Song J, Wei C, Huang Z F, Liu C, Zeng L, Wang X and Xu Z J 2020 A review on fundamentals for designing oxygen evolution electrocatalysts *Chem. Soc. Rev.* **[49](https://doi.org/10.1039/C9CS00607A)** [2196](https://doi.org/10.1039/C9CS00607A)

- <span id="page-8-3"></span>[8] Zhao C X, Li B Q, Liu J N and Zhang Q 2021 Intrinsic electrocatalytic activity regulation of M-N-C single-atom catalysts for the oxygen reduction reaction *Angew. Chem., Int. Ed. Engl.* **[60](https://doi.org/10.1002/anie.202003917)** [4448](https://doi.org/10.1002/anie.202003917)
- <span id="page-8-5"></span>[9] Miao Z *et al* 2021 Improving the stability of non-noble-metal M-N-C catalysts for proton-exchange-membrane fuel cells through M-N bond length and coordination regulation *Adv. Mater.* **[33](https://doi.org/10.1002/adma.202006613)** [e2006613](https://doi.org/10.1002/adma.202006613)
- <span id="page-8-4"></span>[10] Martinez U, Komini Babu S, Holby E F, Chung H T, Yin X and Zelenay P 2019 Progress in the development of Fe-based PGM-free electrocatalysts for the oxygen reduction reaction *Adv. Mater.* **[31](https://doi.org/10.1002/adma.201806545)** [e1806545](https://doi.org/10.1002/adma.201806545)
- [11] Tang T, Wang Z and Guan J 2022 Optimizing the electrocatalytic selectivity of carbon dioxide reduction reaction by regulating the electronic structure of single-atom M-N-C materials *Adv. Funct. Mater.* **[32](https://doi.org/10.1002/adfm.202111504)** [2111504](https://doi.org/10.1002/adfm.202111504)
- <span id="page-8-6"></span>[12] Wu H, Wu J, Li Y, Li W, Zhai J, Jiang Q, Xu X and Gao Y 2022 Enhanced oxygen reduction with carbon-polyhedron-supported discrete cobalt-nitrogen sites for Zn-air batteries *Chem. Eng. J.* **[431](https://doi.org/10.1016/j.cej.2021.134084)** [134084](https://doi.org/10.1016/j.cej.2021.134084)
- <span id="page-8-7"></span>[13] Zhang X, Yang Z, Lu Z and Wang W 2018 Bifunctional CoNx embedded graphene electrocatalysts for OER and ORR: a theoretical evaluation *Carbon* **[130](https://doi.org/10.1016/j.carbon.2017.12.121)** [112](https://doi.org/10.1016/j.carbon.2017.12.121)
- <span id="page-8-8"></span>[14] Liu J, Xiao J, Luo B, Tian E and Waterhouse G I N 2022 Central metal and ligand effects on oxygen electrocatalysis over 3d transition metal single-atom catalysts: a theoretical investigation *Chem. Eng. J.* **[427](https://doi.org/10.1016/j.cej.2021.132038)** [132038](https://doi.org/10.1016/j.cej.2021.132038)
- <span id="page-8-9"></span>[15] Zhang H, Liu Y, Chen T, Zhang J, Zhang J and Lou X W 2019 Unveiling the activity origin of electrocatalytic oxygen evolution over isolated Ni atoms supported on a N-doped carbon matrix *Adv. Mater.* **[31](https://doi.org/10.1002/adma.201904548)** [1904548](https://doi.org/10.1002/adma.201904548)
- <span id="page-8-10"></span>[16] Li H, He Y, Yang Q, Wang J, Yan S, Chen C and Chen J 2019 Urchin-like Ni@N-doped carbon composites with Ni nanoparticles encapsulated in N-doped carbon nantubes as high-efficient electrocatalyst for oxygen evolution reaction *J. Solid State Chem.* **[278](https://doi.org/10.1016/j.jssc.2019.07.004)** [120843](https://doi.org/10.1016/j.jssc.2019.07.004)
- [17] Zhou X *et al* 2020 Highly-dispersed cobalt clusters decorated onto nitrogen-doped carbon nanotubes as multifunctional electrocatalysts for OER, HER and ORR *Carbon* **[166](https://doi.org/10.1016/j.carbon.2020.05.037)** [284](https://doi.org/10.1016/j.carbon.2020.05.037)
- <span id="page-8-11"></span>[18] Wu S *et al* 2023 Confined synthesis of highly dispersed Ni anchored on mesoporous carbon as efficient catalyst for water splitting *Mol. Catal.* **[548](https://doi.org/10.1016/j.mcat.2023.113473)** [113473](https://doi.org/10.1016/j.mcat.2023.113473)
- <span id="page-8-12"></span>[19] Han H, Chao S, Yang X, Wang X, Wang K, Bai Z and Yang L 2017 Ni nanoparticles embedded in N doped carbon nanotubes derived from a metal organic framework with improved performance for oxygen evolution reaction *Int. J. Hydrog. Energy* **[42](https://doi.org/10.1016/j.ijhydene.2017.05.043)** [16149](https://doi.org/10.1016/j.ijhydene.2017.05.043)
- <span id="page-8-13"></span>[20] Liu Y, Jiang H, Zhu Y, Yang X and Li C 2016 Transition metals (Fe, Co, and Ni) encapsulated in nitrogen-doped carbon nanotubes as bi-functional catalysts for oxygen electrode reactions *J. Mater. Chem.* A **[4](https://doi.org/10.1039/C5TA10551J)** [1694](https://doi.org/10.1039/C5TA10551J)
- <span id="page-8-14"></span>[21] Zhang X, Feng S, Yu J, Shi R, Ma Z, Yang Z and Yang L 2022 Tuning d orbital of Ni single atom by encapsulating Ni nanoparticle in carbon nanotube for efficient oxygen evolution reaction *Energy Fuels* **[36](https://doi.org/10.1021/acs.energyfuels.2c02644)** [13159](https://doi.org/10.1021/acs.energyfuels.2c02644)
- <span id="page-8-15"></span>[22] Torrent M, Holzwarth N A W, Jollet F, Harris D, Lepley N and Xu X 2010 Electronic structure packages: two implementations of the projector augmented wave (PAW) formalism *Comput. Phys. Commun.* **[181](https://doi.org/10.1016/j.cpc.2010.07.036)** [1862](https://doi.org/10.1016/j.cpc.2010.07.036)
- <span id="page-8-16"></span>[23] Kresse G and Furthmüller J 1996 Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set *Phys. Rev.* B **[54](https://doi.org/10.1103/PhysRevB.54.11169)** [11169](https://doi.org/10.1103/PhysRevB.54.11169)
- <span id="page-8-17"></span>[24] Perdew J P, Burke K and Ernzerhof M 1996 Generalized gradient approximation made simple *Phys. Rev. Lett.* **[77](https://doi.org/10.1103/PhysRevLett.77.3865)** [3865](https://doi.org/10.1103/PhysRevLett.77.3865)
- <span id="page-8-19"></span>[25] Han X, Benkraouda M, Qamhieh N and Amrane N 2020 Understanding ferromagnetism in Ni-doped MoS<sup>2</sup> monolayer from first principles *Chem. Phys.* **[528](https://doi.org/10.1016/j.chemphys.2019.110501)** [110501](https://doi.org/10.1016/j.chemphys.2019.110501)

- <span id="page-9-0"></span>[26] Peng Y, Hajiyani H and Pentcheva R 2021 Influence of Fe and Ni doping on the OER performance at the Co<sub>3</sub>O<sub>4</sub>(001) surface: insights from DFT+U calculations ACS Catal. 11 5601
- <span id="page-9-1"></span>[27] Duraisamy P D, Prince Makarios Paul S, Gopalan P and Angamuthu A 2022 Feasibility of halide (F-, Cl- and Br-) encapsulated Be<sub>12</sub>O<sub>12</sub> nanocages as potential anode for metal-ion batteries—A DFT-D3 approach *Mater. Sci. Semicond. Process.* 147 106719
- <span id="page-9-2"></span>[28] Bakhshi F and Farhadian N 2018 Co-doped graphene sheets as a novel adsorbent for hydrogen storage: DFT and DFT-D3 correction dispersion study *Int. J. Hydrog. Energy* 43 8355
- <span id="page-9-3"></span>[29] Zhu G, Liu F, Wang Y, Wei Z and Wang W 2019 Systematic exploration of N,C coordination effects on the ORR performance of Mn-N(x) doped graphene catalysts based on DFT calculations *Phys. Chem. Chem. Phys.* 21 12826
- <span id="page-9-4"></span>[30] Nelson R, Ertural C, George J, Deringer V L, Hautier G and Dronskowski R 2020 LOBSTER: local orbital projections, atomic charges, and chemical-bonding analysis from projector-augmented-wave-based density-functional theory J. Comput. Chem. 41 1931
- <span id="page-9-5"></span>[31] Deringer V L, Tchougreeff A L and Dronskowski R 2011 Crystal orbital Hamilton population (COHP) analysis as projected from plane-wave basis sets *J. Phys. Chem.* A 115 5461
- <span id="page-9-6"></span>[32] Rossmeisl J, Qu Z W, Zhu H, Kroes G J and Nørskov J K 2007 Electrolysis of water on oxide surfaces J. Electroanal. Chem. 607 83
- <span id="page-9-7"></span>[33] Nørskov J K, Rossmeisl J, Logadottir A, Lindqvist L, Kitchin J R, Bligaard T and Jónsson H 2004 Origin of the

- overpotential for oxygen reduction at a fuel-cell cathode *J. Phys. Chem.* A **108** 17886
- <span id="page-9-8"></span>[34] Mao X, Kour G, Yan C, Zhu Z and Du A 2019 Single transition metal atom-doped graphene supported on a nickel substrate: enhanced oxygen reduction reactions modulated by electron coupling *J. Phys. Chem.* C 123 3703
- <span id="page-9-9"></span>[35] Yang H, Luo D, Gao R, Wang D, Li H, Zhao Z, Feng M and Chen Z 2021 Reduction of N<sub>2</sub> to NH<sub>3</sub> by TiO<sub>2</sub>-supported Ni cluster catalysts: a DFT study *Phys. Chem. Chem. Phys.* 23 16707
- [36] Xu H, Chu W, Sun W, Jiang C and Liu Z 2016 DFT studies of Ni cluster on graphene surface: effect of CO<sub>2</sub> activation RSC Adv. 6 96545
- [37] Reuse F A, Khanna S N and Bernel S 1995 Electronic structure and magnetic behavior of Ni1<sub>3</sub> clusters *Phys. Rev.* B 52 11650
- <span id="page-9-10"></span>[38] Piotrowski M J, Piquini P and Da Silva J L F 2010 Density functional theory investigation of 3d, 4d, and 5d 13-atom metal clusters *Phys. Rev.* B 81 155446
- <span id="page-9-11"></span>[39] Kattel S, Atanassov P and Kiefer B 2014 A density functional theory study of oxygen reduction reaction on non-PGM Fe-Nx-C electrocatalysts *Phys. Chem. Chem. Phys.* 16 13800
- <span id="page-9-12"></span>[40] Zhang X, Wang W and Yang Z 2020 CO<sub>2</sub> reduction on metaland nitrogen-codoped graphene: balancing activity and selectivity via coordination engineering ACS Sustain. Chem. Eng. 8 6134
- <span id="page-9-13"></span>[41] Ma Z, Zhang X, Wu D, Han X, Zhang L, Wang H, Xu F, Gao Z and Jiang K 2020 Ni and nitrogen-codoped ultrathin carbon nanosheets with strong bonding sites for efficient CO<sub>(2)</sub> electrochemical reduction *J. Colloid Interface Sci.* 570 31