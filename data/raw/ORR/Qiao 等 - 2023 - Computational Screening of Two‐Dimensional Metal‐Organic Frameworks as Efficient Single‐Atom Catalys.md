---
source: Qiao 等 - 2023 - Computational Screening of Two‐Dimensional Metal‐Organic Frameworks as Efficient Single‐Atom Catalys.pdf
tool: marker
duration: 94.486s
generated: 2026-01-09T13:04:06.155828Z
---

Check for updates

Chemistry-A European Journal

www.chemeurj.org

## Computational Screening of Two-Dimensional Metal-Organic Frameworks as Efficient Single-Atom Catalysts for Oxygen Reduction Reaction

Man Qiao,\*[a] Jiachi Xie,[a] and Dongdong Zhu\*[a]

Abstract: The development of efficient and inexpensive oxygen reduction reaction (ORR) catalysts is crucial for renewable energy technologies. Herein, using density functional theory (DFT) methods and microkinetic simulations, we systematically investigated the ORR catalytic performance of a series of 2D metal-organic frameworks  $M_3(HADQ)_2$  (HADQ=2,3,6,7,10,11-hexaamine dipyrazino quinoxaline). It shows that all 2D  $M_3(HADQ)_2$  (M=Cr, Mn, Fe, Co, Ni, Cu, Ru, Rh and Pd) monolayers are metallic, due to  $\pi$ -conjugated crystal orbitals centered on the central metals and ligand N atoms. The

catalytic activity of M<sub>3</sub>(HADQ)<sub>2</sub> depends on the binding strength between ORR intermediates and metal species, and can be tuned via changing the central metals. Among these candidates, Rh<sub>3</sub>(HADQ)<sub>2</sub> and Co<sub>3</sub>(HADQ)<sub>2</sub> show superior ORR performance to Pt (111) with high half-wave potentials of 0.99 and 0.93 V, respectively. Moreover, the screened two catalysts have excellent intermediate-tolerance ability for dynamic coverage of oxygenated species on the active sites. Our work provides a new path towards developing efficient ORR electrocatalysts.

#### Introduction

The electrocatalytic oxygen reduction reaction (ORR) is at the heart of renewable energy conversion and storage devices such as fuel cells and metal-air batteries. However, the cathodic ORR exhibits inherent sluggish kinetics due to its complicated multi-electron transfer steps, which greatly limits the overall performance of fuel cells or metal-air batteries. Among multifarious ORR electrocatalysts, Pt and Pt-based materials show the best ORR activity. Nevertheless, the prohibitive costs and scarce reserve of Pt-based catalysts have severely limited their large-scale commercial application. Moreover, Pt-based electrodes generally suffer from problems such as insufficient durability, carbon monoxide deactivation and methanol crossover. Hence, it is highly desirable to search novel catalysts with low cost, high catalytic activity and long-term durability to replace Pt.

Over the past decades, numerous efforts have been devoted to exploiting non-metal containing materials as ORR electrocatalysts. However, due to the lack of active sites, the catalytic activity and stability of those metal-free catalysts are still worse than precious-metal based catalysts. In this regard, single-atom catalysts (SACs) with isolated metal centers anchored on low-cost substrates have attracted intensive attention. [4] One typical example is the M–N-C systems, which emerge as one of the

[a] Dr. M. Qiao, J. Xie, Dr. D. Zhu
 School of Chemistry and Materials Science
 Institute of Advanced Materials and Flexible Electronics (IAMFE)
 Nanjing University of Information Science and Technology
 Nanjing, 210044 (China)
 E-mail: dd.zhu@nuist.edu.cn
 qiaoman@nuist.edu.cn

Supporting information for this article is available on the WWW under https://doi.org/10.1002/chem.202300686 most promising ORR catalysts. In particular, Fe-N–C catalysts with pyridinic-type FeN<sub>4</sub> motifs exhibit superior ORR activity.<sup>[5]</sup> Furthermore, replacing the central atomic metal with Co, Ni and Mn is an effective method to enhance ORR activity in M–N-C catalysts.<sup>[6]</sup> Although SACs with MN<sub>4</sub> sites exhibit satisfying ORR performance, their low mass activity, insufficient stability, inhomogeneity, and poor electrical conductivity prevent their practical application at the industrial level.<sup>[7]</sup>

Two-dimensional (2D) metal-organic frameworks (MOFs) formed by metallic nodes and organic linkers, are emerging as a novel class of carbon-rich multifunctional materials due to their unique topology, high porosity, large surface area and well-defined active units.[8] Particularly, the properties and functions of MOFs can be tuned by altering the molecular building blocks, enabling their broad applications in catalysis, [9a,b] sensing, [9c,d] gas separation, [9e] energy storage and conversion, [9f,g] etc. For instance, Dincă et al. firstly reported the use of 2D conductive MOF  $Ni_3(HITP)_2$  (HITP=2,3,6,7,10,11hexaiminotriphenylene) for ORR in alkaline media. [10] Du et al. evaluated a series of transition metal atoms within 2D hexaaminobenzene-based coordination polymers (HAB-CPs) as bifunctional electrocatalysts for ORR and OER (oxygen evolution reaction).[11] Moreover, experimental and theoretical studies reported that 2D MOF M<sub>3</sub>C<sub>12</sub>X<sub>12</sub> can be used as effective ORR electrocatalysts through cooperating metallic nodes (Rh, Ir, Pd, Co, Mn, Fe) with organic linkers  $(C_6N_6H_6, C_6O_6, C_6S_6, C_6Se_6)$ . [12] Recently, Zhao et al. have synthesized a cobalt-based 2D conjugated MOF Co<sub>3</sub>(HADQ)<sub>2</sub> with 2,3,6,7,10,11-hexaamine dipyrazino quinoxaline (HADQ) as the organic linkages, which possess excellent activity for acidic ORR.[13] Note that altering the central metal atoms can effectively manipulate the catalytic properties of 2D MOFs. However, to the best of our knowledge, the ORR catalytic activity of 2D M<sub>3</sub>(HADQ)<sub>2</sub> with different transition metals have not yet been explored.

