---
source: Wang 等 - 2022 - Two-dimensional metal–organic frameworks as efficient electrocatalysts for bifunctional oxygen evolu.pdf
tool: marker
duration: 70.917s
generated: 2026-01-09T08:07:15.280185Z
---

# Journal of Materials Chemistry A

**PAPER** 

View Article Online
View Journal | View Issue

Cite this: J. Mater. Chem. A, 2022, 10, 13005

# Two-dimensional metal—organic frameworks as efficient electrocatalysts for bifunctional oxygen evolution/reduction reactions†

Anyang Wang, Da Huan Niu, Da Xiting Wang, Da Xuhao Wan, Da Liu Xie, Laofu Zhang, Dc Jun Wang D\*\* and Yuzheng Guo D\*\*

With the continuous development of sustainable and renewable energy, the electrocatalytic water cycle and rechargeable metal—air batteries are attracting increasing attention. As two main reactions, oxygen evolution/reduction reactions (OER/ORR) require highly efficient bifunctional electrocatalysts. Herein, by first-principles calculations, we have systematically investigated the OER and ORR performance for a new class of two-dimensional (2D) metal—organic frameworks (MOFs)  $M_3(C_6S_6)_2$ , with M including Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ir, and Pt. It is demonstrated that  $Rh_3(C_6S_6)_2$  possesses promising bifunctional OER/ORR activity, with calculated overpotentials of 0.43 and 0.42 V for the OER and ORR, respectively. Moreover, the volcano plots and contour maps regarding activity vs. intermediate adsorption strength are established to describe the activity trends of the OER and ORR for  $M_3(C_6S_6)_2$ . A combination of the d-band center and crystal orbital Hamilton populations (COHPs) is employed to correlate the activity and electronic structure of the catalyst. The catalytic origin of OER and ORR activities can be ascribed to the simple d-electron number of the central metal of  $M_3(C_6S_6)_2$ . Our findings not only provide cost-effective bifunctional oxygen electrocatalysts but also offer important insights into advancing clean energy technology.

Received 17th February 2022 Accepted 23rd May 2022

DOI: 10.1039/d2ta01319c

rsc.li/materials-a

## 1. Introduction

With the global environmental problems becoming increasingly serious, searching for efficient, clean, and renewable energy sources to replace fossil fuels has gradually become a research hotspot.<sup>1-3</sup> The electrocatalytic water cycle and rechargeable metal–air batteries are considered to be promising approaches to conversion and storage technology for renewable energy.<sup>4-7</sup> However, the oxygen evolution reaction (OER) and oxygen reduction reaction (ORR), as the two core reactions in the electrocatalytic water cycle and charge and discharge processes of metal–air batteries, suffer from serious sluggish kinetics, which heavily hampers the application and development of metal–air batteries.<sup>8</sup>

Some traditional noble metals or their oxide catalysts, such as Pt and  $RuO_2$ , can reduce the ORR overpotential to 0.45 V and the OER overpotential to 0.42 V, respectively. However, due to their high cost, instability, and poor selectivity, their practical utilization has been severely hampered and limited. More

importantly, as two reciprocal oxygen-related reactions, a catalyst that exhibits superior ORR activity may have poor catalytic performance for the OER, and *vice versa*.<sup>11</sup> Due to the different working conditions of the two separate unifunctional catalysts, the performance of the bifunctional catalysts for overall water splitting is always better than that of the ensemble of the two unifunctional catalysts, and besides, the bifunctional catalysts can make the rechargeable metal–air battery devices much simpler.<sup>12,13</sup> Therefore, designing stable, low cost and highefficiency bifunctional catalysts for both the ORR and OER is the key to realizing the large-scale application of the electrocatalytic water cycle and rechargeable metal–air batteries and meanwhile solving the environmental pollution problem.<sup>14-18</sup>

Metal-containing macromolecular materials have been widely used in the field of catalysis. 19-21 Single metal atoms supported on different substrates can show different catalytic activities and often show unique selectivity different from that of nanoparticle catalysts. 22 Among them, 2D metal-organic frameworks (2D-MOFs), composed of metal ions and organic ligands through strong coordination bonds, have greatly inspired the application prospects of single-atom catalysis due to their unique properties, such as high surface areas, adjustable microstructures, highly disperse active sites and hierarchical porous structures. 23-26 Their high surface area always results in plenty of active sites, and the diverse geometry of metal-ligand centers can lead to adjustable electronic

<sup>&</sup>quot;School of Electrical Engineering and Automation, Wuhan University, Wuhan, Hubei 430072, China. E-mail: junwangszu@163.com; yguo@whu.edu.cn

<sup>&</sup>lt;sup>b</sup>Yangtze Memory Technologies Co., Ltd., Wuhan, Hubei 430074, China

Department of Engineering, Cambridge University, Cambridge, CB2 1PZ, UK

<sup>†</sup> Electronic supplementary information (ESI) available. See https://doi.org/10.1039/d2ta01319c

structures and catalytic performance. Meanwhile, their hierarchical porous structure and dispersed sites would provide efficient channels for ion diffusion in solution and thus high metal atom utilization.<sup>27</sup> Nevertheless, their atomic scale pores also bring forth a negative impact on the electrical conductivity of materials, endowing most 2D-MOFs with unsatisfactory electron transfer capability. As a result, the low electrical conductivity becomes a key obstacle that 2D-MOFs need to overcome.<sup>28,29</sup>