Chemistry Europe

European Chemical Societies Publishing

In this work, by utilizing comprehensive density functional theory (DFT) calculations and microkinetic simulations, we have investigated the stability, electronic properties and ORR performance of a series of 2D M<sub>3</sub>(HADQ)<sub>2</sub> (M=Cr, Mn, Fe, Co, Ni, Cu, Ru, Rh and Pd) monolayers. By varying the central metal atoms, the M<sub>3</sub>(HADQ)<sub>2</sub> monolayers have different adsorption strength to ORR intermediates, resulting in altered ORR activities. Through a systematic computational screening, four M<sub>3</sub>(HADQ)<sub>2</sub> (M= Co, Rh, Mn, Fe) monolayers are selected as promising candidates for ORR. Especially, the obtained half-wave potentials of Rh<sub>3</sub>(HADQ)<sub>2</sub> and Co<sub>3</sub>(HADQ)<sub>2</sub> are 0.99 and 0.93 V, which are superior to the benchmark Pt (111) at the same theoretical level. Our work provides useful guidance for rational design of high-performance ORR catalysts in the future.

#### **Results and Discussion**

# Structure, stability and electronic property of $M_3(HADQ)_2$ monolayers

The optimized geometrical structure of  $M_3(HADQ)_2$  monolayer is shown in Figure 1, and the primitive cell of 2D  $M_3(HADQ)_2$  is connected by three central metal atoms and two HADQ organic ligands. To systematically investigate the ORR catalytic performance of  $M_3(HADQ)_2$ systems, we considered 9 transition metals (M, including Co, Cr, Cu, Fe, Mn, Ni, Pd, Rh and Ru) as the central metal atoms. As shown in Table S1, the optimized lattice parameters of  $M_3(HADQ)_2$  are in the range from 21.20 to 21.83 Å. The distance of nearest metal atoms ( $D_m$ ) is larger than 10.60 Å, which means single-atom characteristic of  $M_3(HADQ)_2$  monolayers. Due to the larger ligand core, the pore size ( $D_p$ ) values are in the range from 16.68 to 17.23 Å, which would facilitate proton-electron transport during ORR. In addition, it can be found that the  $D_p$  of  $M_3(HADQ)_2$  is 16.73 Å, in good agreement with previous experimental value (16.50 Å). [13]

The stability is important for long-term use of a catalyst, thus the cohesive energy ( $E_{coh}$ ) of 2D  $M_3(HADQ)_2$  monolayers was calculated as follows:

Figure 1. Optimized geometric structures of 2D  $M_3$ (HADQ) $_2$  monolayer in a  $2\times 2$  supercell. The dashed rhombus marks the unit cell of monolayer, and the terms a and b indicate the lattice vectors.

$$E_{\text{coh}} = (n_1 E_{\text{C}} + n_2 E_{\text{N}} + n_3 E_{\text{H}} + n_4 E_{\text{M}} - E_{\text{2D-MOF}}) / (n_1 + n_2 + n_3 + n_4)$$

where  $E_C$ ,  $E_N$ ,  $E_H$ ,  $E_M$  and  $E_{2D\text{-MOF}}$  are the total energies of a single C atom, N atom, H atom, M atom and  $M_3(\text{HADQ})_2$  monolayer, respectively.  $n_1$ ,  $n_2$ ,  $n_3$  and  $n_4$  denote the number of C, N, H and M atoms, respectively. As can be seen from Table S1, the calculated  $E_{\text{coh}}$  are all positive values and in the range from 7.40 to 7.71 eV. As a reference, the  $E_{\text{coh}}$  of the experimentally synthesized  $Co_3(\text{HADQ})_2$  monolayer is 7.58 eV/atom, and such high binding strength of connected 2D  $M_3(\text{HADQ})_2$  frameworks indicates their excellent stability. Moreover, 2D  $Co_3(\text{HADQ})_2$  has been synthesized by experiments and used as acidic ORR electrocatalyst, and above high cohesive energy values suggest that other eight metals within  $M_3(\text{HADQ})_2$  frameworks can survive under acidic solution.<sup>[13]</sup>

Generally, electronic properties of the 2D MOFs play an important role in determining their electrocatalytic activity. Hence, we computed the band structures and density of states (DOS) of M<sub>3</sub>(HADQ)<sub>2</sub> monolayers to unveil their electrical conductivity. As shown in Figure 2, all computed M<sub>3</sub>(HADQ)<sub>2</sub> systems are metallic with several bands across the Fermi level, which can ensure effective electron transfer in the ORR process. Moreover, the calculated partial DOS demonstrates that the electronic states near the Fermi level are related to the center metal atoms. For example, the electronic states of M<sub>3</sub>(HADQ)<sub>2</sub> (M=Co, Cr, Rh and Ru) at the Fermi level are mainly dominated by the d orbitals of the central M atoms. Our computations also revealed that M<sub>3</sub>(HADQ)<sub>2</sub> (M=Co, Cr, Cu, Fe, Mn, Rh and Ru) are ferromagnetic with the magnetic moments of 0.97, 2.85, 0.50, 2.13, 3.30, 0.43 and 1.46 B per metal atom, respectively, while Ni<sub>3</sub>(HADQ)<sub>2</sub> and Pd<sub>3</sub>(HADQ)<sub>2</sub> are nonmagnetic. Therefore, M<sub>3</sub>(HADQ)<sub>2</sub> with different central metal atoms can result in different electronic states and magnetic properties, which could further affect the ORR catalytic activities.

#### O<sub>2</sub> adsorption and activation on M<sub>3</sub>(HADQ)<sub>2</sub> monolayers

Effective adsorption of O<sub>2</sub> on the catalyst surface is a prerequisite for the subsequent ORR pathways. Hence, we first investigated the interaction between  $O_2$  molecule with M<sub>3</sub>(HADQ)<sub>2</sub> monolayers before evaluating its ORR catalytic performance. Here, we considered three possible configurations for the adsorption of O<sub>2</sub> intermediates on M<sub>3</sub>(HADQ)<sub>2</sub>, including the physisorption, end-on and side-on chemisorption. As illustrated in Table 1, the nine M<sub>3</sub>(HADQ)<sub>2</sub> monolayers can be classified into three types according to the aforementioned three adsorption configurations. Cu<sub>3</sub>(HADQ)<sub>2</sub>, Ni<sub>3</sub>(HADQ)<sub>2</sub>, and Pd<sub>3</sub>(HADQ)<sub>2</sub> monolayers show weaker physisorption with adsorption energies approximately zero, which is similar to the most previous reported 2D Cu (Ni or Pd)-based MOF electrocatalysts. [12c,d] The variation in O2 adsorption free energy can be understood by the d-band center theory. As shown in Figure S1, Cu<sub>3</sub>(HADQ)<sub>2</sub>, Ni<sub>3</sub>(HADQ)<sub>2</sub>, and Pd<sub>3</sub>(HADQ)<sub>2</sub> have lower d-band centers, leading to weaker binding intensity between

Chemistry Europe

European Chemical Societies Publishing

Figure 2. Spin-polarized band structures and projected density of states of 2D a) Co<sub>3</sub>(HADQ)<sub>2</sub>, b) Cr<sub>3</sub>(HADQ)<sub>2</sub>, c) Cu<sub>3</sub>(HADQ)<sub>2</sub>, d) Fe<sub>3</sub>(HADQ)<sub>2</sub>, e) Mn<sub>3</sub>(HADQ)<sub>2</sub>, f) Ni<sub>3</sub>(HADQ)<sub>2</sub>, g) Pd<sub>3</sub>(HADQ)<sub>2</sub>, h) Rh<sub>3</sub>(HADQ)<sub>2</sub>, and i) Ru<sub>3</sub>(HADQ)<sub>2</sub> monolayers. The blue and pink solid lines denote spin-up and spin-down channels, respectively.

**Table 1.** Adsorption energy of  $O_2$  ( $\Delta E_{O2}$ ), the O-O bond length ( $L_{C:O}$ ) and polarized charges ( $PC_{O2}$ ) of the adsorbed  $O_2$ , limiting potential ( $U_1$ ) and overpotential (η) for the thermodynamics of the ORR on the M<sub>3</sub>(HADQ)<sub>2</sub> monolayer. M =Pd Mn Fe Co Cu Ru  $\Delta E_{02}(eV)$ -1.53 -0.62 -0.29 -0.03 -0.04 -1.35 -0.03 -0.60 -0.47  $L_{\mathrm{O-O}}$  (Å) 1.43 1.29 1.28 1.28 1.24 1.24 1.29 1.28 1.24 0.74 0.09 0.09 0.46 0.31 0.33 0.43 0.31 0.09 PC<sub>02</sub> (|e|)

0.23

1 00

-0.28

1.51

0.87

0.36

the metal centers and  $O_2$  molecule. Because the spontaneous chemisorption can capture and activate the  $O_2$  molecule, we would filter out these three materials as qualified ORR catalysts.

0.64

0.59

0.68

0.55

In contrast, the remaining six  $M_3(HADQ)_2$  monolayers show a chemisorption of  $O_2$  with adsorption energies range from -0.29 eV to -1.53 eV (Table 1).  $M_3(HADQ)_2$  (M=Co, Fe, Mn, Rh and Ru) chemisorb  $O_2$  via the end-on configuration, while only  $Cr_3(HADQ)_2$  prefer  $O_2$  adsorption with the side-on configuration.

Here, we take  $Co_3(HADQ)_2$  and  $Cr_3(HADQ)_2$  as examples to discuss the  $O_2$  activation mechanism with different adsorption configurations. As depicted in Figure 3a and Figure 3b,  $O_2$  adsorbed on the Co atom with a side-on configuration, and the charge transfers from Co to  $O_2$  molecule, which leads to the elongation of the O–O bond from 1.23 Å to 1.28 Å. Bader charge analysis indicates that  $O_2$  molecule gains 0.33 |e| from  $Co_3(HADQ)_2$  monolayer. For  $Cr_3(HADQ)_2$  monolayer,  $O_2$  molecule