In recent years, a novel 2D-MOF named M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> has emerged and has been successfully synthesized. 30-32 M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub>, belonging to the  $M_3(C_6X_6)_2$  (X = NH, O, S) family, bears a metal bis(dithiolene) complex structure, whose outstanding electrical conductivity has been validated both theoretically and experimentally, endowing it with great potential as a catalyst in electrochemical reactions.33-39 Bohayra Mortazavi and co-workers confirmed that  $M_3(C_6X_6)_2$  (X = O, S, Se) is thermally stable at high temperatures over 1500 K by first-principles calculations.<sup>38</sup> Recently, Zhang and co-workers40 found that the interaction strength between the reaction intermediates and the metal complex (MO<sub>4</sub>) sites can be modulated by changing the metal centers to those with different d-electron occupations. This can further affect the catalytic performance of M<sub>3</sub>(C<sub>6</sub>O<sub>6</sub>)<sub>2</sub> in ORR electrocatalysis. Considering that S belongs to the same group as O but shows lower electronegativity, different electronic states of M will be induced in  $M_3(S_6O_6)_2$  and thus lead to distinct OER and ORR performance, which has not been studied yet.

In this work, by using density functional theory (DFT) calculations, we have systematically studied  $M_3(C_6S_6)_2$  (M=Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ir,orPt) as potential ORR and OER catalysts. The highlights of our original contributions in this paper are shown below. First, we have evaluated the stability as well as the OER and ORR activities of different  $M_3(C_6S_6)_2$  catalysts, respectively. Next, the trend of catalytic activity on  $M_3(C_6S_6)_2$  has been clarified by volcano plots and contour maps, which predict not only the optimal activity but also the potential-determining steps (PDSs) of the OER and ORR respectively. Last but not least, the origin of catalytic activity of the OER and ORR has been related to the simple delectron number of the central metal of  $M_3(C_6S_6)_2$  by using electronic structure analysis.

# 2. Computational methods

Spin-polarized density functional theory was employed as implemented in the Vienna *Ab initio* Simulation Package (VASP).<sup>41,42</sup> The projector-augmented wave (PAW) potentials were employed to describe the interactions between ions and electrons.<sup>43</sup> The generalized gradient approximation (GGA) in the form of the Perdew–Burke–Ernzerhof (PBE) functional was adopted to describe the exchange–correlation energy.<sup>44</sup> A vacuum space of 20 Å was set to avoid the interaction between two  $M_3(C_6S_6)_2$  sheets. The convergence threshold was set to  $10^{-5}$  eV and 0.02 eV Å<sup>-1</sup> for energy and force, respectively. The plane-wave cutoff energy was set to 520 eV, and a  $2 \times 2 \times 1$  k-point sampling was adopted. The long-range van der Waals interactions were described by the DFT-D3 method using

dispersion correction in Grimme's scheme.<sup>45</sup> The charge transfer was analyzed by Bader charge analysis.<sup>46</sup>

The OER process has been reported to be composed of fourelectron steps in the acidic solution (pH=0).<sup>47,48</sup> First, a water molecule is decomposed by  $M_3(C_6S_6)_2$  (denoted as \*) into one  $(H^+ + e^-)$  pair and \*OH. And then, the \*OH intermediate dissociates into \*O with the release of one  $(H^+ + e^-)$  pair. Next, \*O reacts with another water molecule to form \*OOH and releases an  $(H^+ + e^-)$  pair. Finally, the \*OOH dissociates into  $O_2$ , producing another  $(H^+ + e^-)$  pair. The overall and four elementary reactions can be expressed as eqn (1)–(5).

$$2H_2O \rightarrow O_2 + 4e^- + 4H^+$$
 (1)

\* + 
$$H_2O \rightarrow *OH + (H^+ + e^-)$$
 (2)

$$*OH \rightarrow *O + (H^{+} + e^{-})$$
 (3)

$$*O + H_2O \rightarrow *OOH + (H^+ + e^-)$$
 (4)

\*OOH 
$$\rightarrow$$
 \* + O<sub>2</sub> + (H<sup>+</sup> + e<sup>-</sup>) (5)

where \* denotes the  $M_3(C_6S_6)_2$  substrate. Correspondingly, the free energy changes of the four elementary steps can be calculated using eqn (6)–(9).

$$\Delta G_1 = \Delta G_{*\mathrm{OH}} \tag{6}$$

$$\Delta G_2 = \Delta G_{*O} - \Delta G_{*OH} \tag{7}$$

$$\Delta G_3 = \Delta G_{*OOH} - \Delta G_{*O} \tag{8}$$

$$\Delta G_4 = 4.92 - \Delta G_{*OOH} \tag{9}$$

where  $\Delta G_{*OH}$ ,  $\Delta G_{*O}$ , and  $\Delta G_{*OOH}$  represent the adsorption free energies of \*OH, \*O, and \*OOH, respectively, which can be defined as eqn (10)–(12).

$$\Delta G_{*OH} = G_{*OH} - G_* - (G_{H,O} - 1/2G_{H,O}) \tag{10}$$

$$\Delta G_{*O} = G_{*O} - G_* - (G_{H,O} - G_{H_*}) \tag{11}$$

$$\Delta G_{*OOH} = G_{*OOH} - G_* - (2G_{H_2O} - 3/2G_{H_2})$$
 (12)

where the  $G_*$ ,  $G_{*OH}$ ,  $G_{*O}$ , and  $G_{*OOH}$  represent the free energies of \*, \*OH, \*O, and \*OOH, respectively.  $G_{\rm H_2O}$  and  $G_{\rm H_2}$  represent the free energies of  $\rm H_2O$  and  $\rm H_2$  molecules, respectively. The Gibbs free energy (G) can be calculated using eqn (13).<sup>49</sup>

$$\Delta G = \Delta E + \Delta Z P E - T \Delta S + \Delta G_U \tag{13}$$

where E is the total energy calculated by DFT. ZPE is zero-point energy, which can be calculated from vibration frequency. T is temperature, and S is standard entropy. For an intermediate adsorbed on a surface,  $\Delta S$  is specified as zero.  $\Delta G_U = -n_e U$ , which is the contribution of the electrode potential to  $\Delta G$ . According to the computational hydrogen electrode (CHE) method, half of the free energy of the  $H_2$  molecule at 298 K is used to replace the energy of  $(H^+ + e^-)$ , and the free energy of  $O_2$ 

was indirectly calculated on the basis of the overall energy change (4.92 eV) due to the difficulty in accurately describing its total energy by DFT.

The OER overpotential  $(\eta_{OER})$  is used to measure the OER catalytic performance. A smaller  $\eta_{\rm OER}$  represents a better OER activity.

$$\eta_{\text{OER}} = \max(\Delta G_1, \Delta G_2, \Delta G_3, \Delta G_4)/e - 1.23 \tag{14}$$

where  $\Delta G_n$  (n=1–4) is the free energy change of each elementary reaction step.

As the reverse reaction of the OER, the ORR overpotential  $(\eta_{\rm ORR})$  can be similarly written as eqn (15). A smaller  $\eta_{\rm ORR}$ represents a better ORR activity.

$$\eta_{\text{ORR}} = \max(-\Delta G_1, -\Delta G_2, -\Delta G_3, -\Delta G_4)/e + 1.23$$
(15)

#### 3. Results and discussion

# 3.1. Stability of $M_3(C_6S_6)_2$

As shown in Fig. 1a and S1,†  $M_3(C_6S_6)_2$  possesses a hexagonal lattice, which is composed of planar square MS<sub>4</sub> ligands attached to a benzene ring. Consequently, a unit cell of M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> consists of two benzene rings and four MS<sub>4</sub> fragments. To screen out expected catalysts from  $M_3(C_6S_6)_2$  groups, different central metals M varying from V to Pt have been adopted to construct the catalyst models (Fig. 1a).

The stability of catalysts is an essential requirement for practical application. In this work, the thermodynamic stability of  $M_3(C_6S_6)_2$  is evaluated from formation energy ( $E_{form}$ ). Herein, the  $E_{\text{form}}$  is defined as  $E_{\text{form}} = E_{\text{M3}(C_6S6)_2} - 2E_{C_6S_6H_6} - 3E_{\text{M-bulk}}/N +$  $12E_{\rm H}$ , where  $E_{\rm M3(C_cS_c)_a}$ ,  $E_{\rm C_cS_cH_c}$ , and  $E_{\rm M-bulk}$  are the total energies of  $M_3(C_6S_6)_2$ ,  $C_6S_6H_6$ , and the metal bulk, respectively. N represents the number of metal atoms in the bulk. A more negative  $E_{\text{form}}$  corresponds to higher stability of the catalyst,

Fig. 1 (a) Illustration of  $M_3(C_6S_6)_2$  with different transition metals (TM) varying from V to Pt. (b) The formation energy of  $M_3(C_6S_6)_2$ . (c) Charge transfer between the metal atom and  $C_6S_6$ . (d) Band structure of  $Rh_3(C_6S_6)_2$ 

and a stable M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> structure should satisfy the criterion  $E_{\text{form}} > 0$ . Fig. 1b shows the formation energies of  $M_3(C_6S_6)_2$  with the different central metals. In addition, the dissolution potentials  $(U_{\text{diss}} = U_{\text{diss-bulk}} - E_{\text{form}}/(eN_e))$  of M atoms on  $M_3(C_6S_6)_2$  are explored to investigate the stability of  $M_3(C_6S_6)_2$ under the electrochemical conditions. $^{50,51}$   $U_{\rm diss-bulk}$  and  $N_{\rm e}$ represent the standard dissolution potentials of M bulk and the number of electrons transferred during the dissolution process, respectively. As seen in Fig. S2,† a thermodynamically and electrochemically stable M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> should satisfy the criteria of  $E_{\text{form}} < 0 \text{ eV}$  and  $U_{\text{diss}} > 0 \text{ V}$ , simultaneously. Obviously,  $Cu_3(C_6S_6)_2$ ,  $Nb_3(C_6S_6)_2$ ,  $Mo_3(C_6S_6)_2$   $Tc_3(C_6S_6)_2$  and  $Ru_3(C_6S_6)_2$ suffer from the thermodynamical problem due to their positive  $E_{\text{form}}$ . Additionally,  $V_3(C_6S_6)_2$  and  $Mn_3(C_6S_6)_2$  are excluded in terms of the electrochemical stability because they cannot satisfy the criterion  $U_{\text{diss}} > 0$  V. The detailed  $E_{\text{form}}$  and  $U_{\text{diss}}$  are listed in Table S1.†