0.01

1 22

0.87

0.36

-0.23

1.46

 $U_{L}(V)$ 

η (V)

0.09

1.14

Chemistry Europe

European Chemical Societies Publishing

Figure 3. Side views of the optimized structures, charge density difference plots and spin-polarized PDOS for a-c)  $O_2$  adsorption on  $Co_3(HADQ)_2$  and d-f)  $O_2$  adsorption on  $Cr_3(HADQ)_2$ . The cyan and yellow color represent the charge depletion and accumulation, and the isosurface is set to 0.006 e  $\mathring{A}^{-3}$ .

lies parallelly the plane to form two Cr–O bonds, with a higher charge transfer of 0.74 |e|, leading to a larger elongation of the O–O bond (1.43 Å). The  $O_2$  molecule interacts with  $M_3(HADQ)_2$  monolayer by electron acceptance and donation process, in which the unoccupied d orbitals of metal sites would accept the lone-pair electrons from the bonding orbitals ( $\sigma/\pi$ ) of  $O_2$ , and the occupied d orbitals simultaneously back-donate electrons to the antibonding  $2\pi^*$  orbitals of  $O_2$ , similar to CO oxidation<sup>[14a]</sup> and  $N_2$  reduction.<sup>[14b]</sup> Compared to  $Co_3(HADQ)_2$ , the  $1\pi$  and  $5\sigma$  orbitals of  $O_2$  molecule are highly hybridized with  $Cr_3d$ , and  $O_2_2\pi^*$  is more occupied after adsorption, suggesting the stronger adsorption strength between  $O_2$  and  $Cr_3(HADQ)_2$  (Figure 3c, f). In the following part, we will focus on the catalytic performance of these six  $M_3(HADQ)_2$  monolayers.

## ORR performance on $M_3(HADQ)_2$ monolayers

Next, we investigated the overall ORR performance of 2D  $M_3(HADQ)_2$  using computational hydrogen electrode (CHE) approach. In general, there are two typical reaction mechanisms in the ORR process, i.e., the associative mechanism and the dissociative mechanism. According to previous studies, the ORR on SACs usually proceeds via the associative mechanism, because dissociating O–O bond to separated O atom needs to overcome a large energy barrier. Therefore, we next calculated the free energy diagrams of  $M_3(HADQ)_2$  monolayers via the associative route (Figure 4b–g). The geometric structure of ORR intermediates ( $O_2^*$ , OOH\*, O\*, and OH\*) on surface of  $M_3(HADQ)_2$  monolayers along the 4e<sup>-</sup> process are displayed in Figure 4(a).

As can be seen from the Figure 4(b and g), due to over-activation of  $O_2$  molecule on Cr and Ru site, the last electrochemical step on  $Cr_3(HADQ)_2$  and  $Ru_3(HADQ)_2$  monolayers are energetically unfavourable. While all the ORR elementary steps occurring on  $Co_3(HADQ)_2$ ,  $Fe_3(HADQ)_2$ ,  $Mn_3(HADQ)_2$  and

Rh<sub>3</sub>(HADQ)<sub>2</sub> monolayer are exothermic, indicating that ORR process can proceed spontaneously on these four catalysts at potential of 0 V. To evaluate the catalytic performance of 2D M<sub>3</sub>(HADQ)<sub>2</sub> toward the electrochemical ORR, the limiting potential (U<sub>1</sub>) has been calculated. For Cr-, Fe-, Mn-, Rh- and Ru-centered 2D M<sub>3</sub>(HADQ)<sub>2</sub>, the potential-limiting step is the last electrochemical step (OH\*+H++e $^-\rightarrow$ ++H<sub>2</sub>O), while it is the first step (O<sub>2</sub>\*+H++ e<sup>-</sup>→OOH\*) for Co<sub>3</sub>(HADQ)<sub>2</sub> monolayer. As summarized in Table 1, the Co<sub>3</sub>(HADQ)<sub>2</sub> and Rh<sub>3</sub>(HADQ)<sub>2</sub> exhibits the best ORR catalytic activity with the same  $U_1$  value of 0.87 V, which is higher than that of Pt (111) (0.78 V). In addition,  $Fe_3(HADQ)_2$  and  $Mn_3(HADQ)_2$  also show good ORR catalytic activity with the  $U_{\rm L}$  value of 0.68 V and 0.64 V, respectively. Remarkably, the  $U_1$  of the competing  $2e^{-}$ pathway that has H<sub>2</sub>O<sub>2</sub> as the final product is 0.53 V (Co<sub>3</sub>(HADQ)<sub>2</sub>), 0.21 V (Rh<sub>3</sub>(HADQ)<sub>2</sub>), 0.23 V (Fe<sub>3</sub>(HADQ)<sub>2</sub>) and 0.22 V (Mn<sub>3</sub>(HADQ)<sub>2</sub>), which is much lower than that of corresponding 4e<sup>-</sup> pathway. The above results suggest that 2D Co<sub>3</sub>(HADQ)<sub>2</sub>, Rh<sub>3</sub>(HADQ)<sub>2</sub>, Fe<sub>3</sub>(HADQ)<sub>2</sub> and Mn<sub>3</sub>(HADQ)<sub>2</sub> monolayer with rather good activity and high selectivity are potential 4e<sup>-</sup> ORR electrocatalyst.