Furthermore, the AIMD simulation at 300 K for 10 ps has been performed taking  $Rh_3(C_6S_6)_2$  and  $Fe_3(C_6S_6)_2$  as examples to illustrate the dynamic stability of M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub>. Rh<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> is the bifunctional catalyst with the best performance among  $M_3(C_6S_6)_2$  catalysts, while  $Fe_3(C_6S_6)_2$  just locates around the critical point of the criteria of  $E_{\text{form}} < 0$  eV and  $U_{\text{diss}} > 0$  V. Fig. S3a and b† indicate that the temperature and energy of Rh<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> and Fe<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> oscillate in a small range during AIMD simulation, which further illustrates the thermal stability of M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub>. The experimental results showing that Fe<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> and Ni<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> have been successfully synthesized can firmly support the conclusion.31,32,35 It should be noted that these unstable structures will still be included in catalyst trend investigation to maintain the continuous variation of the electronic structure of the metal center.

Fig. 1c shows the charge transfer between the metal atoms and C<sub>6</sub>S<sub>6</sub> ligand for different M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> catalysts which are summarized in Table S2† together with the bond lengths between metal atoms and neighboring S atoms. In all cases, metal atoms bear a positive charge owing to their lower electronegativity than coordinated S atoms. Furthermore, the number of transferred charges decreases with metal varying from left to right in each period, and more charge transfer always leads to stronger ionic bonds. 52,53 This reveals a strong interaction between the metal atom and C<sub>6</sub>S<sub>6</sub>, reflecting the stability of the catalyst structure as well. Moreover, the band structures (Fig. 1d and S4†) without the bandgap of M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> imply their metallic character, which can be ascribed to the effective orbital interactions between the fully conjugated benzene ring and MS4. The outstanding electrical conductivity of  $M_3(C_6S_6)_2$  would benefit OER and ORR processes.

#### OER/ORR performance

To compare the catalytic performance of different M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> catalysts for the OER and ORR, all possible adsorbed oxygenated intermediates (\*OH, \*O, and \*OOH) in the processes were under consideration, and their free energies and adsorption energies are shown in Tables S3-S6.† As the central metal changes from left to right in the same period, the adsorption

Fig. 2 The OER and ORR free energy diagrams of  $M_3(C_6S_6)_2$  with M varying from (a) V to Nb, and (b) from Mo to Pt. The equilibrium 1.23 V is applied at each step of the reaction. (c) The OER and ORR overpotentials of  $M_3(C_6S_6)_2$ .

energy of intermediates tends to increase, which will bring regular influence on the activity of the catalysts. On the basis of the adsorption energies, the free energy diagrams (Fig. 2a and b) of the OER and ORR were obtained by using eqn (6)–(9).

The OER process will proceed in the forward direction (\* +  $H_2O \rightarrow *OH \rightarrow *O \rightarrow *OOH \rightarrow *+O_2$ ), and the ORR process in the backward direction (\* +  $O_2 \rightarrow *OOH \rightarrow *O \rightarrow *OH \rightarrow * +$ H<sub>2</sub>O) as shown in Fig. S5.† As coherent processes, the rate of the whole OER or ORR is always limited by certain elementary reactions called potential determining steps (PDSs) that suffer from the largest free energy change. For instance, in the case of  $Ni_3(C_6S_6)_2$ , the OER is blocked by the step of \*OH  $\rightarrow$  \*O, while the ORR is blocked by the step of  $O_2 \rightarrow *OOH$ . In addition, as the central metal changes in the same period, the free energy change of each step on different M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> catalysts shows a concurrent varying trend. For example, from V<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> to  $Ni_3(C_6S_6)_2$ , the first two steps of the OER process release less and less energy; meanwhile, the last two steps absorb less and less energy. As the reverse process of the OER, the ORR also shows similar trends on different  $M_3(C_6S_6)_2$  catalysts.

According to eqn (14) and (15), the OER/ORR overpotentials of  $M_3(C_6S_6)_2$  were obtained from the free energy change of PDSs, and the corresponding overpotentials of each catalyst are summarized in Fig. 2c and Table S7.† After a full comparison,  $Rh_3(C_6S_6)_2$  exhibits the highest comprehensive performance due to their rather low OER ( $\eta_{OER}=0.43$  V) and ORR overpotentials ( $\eta_{ORR}=0.42$  V), which can be equal to or even lower than that of traditional unifunctional catalysts (such as Pt (0.45 V) and  $RuO_2$  (0.42 V)), rendering it an outstanding bifunctional catalyst. Meanwhile,  $Ir_3(C_6S_6)_2$  and  $Fe_3(C_6S_6)_2$  also show considerably high ORR performance with overpotentials of 0.40 and 0.44 V, respectively, indicating that they are excellent ORR catalysts as well.

#### 3.3. OER/ORR activity trend

The scaling relationship, a ubiquitous phenomenon for oxygenate catalysis, always leads to synchronous adsorption strength variation of oxygenated intermediates on catalysts. Therefore, we have also focused on the adsorption energies of \*OH, \*O, and \*OOH on different  $M_3(C_6S_6)_2$  catalysts, and investigated the relationship among them. As seen in Fig. 3, both  $\Delta G_{^{*}OOH}$  and  $\Delta G_{^{*}O}$  linearly vary with  $\Delta G_{^{*}OH}$ . Their correlation equation can be fitted as  $\Delta G_{^{*}OOH} = 0.84 \Delta G_{^{*}OH} + 3.21 (R^2 = 0.99)$  and  $\Delta G_{^{*}O} = 1.46 \Delta G_{^{*}OH} + 0.74 (R^2 = 0.94)$ , respectively, basically in accordance with other catalytic systems. These relationships would codetermine the free energy change of each elementary step and hence unfortunately limit the catalytic potential of  $M_3(C_6S_6)_2$ .

Based on the scaling relationship, two curves describing  $-\eta_{\rm OER}$  vs.  $\Delta G_{^*{\rm O}} - \Delta G_{^*{\rm OH}}$  and  $-\eta_{\rm ORR}$  vs.  $\Delta G_{^*{\rm OH}}$  are obtained (Fig. 4a and b). Both the activities of the OER and ORR could be divided into two regions, namely the weak and the strong adsorption regions, and a good linear fitting is realized in each region resulting in volcano curves. Each branch of the volcano represents a PDS in the specific adsorption strength range of intermediates. Apparently, for the OER process, the PDSs of weak and strong adsorption regions are step 2 (\*OH  $\rightarrow$  \*O) and step 3 (\*O  $\rightarrow$  \*OOH), respectively, while for ORR process, the PDSs are step 1 (\* + O<sub>2</sub>  $\rightarrow$  \*OOH) and step 4 (\*OH  $\rightarrow$  \* + H<sub>2</sub>O), respectively.

According to the Sabatier principle, both too strong and too weak interactions between the catalyst and adsorbed species will have a negative effect on the catalytic performance. In other words, if the adsorption of reaction intermediates on the catalyst is too strong, the reaction products will be difficult to desorb; conversely, if the adsorption is too weak, the reaction species will be difficult to combine with the catalyst. In such a scenario, a volcano curve regarding catalytic activity *versus* adsorption strength of intermediate would form, and the best catalyst is located at the top. Therefore, for the OER process,  $Rh_3(C_6S_6)_2$  with  $\Delta G_{^*O} - \Delta G_{^*OH}$  (1.30 eV) closest to the summit (1.48 eV) bears the highest activity among all screened catalysts. Similarly, for the ORR process,  $Rh_3(C_6S_6)_2$  with  $\Delta G_{^*OH}$  (1.15 eV) rather close to the summit (0.93 eV) is also considered as one of

Fig. 3 Scaling relations between the adsorption energies of intermediates ( $\Delta G_{^*O}$  vs.  $\Delta G_{^*OH}$  in red;  $\Delta G_{^*OOH}$  vs.  $\Delta G_{^*OH}$  in blue) on  $M_3(C_6S_6)_2$ .

Fig. 4 (a)The volcano plot of the OER on  $M_3(C_6S_6)_2$  with  $-\eta_{OER}$  vs.  $\Delta G_{*O} - \Delta G_{*OH}$ . (b)The volcano plot of the ORR on  $M_3(C_6S_6)_2$  with  $-\eta_{ORR}$  vs.  $\Delta G_{*OH}$ . The PDSs of the OER and ORR are labeled. The contour maps of (c) OER and (d) ORR activity trends on  $M_3(C_6S_6)_2$ , with  $\Delta G_{*OH}$  and  $\Delta G_{*OH}$  and  $\Delta G_{*OH}$  are labeled.  $\Delta G_{*OH}$  as parameters

the best catalysts. The combination of outstanding OER and ORR activities enables Rh<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> to be the best comprehensive bifunctional catalysts among all screened M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> catalysts. In addition, besides Rh<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub>, Ir<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> and Fe<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> also show great potential in ORR catalysis due to their moderate  $\Delta G_{*OH}$ proximal to the summit.

Further, to obtain the PDSs of each M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> and their overpotential distribution region intuitively, two important abovementioned adsorption parameters  $\Delta G_{*\mathrm{OH}}$  and  $\Delta G_{*\mathrm{O}}$  - $\Delta G_{*OH}$  were jointly adopted to describe the activity of the OER or ORR. Specifically, eqn (16)-(19) were obtained by substituting  $\Delta G_{*OOH}$  with  $\Delta G_{*OOH} = 0.84 \Delta G_{*OH} + 3.21$  in eqn (6)-(9), and then the OER activity could be evaluated using  $\Delta G_{*OH}$  and  $\Delta G_{*O}$  $-\Delta G_{*OH}$ .

$$\Delta G_1 = \Delta G_{*OH} \tag{16}$$

$$\Delta G_2 = \Delta G_{*OH} - \Delta G_{*OH} \tag{17}$$

$$\Delta G_3 = -0.16 \ \Delta G_{*OH} - (\Delta G_{*O} - \Delta G_{*OH}) + 3.21$$
 (18)

$$\Delta G_4 = -0.84 \ \Delta G_{*OH} + 1.71 \tag{19}$$

In this case, the activity trend of catalysts can be well described using a contour map. 11,49,56 As shown in Fig. 4c, the four regions separated by dashed lines represent the free energy changes of the four elementary steps of the OER. If a catalyst falls in a certain region, the step of the region will be the

corresponding PDS. For early transition metals, such as V, Cr, Nb, and Mo, their rather low  $\Delta G_{*O} - \Delta G_{*OH}$  makes the PDSs of most of them fall in the step 3 (\*O  $\rightarrow$  \*OOH) region. As the metal gradually changes to late transition metals, such as Pd and Ni, the PDSs changed to step 2 (\*OH  $\rightarrow$  \*O) correspondingly accompanying the increase of  $\Delta G_{*O} - \Delta G_{*OH}$ . Owing to the restrictive relationships between different steps, an ideal OER catalyst should locate at the boundary of four regions, where all steps show equal free energy changes (1.23 eV). Fortunately, Rh<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> located closest to the boundary of four steps among all catalysts, thus possessing the lowest overpotential of 0.43 V.