To better understand the origin of the ORR catalytic activities on different M<sub>3</sub>(HADQ)<sub>2</sub> monolayers, we constructed the scaling relationship of adsorption energy between different oxygenated intermediates ( $\Delta G_{OOH^*}$ ,  $\Delta G_{O^*}$  and  $\Delta G_{OH^*}$ ). As shown in Figure 5(a), we found that the ORR activity trends among different M<sub>3</sub>(HADQ)<sub>2</sub> monolayers can be dominated by the  $\Delta G_{OH^*}$ , as there is a clear liner relationship between  $\Delta G_{\text{OH*}}$  and  $\Delta G_{\text{OOH*}}$  or  $\Delta G_{\text{O*}}$  values. The slopes of 0.78 and 2.02 are analogous to that M-N-C based SACs for ORR.[17] With the established activity descriptor  $\Delta G_{\text{OH*}}$ , the plotted theoretical  $U_L$  versus  $\Delta G_{OH^*}$  for  $2DM_3(HADQ)_2$  exhibit universal volcano curve (see Figure 5b). Either OH\* binding to the M<sub>3</sub>(HADQ)<sub>2</sub> is too weak (Cu<sub>3</sub>(HADQ)<sub>2</sub>, Ni<sub>3</sub>(HADQ)<sub>2</sub>, and Pd<sub>3</sub>(HADQ)<sub>2</sub>) or OH\* binding that is too strong (Cr<sub>3</sub>(HADQ)<sub>2</sub>, and Ru<sub>3</sub>(HADQ)<sub>2</sub>) would lead to a poor ORR performance. In contrast, Mn<sub>3</sub>(HADQ)<sub>2</sub>, Fe<sub>3</sub>(HADQ)<sub>2</sub>, Rh<sub>3</sub>(HADQ)<sub>2</sub>, and Co<sub>3</sub>(HADQ)<sub>2</sub> show appropriate OH\* adsorption strength, suggesting relatively good ORR electrocatalytic activities. Especially, Rh<sub>3</sub>(HADQ)<sub>2</sub>, and Co<sub>3</sub>(HADQ)<sub>2</sub> locate near

Europe

Figure 4. a) Geometries of ORR intermediates: O<sub>2</sub>\*, OOH\*, O\* and OH\*. Red and green balls represent O and H atoms, respectively. b–g) Free energy diagrams for the ORR pathway on  $M_3(HADQ)_2$  at U=0 V and U=1.23 V, respectively.

Figure 5. a) The scaling relationships between  $\Delta G_{\text{OOH}}^*$ ,  $\Delta G_{\text{O}^*}$  and  $\Delta G_{\text{OH}^*}$  on various  $M_3(\text{HADQ})_2$  monolayers. b) Trends in ORR catalytic activity of the  $M_3(\text{HADQ})_2$ monolayers plotted as a function of both  $\Delta G_{\rm OOH}^*$  and  $\Delta G_{\rm OH}^*$ .

the top of the volcano curve and exhibit the highest ORR activity among all the investigated candidates. Interestingly, the most active site on M<sub>3</sub>(HADQ)<sub>2</sub> is the Co or Rh center, which belongs to the same group with 9 valence electrons. According to Table 1, it is observed that from group 6 to 11 (such as Cr to Cu), with the increased electrons of the outermost shell, the  $U_L$  would firstly increase and then decrease. The increased valence electrons in the active metal d-orbitals would partially occupy the antibonding orbital (M-O), thereby leading to weakened interaction with the subsequent intermediates. Among them, Co<sub>3</sub>(HADQ)<sub>2</sub> and Rh<sub>3</sub>(HADQ)<sub>2</sub> possess the excellent ORR catalytic activity owing to suitable adsorption strength of the ORR adsorbates.

and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License.

Chemistry Europe

European Chemical Societies Publishing

## Microkinetic simulations of the ORR on M<sub>3</sub>(HADQ)<sub>2</sub> monolayers

Finally, we employed microkinetic modelling to elucidate the ORR catalytic activity of 2D M<sub>3</sub>(HADQ)<sub>2</sub> monolayers. By solving the rate equations, the polarization curves of four MOFs were obtained (Figure 6a). Meanwhile, the ORR activity of Pt (111) is used as a benchmark for comparison. Figure 6(a) shows the half-wave potentials of 2D Rh<sub>3</sub>(HADQ)<sub>2</sub>, Co<sub>3</sub>(HADQ)<sub>2</sub>, Fe<sub>3</sub>(HADQ)<sub>2</sub> and Mn<sub>3</sub>(HADQ)<sub>2</sub> monolayers are estimated to be 0.99, 0.93, 0.80 and 0.72 V vs. RHE, respectively. Compared to Pt (0.86 V), 2D Co<sub>3</sub>(HADQ)<sub>2</sub> and Rh<sub>3</sub>(HADQ)<sub>2</sub> exhibit even better ORR performance and can be chosen as promising ORR candidates. It should be noted that the active sites of Pt and some SACs are usually occupied by O<sub>2</sub>\*/O\*/OH\* adsorbates when electrode potential is applied.[18] To address this concern, we performed microkinetic modelling to plot the coverage  $(\theta)$  of the most abundant intermediates on 2D M<sub>3</sub>(HADQ)<sub>2</sub> (M=Co, Fe, Mn and Rh) as a function of potential (U). As depicted in Figure 6(b and c), below 0.90 V vs. RHE, 2D Co<sub>3</sub>(HADQ)<sub>2</sub> and Rh<sub>3</sub>(HADQ)<sub>2</sub> are nearly adsorbate-free of OH\* and O<sub>2</sub>\* intermediates, indicating that 2D Co<sub>3</sub>(HADQ)<sub>2</sub> and Rh<sub>3</sub>(HADQ)<sub>2</sub> possess considerable intermediatetolerance ability under ORR working potentials.