Similarly, an ORR contour map can be established as shown in Fig. 4d. With the increase of  $\Delta G_{*O} - \Delta G_{*OH}$ , the PDSs of  $M_3(C_6S_6)_2$  change from step 4 (\*OH  $\rightarrow$  \* +  $H_2O$ ) to step 1 (\* +  $O_2$ → \*OOH), and the optimal ORR catalyst located at the boundary of the four regions. Rh and Ir are closest to the boundary, thus possessing the extremely low overpotentials of 0.42 and 0.40 V, respectively.

#### 3.4. OER/ORR activity origin

To uncover the origin of OER and ORR activities on  $M_3(C_6S_6)_2$ , the electronic structure of the central metal which acts as the main active site in reactions has been carefully studied. The dband center  $(\varepsilon_d)$  has been evidenced to be an effective descriptor to relate the electronic structure of catalysts to the adsorption strength of intermediates. 57-59 In general, a more negative  $\varepsilon_d$  will be associated with weaker adsorption and vice versa. Fig. S6†

Fig. 5 (a) Correlation between the d-band center and the adsorption energy of \*OH. (b) The relationship between ICOHP and the adsorption energy of the OH intermediate. The fifth period transition metal center is taken as an example.

shows the partial density of states (PDOS) of d-orbitals of the central metal in M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> and the d-band center labeled. It can be seen that, for different metals in each period, the d-band center becomes lower as the d-electron number of metal increases, which will result in weaker adsorption strength between metal sites and intermediates. As shown in Fig. 5a and S7,† the relationships between  $\varepsilon_d$  and adsorption energy of the intermediates \*OH, \*O, and \*OOH were established. It can be seen that the adsorption energy *versus*  $\varepsilon_d$  shows a similar trend for all adsorbed species and was coincidental with the d-band center principle simultaneously. This is because when adsorption happens, the d-orbitals of metal will interact with the sporbitals of intermediates, leading to hybridization of orbitals and formation of bonding and antibonding states, while a lower d-band center results in a more occupied antibonding state and thus reduces the adsorption energy.

To evidence these conclusions, the bonding and antibonding states of the M-O bond in the OH adsorption structure have been analyzed for all M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> systems. Herein, the bonding and antibonding states are described by crystal orbital Hamilton populations (COHP), where the positive and negative values of -COHP represent the bonding and antibonding states, respectively, and the integration of -COHP (-ICOHP) represents the bond order. As seen in Fig. S8a-f,† with the central metal change from Nb to Pd, namely the d-electron number  $(\theta_d)$ varying from 4 to 10, the antibonding states are gradually shifted down relative to the Fermi level. This variation would induce more electron occupation in the antibonding states of the M-O bond, thus weakening the M-O bond correspondingly. To confirm this deduction, the relationship regarding  $\Delta G_{*OH} \nu s$ . -ICOHP was established as shown in Fig. 5b. It can be observed that a linear relationship between them was well fitted ( $R^2$ 0.94), that is, a higher -ICOHP will contribute to stronger adsorption of species.

Considering that the –ICOHP shows strong dependence on  $\theta_d$  of the central metal, a relationship between  $\theta_d$  and the adsorption strengths of \*OH, \*O, and \*OOH is supposed to exist. As seen in Fig. 6a, the adsorption energy of all adsorbents can be linearly correlated with  $\theta_d$  of the central metal, which

Fig. 6 (a)The relationship between  $\theta_{\rm d}$  and the adsorption energies of \*OH, \*O, and \*OOH. (b)The volcano plot of the OER on M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> with  $-\eta_{\rm OER}$  vs.  $\theta_{\rm d}$ . (c)The volcano plot of the ORR on M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> with  $-\eta_{\rm ORR}$  vs.  $\theta_{\rm d}$ .

firmly validates the potential of simple intrinsic properties of metal as an effective descriptor to determine the catalytic activity of the  $M_3(C_6S_6)_2$  system. On the basis of these linear relationships, a volcanic diagram between the overpotential and  $\theta_d$  was obtained (Fig. 6b and c). Each point representing the overpotential of different catalysts was added to the diagram. As seen, the activity of catalysts increases first and then decreases with the increase of  $\theta_d$ . When the  $\theta_d$  reaches around 8, the catalytic performance of  $M_3(C_6S_6)_2$  becomes the best, which can be ascribed to a moderate adsorption strength under these conditions as stated before.

## 4. Conclusion

To summarize, we have systematically and comprehensively studied the properties of a novel two-dimensional material M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> as a bifunctional catalyst for the OER and ORR by virtue of DFT methods. After considering the stability and activity of M<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub>, Rh<sub>3</sub>(C<sub>6</sub>S<sub>6</sub>)<sub>2</sub> was found to be a promising bifunctional catalyst with overpotentials of 0.43 V and 0.42 V for the OER and ORR, respectively, due to its moderate adsorption strength for the reaction intermediates. Besides, the volcanic maps and contour maps correlating OER and ORR activities with the adsorption strength of intermediates were established according to the scaling relationship between intermediates (\*OH, \*O, and \*OOH). Furthermore, the d-band center and ICOHP methods were employed to correlate the activity origin of the OER and ORR to a simple d-electron number of the central metal. These findings show a new kind of promising high-efficiency OER and ORR bifunctional catalyst, with great application potential in clean energy technology, and pave the way for further exploration of 2D-MOF catalysts.