#### **Conclusions**

To summarize, by means of first-principles calculations and microkinetic modelling, we have systematically investigated the stability, electronic properties, and ORR electrocatalytic activities of 2D M<sub>3</sub>(HADQ)<sub>2</sub> (M=Cr, Mn, Fe, Co, Ni, Cu, Ru, Rh and Pd) monolayers. According to the obtained results, four 2D MOFs including Rh<sub>3</sub>(HADQ)<sub>2</sub>, Co<sub>3</sub>(HADQ)<sub>2</sub>, Fe<sub>3</sub>(HADQ)<sub>2</sub> and Mn<sub>3</sub>(HADQ)<sub>2</sub> are identified as promising catalysts for ORR. Especially, the Rh<sub>3</sub>(HADQ)<sub>2</sub> and Co<sub>3</sub>(HADQ)<sub>2</sub> are considered as the optimal ORR catalysts due to their high half-wave potentials of 0.99 and 0.93 V, respectively. Given that 2D Co<sub>3</sub>(HADQ)<sub>2</sub> has been successfully synthesized and used as an electrocatalyst for acidic ORR, we believe that other three 2D M<sub>3</sub>(HADQ)<sub>2</sub> catalysts can also be synthesized experimentally and used in renewable energy conversion and storage devices in the near future. Therefore, our work

provides useful insight for developing 2D conductive MOFs for ORR.

### **Experimental Section**

All the geometry optimizations and energy calculations were performed by using spin-polarized density functional theory (DFT) as implemented within the Vienna ab initio simulation package (VASP) code.[19] The projector-augmented wave (PAW) method was used to treat the interactions between the ion cores and valence electrons. [20] The Perdew-Burke-Ernzerhof (PBE) functional of generalized gradient approximation (GGA) was adopted to deal with exchange-correlation energy. [21] The HSE06 functional with a mixing parameter alpha value of 0.25 were utilized to describe the band structure of 2D MOFs. [22] The cutoff energy was set to 400 eV and the Brillouin zone in the reciprocal space was sampled with a 3×3×1 Monkhorst-Pack -point grid. The convergence tolerance was set to be 10<sup>-5</sup> eV in energy and 0.05 eV/Å in force for all calculations. The vacuum space was set to 15 Å to avoid the interaction between periodical images. Grimme method (DFT-D3) was employed to describe the van der Waals interactions between the reaction species and MOFs.[23] The Bader charge analysis was selected to calculate charge transfer. [24] The ORR proceeds on 2D M<sub>3</sub>(HADQ)<sub>2</sub> catalysts via the four-electron reaction pathway can be described by the Equations (1)-(4):

$$^* + O_2 + H^+ + e^- \rightarrow OOH^*$$
 (1)

$$OOH^* + H^+ + e^- \rightarrow H_2O + O^*$$
 (2)

$$O^* + H^+ + e^- \rightarrow OH^*$$
 (3)

$$OH^* + H^+ + e^- \rightarrow H_2O + *$$
 (4)

where the \* and OOH\* (O\* and OH\*) denote the adsorbed site and adsorbed species on the catalyst, respectively. In each elementary step, the reaction Gibbs free energy ( $\Delta G$ ) was calculated as follows:

$$\Delta G = \Delta E + \Delta E_{ZPE} - T \Delta S + \Delta G_{U} + \Delta G_{pH}$$
 (5)

where  $\Delta E$  is the reaction energy difference obtained from DFT calculation,  $\Delta E_{\rm ZPE}$  is the zero energy calculated from the vibrational frequencies,  $\Delta S$  is the entropy change, and T is the system temperature (298.15 K, in our work). The calculated  $\Delta E_{\rm ZPE}$  and  $T\Delta S$  for each gas-phase species can be obtained from the NIST database.  $\Delta G_{\rm U}$  and  $\Delta G_{\rm PH}$  added in the equation was treated as the energy contribution of the electrode potential (U) and pH effect:  $\Delta G_{\rm U} = -e U$  and

Figure 6. a) Simulated ORR polarization curves for the 2D  $Co_3(HADQ)_2$ ,  $Fe_3(HADQ)_2$ ,  $Mn_3(HADQ)_2$ , and  $Rh_3(HADQ)_2$  monolayers. Coverage of the most abundant ORR intermediates on the b)  $Co_3(HADQ)_2$  and c)  $Rh_3(HADQ)_2$  monolayers as a function of electrode potential.

Chemistry Europe

European Chemical Societies Publishing

5213765,

 $\Delta G_{pH} = k_B T \ln 10 \times pH$ . Here, the value of pH was set to be 0 for the acidic medium. The limiting potential  $(U_l)$  was defined as:

$$U_{L} = -\max \{ \Delta G_{1}, \Delta G_{2}, \Delta G_{3}, \Delta G_{4} \} / e$$
 (6)