#### Conflicts of interest

There are no conflicts to declare.

# Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant No. 62174122) and Natural Science Foundation of Hubei Province (Grant No. 2021CFB085). We are thankful for the financial support from Wuhan University. The computational resources were provided by the Supercomputing Center of Wuhan University.

#### References

- 1 S. Chu and A. Majumdar, *Nature*, 2012, 488, 294-303.
- 2 Z. Yang, J. Zhang, M. C. W. Kintner-Meyer, X. Lu, D. Choi, J. P. Lemmon and J. Liu, Chem. Rev., 2011, 111, 3577-3613.
- 3 E. Pomerantseva, F. Bonaccorso, X. Feng, Y. Cui and Y. Gogotsi, Science, 2019, 366, eaan8285.
- 4 Y. Gorlin and T. F. Jaramillo, J. Am. Chem. Soc., 2010, 132, 13612-13614.
- 5 H. A. Gasteiger, S. S. Kocha, B. Sompalli and F. T. Wagner, Appl. Catal., B, 2005, 56, 9-35.
- 6 D. J. Yang, L. J. Zhang, X. C. Yan and X. D. Yao, Small Methods, 2017, 1, 1700209.
- 7 B. C. H. Steele and A. Heinzel, *Nature*, 2001, 414, 345-352.
- 8 Z. P. Cano, D. Banham, S. Y. Ye, A. Hintennach, J. Lu, M. Fowler and Z. W. Chen, Nat. Energy, 2018, 3, 279-289.
- 9 J. T. Zhang, Z. H. Zhao, Z. H. Xia and L. M. Dai, Nat. Nanotechnol., 2015, 10, 444-452
- 10 T. He, S. K. Matta, G. Will and A. Du, Small Methods, 2019, 3,
- 11 Z. Xue, X. Zhang, J. Qin and R. Liu, J. Energy Chem., 2021, 55,
- 12 H. Wang, H.-W. Lee, Y. Deng, Z. Lu, P.-C. Hsu, Y. Liu, D. Lin and Y. Cui, Nat. Commun., 2015, 6, 1-8.
- 13 W. T. Hong, M. Risch, K. A. Stoerzinger, A. Grimaud, J. Suntivich and Y. Shao-Horn, Energy Environ. Sci., 2015, 8, 1404-1427.
- 14 X. Wan, H. Niu, Y. Yin, X. Wang, C. Shao, Z. Zhang and Y. Guo, Catal. Sci. Technol., 2020, 10, 8339-8346.
- 15 K. Zeng, X. Zheng, C. Li, J. Yan, J.-H. Tian, C. Jin, P. Strasser and R. Yang, Adv. Funct. Mater., 2020, 30, 2000503.
- 16 X. Sun, S. Sun, S. Gu, Z. Liang, J. Zhang, Y. Yang, Z. Deng, P. Wei, J. Peng, Y. Xu, C. Fang, Q. Li, J. Han, Z. Jiang and Y. Huang, Nano Energy, 2019, 61, 245-250.
- 17 B.-Q. Li, C.-X. Zhao, S. Chen, J.-N. Liu, X. Chen, L. Song and Q. Zhang, Adv. Mater., 2019, 31, 1900592.
- 18 K. Elumeeva, J. Masa, D. Medina, E. Ventosa, S. Seisel, Y. U. Kayran, A. Genc, T. Bobrowski, P. Weide, J. Arbiol, M. Muhler and W. Schuhmann, J. Mater. Chem. A, 2017, 5, 21122-21129.
- 19 Y. Sun, J. P. Bigi, N. A. Piro, M. L. Tang, J. R. Long and C. J. Chang, J. Am. Chem. Soc., 2011, 133, 9212-9215.
- 20 N. B. Thompson, M. T. Green and J. C. Peters, J. Am. Chem. Soc., 2017, 139, 15312-15315.
- 21 R. C. Cammarota, M. V. Vollmer, J. Xie, J. Ye, J. C. Linehan, S. K. Burgess, A. M. Appel, L. Gagliardi and C. C. Lu, J. Am. Chem. Soc., 2017, 139, 14244-14250.