where,  $\Delta G_1$ ,  $\Delta G_2$ ,  $\Delta G_3$ ,  $\Delta G_4$  are the free energy change of reactions (1)–(4).

## **Supporting Information**

Additional references cited within the Supporting Information. [25]

#### **Acknowledgements**

The authors are grateful for funding support from the National Natural Science Foundation of China (22203045), Natural Science Foundation of Jiangsu Province (BK20200804), and Natural Science Foundation of the Jiangsu Higher Education Institutions of China (21KJB150030). We acknowledge the High Performance Computing Center of Nanjing University of Information Science & Technology for their support of this work.

#### Conflict of Interests

The authors declare no conflict of interest.

### **Data Availability Statement**

The data that support the findings of this study are available from the corresponding author upon reasonable request.

**Keywords:** density functional theory · metal-organic frameworks · microkinetic simulations · oxygen reduction reaction · single-atom catalysts

- [1] a) M. K. Debe, Nature 2012, 486, 43–51; b) Z. W. Seh, J. Kibsgaard, C. F. Dickens, I. Chorkendorff, J. K. Nørskov, T. F. Jaramillo, Science 2017, 355, eaad4998.
- [2] a) Y. Wang, Y. Li, T. Heine, J. Am. Chem. Soc. 2018, 140, 12732–12735;
   b) X. Ma, M. Li, J. Lu, C. Xu, J. Li, Chin. J. Struct. Chem. 2022, 41, 2212080–2212088.
- [3] a) Z. Zhao, C. Chen, Z. Liu, J. Huang, M. Wu, H. Liu, Y. Li, Y. Huang, Adv. Mater. 2019, 31, 1808115; b) L. Huang, S. Zaman, X. Tian, Z. Wang, W. Fang, B. Y. Xia, Acc. Chem. Res. 2021, 54, 311–322; c) Z. Kong, D. Zhang, Y. Lu, C. Yang, S. Du, W. Li, L. Tao, S. Wang, ACS Materials Lett. 2021, 3, 1610–1634; d) Z. Li, Di. W, W. Gong, J. Li, S. Sang, H. Liu, R. Long, Y. Xiong, Chin. J. Struct. Chem. 2022, 41, 2212043–2212050.
- [4] a) X. Yang, A. Wang, B. Qiao, J. Li, J. Liu, T. Zhang, Acc. Chem. Res. 2013, 46, 1740–1748; b) Y. Peng, B. Lu, S. Chen, Adv. Mater. 2018, 30, 1801995; c) B. Lu, Q. Liu, S. Chen, ACS Catal. 2020, 10, 7584–7618; d) S. Zhao, G. Chen, G. Zhou, L.-C. Yin, J.-P. Veder, B. Johannessen, M. Saunders, S.-Z. Yang, R. De Marco, C. Liu, S. P. Jiang, Adv. Funct. Mater. 2020, 30, 1906157.
- [5] a) Y. Chen, S. Ji, Y. Wang, J. Dong, W. Chen, Z. Li, R. Shen, L. Zheng, Z. Zhuang, D. Wang, Y. Li, Angew. Chem. Int. Ed. 2017, 56, 6937; b) Y.