- 22 J. Kim, H. E. Kim and H. Lee, ChemSusChem, 2018, 11, 104-
- 23 H. Furukawa, K. E. Cordova, M. O'Keeffe and O. M. Yaghi, Science, 2013, 341, 1230444.
- 24 J. R. Long and O. M. Yaghi, Chem. Soc. Rev., 2009, 38, 1213-1214.
- 25 S. Kitagawa, R. Kitaura and S. Noro, Angew. Chem., Int. Ed., 2004, 43, 2334-2375.
- 26 A. Schneemann, V. Bon, I. Schwedler, I. Senkovska, S. Kaskel and R. A. Fischer, Chem. Soc. Rev., 2014, 43, 6062-6096.
- 27 J. Lee, O. K. Farha, J. Roberts, K. A. Scheidt, S. T. Nguyen and J. T. Hupp, Chem. Soc. Rev., 2009, 38, 1450-1459.
- 28 B. Li, H.-M. Wen, W. Zhou and B. Chen, J. Phys. Chem. Lett., 2014, 5, 3468-3479.
- 29 H. B. Wu and X. W. Lou, Sci. Adv., 2017, 3, eaap9252.
- 30 A. J. Clough, J. M. Skelton, C. A. Downes, A. A. de la Rosa, J. W. Yoo, A. Walsh, B. C. Melot and S. C. Marinescu, J. Am. Chem. Soc., 2017, 139, 10863-10867.
- 31 T. Kambe, R. Sakamoto, K. Hoshiko, K. Takada, M. Miyachi, J.-H. Ryu, S. Sasaki, J. Kim, K. Nakazato, M. Takata and H. Nishihara, J. Am. Chem. Soc., 2013, 135, 2462-2465.
- 32 X. Huang, P. Sheng, Z. Y. Tu, F. J. Zhang, J. H. Wang, H. Geng, Y. Zou, C. A. Di, Y. P. Yi, Y. M. Sun, W. Xu and D. B. Zhu, Nat. Commun., 2015, 6, 1-8.
- 33 H. Liu, X. Li, L. Chen, X. Wang, H. Pan, X. Zhang and M. Zhao, J. Phys. Chem. C, 2016, 120, 3846-3852.
- 34 P. Zhang, X. Hou, L. Liu, J. Mi and M. Dong, J. Phys. Chem. C, 2015, 119, 28028-28037.
- 35 C. A. Downes, A. J. Clough, K. Chen, J. W. Yoo and S. C. Marinescu, ACS Appl. Mater. Interfaces, 2018, 10, 1719-1727
- 36 C. A. Downes and S. C. Marinescu, Dalton Trans., 2016, 45, 19311-19321.
- 37 A. J. Clough, J. W. Yoo, M. H. Mecklenburg and S. C. Marinescu, J. Am. Chem. Soc., 2015, 137, 118-121.
- 38 B. Mortazavi, M. Shahrokhi, T. Hussain, X. Zhuang and T. Rabczuk, Appl. Mater. Today, 2019, 15, 405-415.
- 39 Y. Cui, J. Yan, Z. Chen, J. Zhang, Y. Zou, Y. Sun, W. Xu and D. Zhu, Adv. Sci., 2019, 6, 1802235.
- 40 J. Zhang, Z. Zhou, F. Wang, Y. Li and Y. Jing, ACS Sustainable Chem. Eng., 2020, 8, 7472-7479.
- 41 G. Kresse and J. Furthmuller, Comput. Mater. Sci., 1996, 6,
- 42 G. Kresse and J. Furthmuller, Phys. Rev. B: Condens. Matter Mater. Phys., 1996, 54, 11169-11186.
- 43 P. E. Blöchl, Phys. Rev. B: Condens. Matter Mater. Phys., 1994, 50, 17953-17979.
- 44 J. P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett., 1996, 77, 3865-3868.
- 45 S. Grimme, J. Comput. Chem., 2006, 27, 1787-1799.
- 46 W. Tang, E. Sanville and G. Henkelman, J. Phys.: Condens. Matter, 2009, 21, 084204.
- 47 H. W. Kim, V. J. Bukas, H. Park, S. Park, K. M. Diederichsen, J. Lim, Y. H. Cho, J. Kim, W. Kim and T. H. Han, ACS Catal., 2019, 10, 852-863.
- 48 L. Yu, X. Pan, X. Cao, P. Hu and X. Bao, J. Catal., 2011, 282, 183-190.

- 49 J. Rossmeisl, A. Logadottir and J. K. Norskov, *Chem. Phys.*, 2005, 319, 178–184.
- 50 E. F. Holby, G. Wang and P. Zelenay, *ACS Catal.*, 2020, **10**, 14527–14539.
- 51 X. Guo, S. Lin, J. Gu, S. Zhang, Z. Chen and S. Huang, *ACS Catal.*, 2019, **9**, 11042–11054.
- 52 X. Liu, C. Wang, Y. Yao, W. Lu, M. Hupalo, M. Tringides and K. Ho, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2011, **83**, 235411.
- 53 M. N. Faraggi, N. Jiang, N. Gonzalez-Lakunza, A. Langner, S. Stepanow, K. Kern and A. Arnau, *J. Phys. Chem. C*, 2012, 116, 24558–24565.

- 54 H. Niu, X. Wang, X. Wang, C. Shao, J. Robertson, Z. Zhang and Y. Guo, ACS Sustainable Chem. Eng., 2021, 9, 3590–3599.
- 55 A. J. Medford, A. Vojvodic, J. S. Hummelshoj, J. Voss, F. Abild-Pedersen, F. Studt, T. Bligaard, A. Nilsson and J. K. Norskov, J. Catal., 2015, 328, 36–42.
- 56 Q. Deng, J. Zhao, T. Wu, G. Chen, H. A. Hansen and T. Vegge, J. Catal., 2019, 370, 378–384.
- 57 X. Mao, C. Ling, C. Tang, C. Yan, Z. Zhu and A. Du, *J. Catal.*, 2018, 367, 206–211.
- 58 C. Ling, L. Shi, Y. Ouyang, X. C. Zeng and J. Wang, *Nano Lett.*, 2017, 17, 5133–5139.
- 59 Z. Fu, C. Ling and J. Wang, *J. Mater. Chem. A*, 2020, **8**, 7801–7807