- Wang, Y.-J. Tang, K. Zhou, *J. Am. Chem. Soc.* **2019**, *141*, 14115–14119; c) C. X. Zhao, B. Q. Li, J. N. Liu, Q. Zhang, *Angew. Chem. Int. Ed.* **2021**, *60*, 4448; d) T. Liu, Y. Wang, Y. Li, *Adv. Funct. Mater.* **2022**, *32*, 2207110; e) T. Liu, Y. Wang, Y. Li, *ACS Catal.* **2023**, *13*, 1717–1725.
- [6] a) X. Xie, C. He, B. Li, Y. He, D. A. Cullen, E. C. Wegener, A. J. Kropf, U. Martinez, Y. Cheng, M. H. Engelhard, M. E. Bowden, M. Song, T. Lemmon, X. S. Li, Z. Nie, J. Liu, D. J. Myers, P. Zelenay, G. Wang, G. Wu, V. Ramani, Y. Shao, Nat. Catal. 2020, 3, 1044–1054; b) Y. Zheng, D.-S. Yang, J. M. Kweun, C. Li, K. Tan, F. Kong, C. Liang, Y. J. Chabal, Y. Y. Kim, M. Cho, J.-S. Yu, K. Cho, Nano Energy 2016, 30, 443–449; c) J. Li, M. Chen, D. A. Cullen, S. Hwang, M. Wang, B. Li, K. Liu, S. Karakalos, M. Lucero, H. Zhang, Nat. Catal. 2018, 1, 935–945.
- [7] a) X. X. Wang, V. Prabhakaran, Y. He, Y. Shao, G. Wu, Adv. Mater. 2019, 31, 1805126; b) X. X. Wang, M. T. Swihart, G. Wu, Nat. Catal. 2019, 2, 578–589; c) Y. H. He, S. W. Liu, C. Priest, Q. R. Shi, G. Wu, Chem. Soc. Rev. 2020, 49, 3484–3524.
- [8] a) G. Chakraborty, I.-H. Park, R. Medishetty, J. J. Vittal, Chem. Rev. 2021, 121, 3751–3891; b) C. A. Trickett, A. Helal, B. A. Al-Maythalony, Z. H. Yamani, K. E. Cordova, O. M. Yaghi, Nat. Rev. Mater. 2017, 2, 17045; c) Y.-S. Wei, M. Zhang, R. Zou, Q. Xu, Chem. Rev. 2020, 120, 12089–12174.
- [9] a) Q. Wang, D. Astruc, Chem. Rev. 2020, 120, 1438–1511; b) J. Zhang, X. Zhu, W. Geng, T. Li, M. Li, C. Fang, X. Shan, Y. Li, Y. Jing, J. Energy Chem. 2021, 61, 71–76; c) H. Y. Li, S. N. Zhao, S. Q. Zang, J. Li, Chem. Soc. Rev. 2020, 49, 6364–6401; d) P. Liu, A. Liu, P. Wang, Y. Chen, B. Li, Chin. J. Struct. Chem. 2022, 41, 100001; e) Q. Qian, P. A. Asinger, M. J. Lee, G. Han, K. M. Rodriguez, S. Lin, F. M. Benedetti, A. X. Wu, W. S. Chi, Z. P. Smith, Chem. Rev. 2020, 120, 8161–8266; f) D. Sheberla, J. C. Bachman, J. S. Elias, C.-J. Sun, Y. Shao-Horn, M. Dincă, Nat. Mater. 2017, 16, 220–224; g) J. Liu, X. Song, T. Zhang, S. Liu, H. Wen, L. Chen, Angew. Chem. Int. Ed. 2021, 60, 5612.
- [10] E. M. Miner, T. Fukushima, D. Sheberla, L. Sun, Y. Surendranath, M. Dinca, Nat. Commun. 2016, 7, 10942.
- [11] G. Gao, E. R. Waclawik, A. Du, J. Catal. 2017, 352, 579–585.
- [12] a) J. Park, Z. Chen, R. A. Flores, G. Wallnerstrom, A. Kulkarni, J. K. Norskov, T. F. Jaramillo, Z. Bao, ACS Appl. Mater. Interfaces 2020, 12, 39074–39081; b) N. Lahiri, N. Lotfizadeh, R. Tsuchikawa, V. V. Deshpande, J. Louie, J. Am. Chem. Soc. 2017, 139, 19–22; c) J. Zhang, Z. Zhou, F. Wang, Y. Li, Y. Jing, ACS Sustainable Chem. Eng. 2020, 8, 7472–7479; d) T. Li, M. Li, X. Zhu, J. Zhang, Y. Jing, J. Mater. Chem. A 2021, 9, 24887–24894; e) Y. Cui, J. Yan, Z. Chen, J. Zhang, Y. Zou, Y. Sun, W. Xu, D. Zhu, Adv. Sci. 2019, 6, 1802235; f) J. Park, A. C. Hinckley, Z. Huang, D. Feng, A. A. Yakovenko, M. Lee, S. Chen, X. Zou, Z. Bao, J. Am. Chem. Soc. 2018, 140, 14533–14537.
- [13] R. Iqbal, S. Ali, G. Yasin, S. Ibraheem, M. Tabish, M. Hamza, H. Chen, H. Xu, J. Zeng, W. Zhao, Chem. Eng. J. 2022, 430, 132642.
- [14] a) S. Wang, J. Li, Q. Li, X. Bai, J. Wang, Nanoscale 2020, 12, 364–371; b) X. Guo, S. Lin, J. Gu, S. Zhang, Z. Chen, S. Huang, Adv. Funct. Mater. 2021, 31, 2008056.
- [15] J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard, H. Jonsson, J. Phys. Chem. B 2004, 108, 17886–17892.
- [16] a) SS. Kattel, G. Wang, J. Phys. Chem. Lett. 2014, 5, 452–456; b) Y. Chen,
   F. Sun, Q. Tang, Phys. Chem. Chem. Phys. 2022, 24, 27302–27311.
- [17] H. Xu, D. Cheng, D. Cao, X. C. Zeng, Nat. Catal. 2018, 1, 339-348.
- [18] a) J. Chen, L. Fang, S. Luo, Y. Liu, S. Chen, J. Phys. Chem. C 2017, 121, 6209–6217; b) H. T. Chung, D. A. Cullen, D. Higgins, B. T. Sneed, E. F. Holby, K. L. More, P. Zelenay, Science 2017, 357, 479–484; c) J. Zhang, H. Yang, B. Liu, Adv. Energy Mater. 2020, 11, 2002473.
- [19] a) G. Kresse, J. Hafner, Phys. Rev. B: Condens. Matter Mater. Phys. 1993, 47, 558; b) G. Kresse, J. Furthmüller, Phys. Rev. B 1996, 54, 11169.
- [20] G. Kresse, D. Joubert, *Phys. Rev. B* **1999**, *59*, 1758.
- [21] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1996, 77, 3865.
- [22] J. Heyd, G. E. Scuseria, M. Ernzerhof, J. Chem. Phys. 2003, 118, 8207–8215.
- [23] a) S. Grimme, J. Comput. Chem. 2006, 27, 1787–1799; b) S. Grimme, S. Ehrlich, L. Goerigk, J. Comput. Chem. 2011, 32, 1456–1465.
- [24] G. Henkelman, A. Arnaldsson, H. Jónsson, Comput. Mater. Sci. 2006, 36, 354–360.
- [25] H. A. Hansen, V. Viswanathan, J. K. Nørskov, J. Phys. Chem. C 2014, 118, 6706–6718.

Manuscript received: March 3, 2023 Accepted manuscript online: April 3, 2023 Version of record online: April 27, 2023