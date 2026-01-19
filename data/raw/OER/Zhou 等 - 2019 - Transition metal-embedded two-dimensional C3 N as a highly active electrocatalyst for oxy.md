---
source: Zhou 等 - 2019 - Transition metal-embedded two-dimensional C3 N as a highly active electrocatalyst for oxy.pdf
tool: marker
duration: 64.800s
generated: 2026-01-09T08:45:44.565460Z
---

# Journal of Materials Chemistry A

Accepted Manuscript Materials for energy and sustainability

> This article can be cited before page numbers have been issued, to do this please use: Y. Zhou, G. Gao, J. Kang, W. Chu and L. Wang*, J. Mater. Chem. A*, 2019, DOI: 10.1039/C9TA01389J.

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the [author guidelines](http://www.rsc.org/Publishing/Journals/guidelines/AuthorGuidelines/JournalPolicy/accepted_manuscripts.asp).

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard [Terms & Conditions](http://www.rsc.org/help/termsconditions.asp) and the ethical guidelines, outlined in our [author and reviewer resource centre](http://www.rsc.org/publishing/journals/guidelines/), still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

# Journal of Materials Chemistry A

# **ARTICLE**

# Transition metal embedded two-dimensional C<sub>3</sub>N as highly active electrocatalysts for oxygen evolution and reduction reactions

Received 00th January 20xx, Accepted 00th January 20xx

Yanan Zhou, ab Guoping Gao, b Jun Kang, b Wei Chu, \*a and Lin-Wang Wang \*b

DOI: 10.1039/x0xx000000x

www.rsc.org

Published on 23 April 2019. Downloaded by Idaho State University on 4/26/2019 11:23:07 AM.

Searching for the highly efficient, stable and cost-effective catalysts for oxygen evolution reaction (OER) and oxygen reduction reaction (ORR) are vital to resolve energy security and environmental problems. Herein, by means of the computational screening based on density functional theory (DFT), we studied a wide range of transition metal (TM) atom embedded into double carbon vacancy of C<sub>3</sub>N monolayer (V<sub>CC</sub>), denoted as TM-V<sub>CC</sub> (TM= Mn, Fe, Co, Ni, Cu, Ru, Rh, Pd, Ir and Pt), as efficient single-atom catalysts (SACs) for OER and ORR. The calculated results show that all the considered TM- $V_{CC}$  composites exhibit metallic feature that ensures the efficient charge transfer during reactions. The interaction strength between intermediates and TM-V<sub>CC</sub> has a direct correlation with the d-band center of TM, which can be tuned by changing the TM atoms with the different number of d-electron. The best catalyst for OER is Rh-V<sub>CC</sub> with an overpotential ( $\eta^{OER}$ ) of 0.35 V, followed by Co-V<sub>CC</sub> (0.43 V). For ORR process, Rh-V<sub>CC</sub> exhibits the lowest ORR overpotential ( $\eta^{ORR}$ ) of 0.27 V, followed by Co- $V_{CC}$  (0.42 V). The results suggest that the performance of the newly predicted Rh-V<sub>CC</sub> and Co-V<sub>CC</sub> SACs is comparable to those of the noble-metal benchmark catalysts for OER and ORR. Ab initio molecular dynamics simulation exhibits that the Rh-V<sub>CC</sub> and Co-V<sub>CC</sub> SACs can remain stable under 300K, and possess high energy barriers to prevent the isolated Rh and Co atoms from clustering. Our results highlight a new family of efficient and stable catalysts with single-atom anchored on carbon nitride-based materials, which provides a useful guideline for catalyst design and practical application.

# 1. Introduction

The growing global energy crisis and environmental pollution problem have stimulated tremendous interest in researches on sustainable energy storage and conversion systems. <sup>1-3</sup> Promising technologies include fuel cells, <sup>4</sup> water splitting <sup>5</sup> and metal-air batteries <sup>6</sup> owing to their high energy density and environmental benign. The electrocatalytic oxygen evolution reaction (OER) and oxygen reduction reaction (ORR) play important roles in the electrochemical energy

conversion processes. As we known, the OER occurs on the anode side of electrochemical water splitting cell with ruthenium (Ru) and iridium (Ir) oxides as the state-of-the-art electrocatalysts,<sup>7, 8</sup> while the ORR, a reverse reaction of the OER, happens on the cathode side of the fuel cell and the air battery with the platinum (Pt) and its alloys as the most active catalysts.9-11 However, due to the multistep holes transport requirement, and the insulating nature for some of these oxide catalysis, the reaction can be sluggish even for some of these noble metal catalysts. Furthermore, the high cost and limited availability of these noble metals make it highly desirable to use common metal replacement. The recent research of using common transition metal embedded in twodimensional materials open new revenue for searching such alternative catalysts.

Since the discovery of graphene,<sup>12</sup> two-dimensional (2D) materials such as hexagonal boron nitride (*h*-BN),<sup>13, 14</sup> MXenes<sup>15-17</sup> and phosphorene<sup>18, 19</sup> have attracted intense attention in both experiment and

<sup>&</sup>lt;sup>a</sup> School of Chemical Engineering, Sichuan University, Chengdu, 610065, Sichuan, China

b Materials Science Division, Lawrence Berkeley National Laboratory, Berkeley, 94720, California, United States

<sup>\*</sup>E-mail address: chuwei1965@scu.edu.cn (Wei Chu); lwwang@lbl.gov (Lin-Wang

<sup>†</sup>Electronic Supplementary Information (ESI) available: [details of any supplementary information available should be included here]. See DOI: 10.1039/x0xx00000x

ARTICLE Journal Name

theory as promising catalysts for energy conversion and storage applications. Notably, carbon-based materials were widely investigated as active OER and ORR catalysts due to their conductivity, low cost and wide use in electrochemistry.<sup>20-22</sup> It is known that introducing heteroatoms in graphene can significantly enhance its OER and ORR activity.<sup>23-26</sup> Examples include metal-nitrogen carbon (M-N-C) materials, like Co-N-C and Fe-N-C complexes.<sup>27-29</sup> However, they generally need advanced synthetic approaches techniques, and might be limited to a few transition metal elements. Another approach is to doping the 2D material with transition metals. Such single embedded atom can be behaved as catalytic center, and it provides another possible approach to search for new catalysts for OER and ORR reactions. The single-atom catalysts (SACs) can provide the tunable number of active sites and promise the use of minimum amount of transition metals. This approach also provides a large designing space in terms of the type of transition metal and their concentrations. It has been recently become a very active area of research.<sup>30, 31</sup>

Some of the early works were focused on doping pure graphene. However, it is found that pure graphene cannot bind with transition metal strong enough. Thus, some nitrogen is always introduced around the vacancy. However, recently, a new graphene-like 2D polyaniline (C<sub>3</sub>N) material was successfully synthesized in experiment using a bottom-up wet-chemical reaction, which contains uniformly distributed C and N atoms within a unit cell of the 2D crystal.<sup>32</sup> Compared to other 2D carbonitrides, e.g., C<sub>3</sub>N<sub>4</sub> and C<sub>2</sub>N, the C<sub>3</sub>N has the original structure of graphene, thus could mechanically more robust. This is indeed confirmed by theoretically calculation.<sup>33, 34</sup> In addition, it also suitable bandgap and superior thermal conductivity. The monolayer C<sub>3</sub>N and its derivatives have also been predicted to be suitable for gas sensor and capture, 35, 36 and Na- and K-ion batteries. 37 Baek et al. synthesized C<sub>3</sub>N as anode material for Li-ion batteries,<sup>38</sup> and observed excellent electrochemical performance. Most recently, using first-principle calculations, Yang et al. found that doped C<sub>3</sub>N monolayer with B replacing C is more active toward ORR than B replacing N in the acid environment.<sup>39</sup> All these previous works indicate that C<sub>3</sub>N could be an excellent candidate as a substrate for SACs. The preexistence of N in the system makes it unnecessary to introduce additional N when dope the system with TM. Nevertheless, so far, there is a lack of systematic theoretical investigation on the using of C<sub>3</sub>N as the substrate for SACs. Such theoretical investigation is necessary given the tremendous speed of progress in the experimental work in this field. The binding strength between perfect C<sub>3</sub>N-monolayer and TM atoms is weak. 40 It thus necessary to introduce defects in C<sub>3</sub>N monolayer, which allows the formation of dispersed single-metal electrocatalyst for OER/ORR! As well known, defect is extremely important, and very often it is what makes a semiconductor material works in terms of controlling the property of the material. Experimental studies have shown that using electron or ion irradiation technology, one could create vacancies on carbon-based materials. Such vacancies can act as binding sites for TM atoms. As Thus, in this work, we will study defect site binding with TM atoms to be used as SACs in C<sub>3</sub>N monolayer for OER and ORR. We will focus on late transition metals starting from Mn, including Fe, Co, Ni, Cu, Ru, Rh, Pd, Ir and Pt, as these elements have shown OER and ORR activities in various materials.

More specifically, we will design a series of atomically dispersed TM atoms adsorbed on the double-carbon vacancy site of the C<sub>3</sub>N monolayer and systematically investigated their catalytic activities toward OER and ORR. The double-carbon vacancy is necessarily since a single atom vacancy will not be large enough to accommodate a TM. On the other hand, losing one N atom at the defect site will not be ideal since it will reduce the binding energy of the TM at the defect site. Thus, as we will show, the formation energy of double-carbon vacancy is smaller than the C-N vacancy, which makes the double-carbon vacancy more likely to be formed. The metallic properties of all considered TM-V<sub>CC</sub> composites indicate that the charge transfer during the reactions should be efficient. We found strong correlation between the catalytic activities for OER, and ORR and the d-electron numbers of the doped TM atoms. Notably, our results show that Rh-V<sub>CC</sub> would be the best catalyst for OER with overpotential ( $\eta^{OER}$ ) of 0.35 V, followed by Co-V<sub>CC</sub> (0.43 V). Moreover, Rh-V<sub>CC</sub> is the best catalyst for ORR with the lowest ORR overpotential ( $\eta^{ORR}$ ) of 0.27 V, followed by Co-V<sub>CC</sub> (0.42 V).

#### 2. Computational methodology

All the calculations were carried out by the Vienna ab initio Simulation Package (VASP)<sup>48, 49</sup> using density functional theory (DFT) method. The projector augmented wave (PAW) potentials were employed to describe the nuclei-electron interactions.<sup>50</sup> The generalized gradient approximation (GGA)<sup>51</sup> with the PerdewBurke-Ernzerhof (PBE)52 functional was used the electron exchange-correlation describe interactions. Grimme's DFT-D3 correction method was used to account for the van der Waals (vdW) effects.<sup>53</sup> Spin polarization was considered throughout all the calculations. The wavefunctions of valence electrons were expanded by plane wave basis set with a cutoff energy of 500 eV. The convergence criterion for energy and force during geometrical optimization

Published on 23 April 2019. Downloaded by Idaho State University on 4/26/2019 11:23:07 AM.

Journal Name ARTICLE

was set to 10<sup>-5</sup> eV and 10<sup>-2</sup> eV/Å, respectively. The vacuum space of 20 Å was applied to avoid the interactions along the z-direction. The Brillouin zone was sampled by a 3x3x1 Monkhorst-Pack mesh grid for the structural optimization.<sup>54</sup> The climbing image nudged elastic band (CINEB) method<sup>55, 56</sup> was used to explore the TM diffusion barrier. Ab initio molecular dynamics (AIMD) simulations were also performed to examine their dynamical stability, and the algorithm of the Nose thermostat was carried out to simulate a canonical ensemble,<sup>57</sup> under 300K for 10ps with a time step of 2fs. Throughout the calculation, for aqueous based materials, we have also used implicit solvent model to account for the effects of polarization due to the water condition that calculated with VASPsol with the dielectric constant set to 78.4.58

In the acidic environment, the OER proceeds have been proposed via a four-stage pathway. 45, 59, 60 In this pathway, there are four intermediate states. They are: initiate state with the bare surface (denoted as \*); the state with one HO binding to the surface (denoted as HO\*); the state with one O binding on the surface (denoted as O\*); the state with HOO binding to the surface (denoted as HOO\*). From one intermediate state to the next intermediate state, the system either takes one H<sub>2</sub>O molecule and releases one H<sup>+</sup> (in the acid case), or take one OH- (in the alkali case), or simply release one H<sup>+</sup>. In all these cases, each step will release one hole charge from the electrode Fermi energy to the solvent. The fourth intermediate state can go back to the first intermediate state by releasing one O<sub>2</sub> molecule, one H<sup>+</sup> and one electron. These four steps can be written as:

$$H_2O(1) + * \rightarrow HO^* + H^+ + e^-$$
 (1a)

$$HO^* \to O^* + H^+ + e^-$$
 (1b)

$$O^* + H_2O(1) \rightarrow HOO^* + H^+ + e^-$$
 (1c)

$$HOO^* \rightarrow ^* + O_2(g) + H^+ + e^-$$
 (1d)

where \* stands for catalyst and adsorption site on the catalyst, (l) and (g) refer to the liquid and gas phase, respectively. On the other hand, the Gibbs free energies corresponding to the four intermediate states (using the first state as the reference energy) will be:

$$\Delta G_* = 0 \tag{2a}$$

$$\Delta G_{HO^*} = G_{HO^*} + G_{H^+} + \mu_{e^-} - G_{*^-} - G_{H2O1}$$
 (2b)

$$\Delta G_{O^*} = G_{O^*} + 2G_{H^+} + 2\mu_{e^-} - G_{*} - G_{H2O.1}$$
 (2c)

$$\Delta G_{\text{HOO}*} = G_{\text{HOO}*} + 3G_{\text{H+}} + 3\mu_{\text{e-}} - G_{\text{*-}2}G_{\text{H2O},l}$$
 (2d)

$$\Delta G_{*+O2} = G_{O2} + 4G_{H+} + 4\mu_{e-} - 2G_{H2O1}$$
 (2e)

The last equation Eq.(2e) represents the situation when one oxygen molecule is generated, and the system goes back to its initial state (\*). Note these intermediate states Gibbs free energies depend on the chemical potential of H<sup>+</sup> in the water:  $G_{H^+}$  (hence, the pH values), as well as the electrode Fermi energy  $\mu_{e^-}$ . We will study the pH=0 case, and use the standard Hydrogen generation electrode (SHE) as the reference for electrode Fermi energy. Hence,  $\mu_{e^-}=\mu_{SHE}$ -U (we have used a negative sign here to be consistent with the convention, and make U positive). Since at pH=0, we have:  $G_{H^+}+\mu_{SHE}=1/2G_{H2}$ , the above equations can be converted into:

$$\Delta G_* = 0 \tag{3a}$$

$$\Delta G_{HO*} = G_{HO*} + 0.5G_{H2,g} - U - G_{*} - G_{H2O,l}$$
 (3b)

$$\Delta G_{O^*} = G_{O^*} + G_{H2,g} - 2U - G_{*} - G_{H2O,l}$$
 (3c)

$$\Delta G_{\text{HOO}*} = G_{\text{HOO}*} + 1.5G_{\text{H2,g}} - 3U - G_{*} - 2G_{\text{H2O,l}}$$
 (3d)

$$\Delta G_{*+O2} = 4*1.23 \text{ eV} - 4U$$
 (3e)

In writing down the Eq.(3e), we have used the experimental fact:  $G_{O2}+4G_{H2}-2G_{H2O,1}=4*1.23$  eV, so we don't need to calculate the free energy of O<sub>2</sub> in the gas phase due to the poorly description of this DFT calculation. It is difficult to calculate directly the Gibbs free energy of the liquid phase G<sub>H2O,I</sub>. It is customary to calculate the Gibbs free energy of liquid phase from its vapor phase counterpart at their equilibrium pressure when they have the same Gibbs free energies. Thus,  $G_{H2O,I}=E_{H2O}+ZPE_{H2O}-TS_{H2O}$ . Here,  $E_{H2O}$  is the total energy of single water molecule in gas phase obtained directly from DFT calculation; ZPE<sub>H2O</sub> is the zero point free energy; T is the temperature of 298.15 K, TS<sub>H2O</sub> is the entropy term of the gas phase, it is 0.67 eV.61 Similarly for G<sub>H2,g</sub>=E<sub>H2</sub>+ZPE<sub>H2</sub>-TS<sub>H2</sub>, E<sub>H2</sub> is the DFT energy of H<sub>2</sub> molecule in vacuum, and the ZPE<sub>H2</sub> is the zero energy of the frequency vibration. The TS<sub>H2</sub> are calculated with the value of 0.41 eV in Ref.<sup>61</sup> The same is true to the other few adsorbed adsorbates X (X=HO\*, O\* and HOO\*), where  $G_{X*}=E_{X*}+ZPE_{X*}-TS_{X*}$ . Here  $E_{X*}$  is the DFT total energy of the X\* system after taking into account the solvent polarization effect using the implicit solvent model. ZPE<sub>X\*</sub> is the ZPE of X\* calculated from its phonon modes. Here we only include the phonon degree of freedom in X\*, while keeping the catalyst \* fixed during frequency calculation.  $TS_{X*}$  is the entropy energy of the adsorbed adsorbates obtained from the frequency vibration calculation. The zero-point energies corrections and the entropies contributions of the adsorbatess (HO\*, O\* and HOO\*) on the Co-V<sub>CC</sub> and Rh-V<sub>CC</sub> are listed (2e) in **Table S1 and S2**. Finally, G<sub>\*</sub>=E<sub>\*</sub> refers to the DFT

**ARTICLE** 

Published on 23 April 2019. Downloaded by Idaho State University on 4/26/2019 11:23:07 AM.

calculated total energy of catalyst substrate using the implicit solvent model. Note that for all the above calculations, we have ignored the thermal energy term in the evaluation of G due to the phonon degree of freedom. That energy can be calculated from the phonon model, just like the TS term, but it is rather small, thus has been ignored.

After having a way to calculate the intermediate state Gibbs free energies, the reaction criterion from one state to a subsequent state in the OER reaction is to increase the voltage U, so the Gibbs free energy of the subsequent step becomes lower than the previous step. This also implies that  $\Delta G_{*+O2}$  must be smaller than  $\Delta G^*$ . Thus, the minimum possible U is 1.23 V. Besides, this can only happen when the Gibbs free energies of the four intermediate states are equal distance spaced between 0 and 4\*1.23 when U=0. If this is not true, then the maximum  $(U_{max})$  value of all the four steps for their reactions to happen is the bottleneck of the whole OER. The  $\eta^{OER} = U_{max} - 1.23$  is called the overpotential of OER. The goal of OER optimization is to reduce this over potential as much as possible.

The ORR is just the inverse reaction of OER. Here the U which makes the Gibbs free energies equal to each other between two subsequent intermediate states is the voltage it generated in this chemical reaction. The minimum  $U_{min}$  among all the four steps defined the voltage of the fuel-cell. Thus, instead of looking for Umax, here we are interested in  $U_{min}$  of the four reactions. Obviously, the maximum possible  $U_{min}$  is also 1.23 V when all the four Gibbs free energies of Eq.(3) are equally spaced when U=0.  $\eta^{ORR}$ =1.23- $U_{min}$  is call the overpotential of ORR. The goal of ORR research is also looking for the minimum ORR overpotential.

Finally, it is worth to note that, although we have tested different atomic configurations of the HO\*, O\*, HOO\* absorption on the TM- $V_{CC}$  site, the most stable configuration always correspond to one O binding directly to the TM.

#### 3. Results and discussion

As shown in **Fig. S1a** in the Supporting Information, there are six C and two N atoms in the primitive unit cell of p-C<sub>3</sub>N. The optimized crystal lattice parameter of p-C<sub>3</sub>N is 4.86 Å, and the bong length of C-C and C-N are both about 1.41 Å, in agreement with the previous results.  $^{33, 40, 62}$  There are two kinds of double vacancies in the (3x3) supercell of the C<sub>3</sub>N monolayer, one is double carbon vacancy (V<sub>CC</sub>) by removing two neighboring C atoms, the other one is vacancy CN (V<sub>CN</sub>) created by removing one C atom and its neighboring N atom. The optimized stable atomic configuration for the (3x3) p-C<sub>3</sub>N, V<sub>CC</sub> and V<sub>CN</sub>

**Fig. 1** (a) Top view of TM-V<sub>CC</sub> monolayer, (b) Binding energies of various transition metals anchored on the  $V_{CC}$  systems.

nanosheets are exhibited in Fig. S1b-d, respectively. It can be seen that there is no significant structural reconstruction around the vacancy of V<sub>CC</sub>, the bond lengths of C-C and C-N around the vacancy stretch to 2.75 and 2.47 Å, respectively. While, for  $V_{CN}$ , one pentagon and one hendecagon rings are formed around the vacancy. The vacancy formation energy (E<sub>f</sub>) is a key physical parameter to describe the stability of point defects in C<sub>3</sub>N monolayer, and defined as E<sub>f</sub>=E<sub>V</sub>  $-E_P + \mu_{host}$ . 63, 64 In this equation,  $E_V$  and  $E_P$  are the total energies of the defective and perfect (3x3) C<sub>3</sub>N sheets, respectively, whost is the chemical potential of the removed C or N atom, determined by the total energy per atom in perfect graphene or in a N<sub>2</sub> molecule, respectively. The calculated formation energies for V<sub>CC</sub> and V<sub>CN</sub> are 4.88 and 6.27 eV, respectively, which agrees well with the reported result,65 suggesting that the V<sub>CC</sub> vacancy thermodynamically favored over V<sub>CN</sub>. Compared to the formation energy of the double vacancy in graphene (7.26 eV),66 the much smaller formation energy of the V<sub>CC</sub> indicates that the formation of V<sub>CC</sub> in the C<sub>3</sub>N monolayer is thermodynamically more favorable.67 Therefore, we did the following works based on the V<sub>CC</sub> defect. Electronic conductivity is one of the key factors in determining the efficiency of electrode materials. Therefore the electronic structures of V<sub>CC</sub> will be studied. For comparison, the density of states (DOS) of p-C<sub>3</sub>N and V<sub>CC</sub> monolayers are exhibited in Fig. S2a, The DOS shows that p-C<sub>3</sub>N is a nonmagnetic indirect semiconductor with a band gap about 0.37 eV at the PBE level calculation in line with previous results.<sup>39, 65</sup> Seen from **Fig. S2b**, in contrast to p-C<sub>3</sub>N, the V<sub>CC</sub> is magnetic and the calculated total spin magnetic moment is 1.33  $\mu_B$ . Additionally, the electron states crossing the Fermi levels suggests a good electric conductivity of V<sub>CC</sub> if there are sufficient concentration of it, which makes it suitable for electrode.

The vacancy region of  $V_{CC}$  is expected to bind metal atoms tightly as the substrate for SACs (**Fig. 1a**). First, we calculated the binding energies for vary TM atoms on the  $V_{CC}$  from Mn to Cu, and some noble metal atoms such as Ru, Rh, Pd, Ir and Pt are also taken into consideration in our investigation. The binding energy is defined as  $E_b = E_{TM-Vcc} - \mu_{TM} - E_{Vcc}$ ,

Journal Name ARTICLE

where  $E_{TM-V_{CC}}$  and  $E_{Vcc}$  are the total energies of the TM- $V_{CC}$  system, and  $V_{CC}$  substrate, respectively.  $\mu_{TM}$  is the chemical potential of the TM atom computed from the elemental bulk crystal. Since the  $\mu_{TM}$  is referenced with respect to its bulk metal, negative values of  $E_b$  (**Fig. 1b**) indicates that the TM atoms in  $V_{CC}$  are stable against clustering. The optimized configurations of TM- $V_{CC}$  are exhibited in **Fig. S3**, we can see that all the TM atoms prefer to be adsorbed on the vacancy area.

The distinct electronic structures for different TM atoms anchored on the V<sub>CC</sub> can provide us with insights to understand their catalytic properties. The PDOS of the d orbitals of the different TM atoms anchored on V<sub>CC</sub> were calculated as shown in Fig. 2. As shown in Fig. S4, all the considered TM-V<sub>CC</sub> catalysts in our work show metallic properties, suggesting good electric conductivity for all the TM-V<sub>CC</sub> catalysts as discussed above. The d band center position ( $\varepsilon_d$ ) has been used to analyze the interaction strength between adsorbate and substrate. 69-73 In Fig. 2, we also plotted  $\varepsilon_d$  calculated as the center of mass position of the d-band PDOS. A clear shift of  $\epsilon_d$  to lower energy position with respect to the Fermi level is seen with the increase of the d-electron number of the TM atom. It is well known that the large number

transfer from the TM to the adsorbates. As a result the interaction strength of adsorbates on 10FM 10FM 107 13898 the following expected to exhibit Mn>Fe>Co>Ni>Cu, Ru>Rh>Pd and Ir>Pt. To verify the above prediction, we plot the Gibbs free energy of adsorbates (i.e, the intermediate state energies as calculated in Eq.(3) with U=0) with various number of d-electrons of the TM-V<sub>CC</sub> systems in Fig. 3a. We can conclude that, for the TM's in the same row of the periodic table, the increase of their d-electron numbers tend to weaken the adsorption free energies of adsorbates. This is also true with the position of  $\varepsilon_d$  as shown in Fig. 3b. There is a negative correlation between  $\varepsilon_d$  and  $\Delta G$  of adsorbates, as least when the TM's of the same row are used. This phenomenon was experimentally<sup>75</sup> in observed and also theoretically studies. 45, 76 Therefore, we can modulate the interaction strength to the optimal value for both OER and ORR performance by tuning the TM atom embedded into V<sub>CC</sub>.

Fig. 2 Calculated PDOS of the d band in the TM-V<sub>CC</sub> systems. The Fermi level is set at the zero of energy (blue dash line) and the d band center ( $\varepsilon_d$ ) is marked by the red dash line.

of d-electron in the TM and lower energy level of  $\epsilon_d$  generally result in a weaker interaction strength with HO\*, O\* and HOO\* adsorbates.<sup>74</sup> This is because the interaction between the TM and the adsorbates happen by hybridization of their electronic level, and charge

ARTICLE Journal Name

**Fig. 3** (a) Gibbs free energy of adsorbates as defined in Eq.(3) (with U=0) with various numbers of d-electron doped TM-V<sub>CC</sub> systems, and (b) Gibbs free energy of adsorbates correspond to the d band center  $\epsilon_d$ 

As presented above, the intermediate state Gibbs free energies of adsorbates (HO\*, O\* and HOO\*) on different TM-V<sub>CC</sub> catalysts determines the distinct rate-determining step of OER and ORR. According to the Sabatier's principle,77 too strong or too weak interaction strength between the absorbates and catalyst both leads to the adversarial effects on OER and ORR. For an ideal catalyst, the energy distances for all the steps (between two adjacent intermediate states) are all 1.23 eV (when U=0). Therefore, the OER and ORR can occur at their thermodynamic limit and the overpotential  $\eta$  is zero. However, in reality, the energy steps are not equally distanced, which limits the reactions. While, the OER overpotential is determined by the maximum energy distance, the ORR overpotential is determined by the minimum

energy distance as discussed above. The calculated free energy diagrams for all the intermediate states of OER and ORR for each TM-V<sub>CC</sub> catalyst are shown in Fig. 4, and the rate-determining step of each catalyst colored in red (for OER) and green (for ORR) respectively. With the increase of the d-electron number of anchored TM atoms, the Gibbs free energy of HO\*, O\* and HOO\* on TM-V<sub>CC</sub> decreases accordingly (Fig. 3a). From the Mn-V<sub>CC</sub> to Co-V<sub>CC</sub> in the period four, the third step  $(O^* \rightarrow HOO^*)$  exhibits as the rate-determining step, and the corresponding overpotential  $\eta^{OER}$  decreases from 1.86 V (Mn-V<sub>CC</sub>) to 0.43 V (Co-V<sub>CC</sub>). However, for the Ni-V<sub>CC</sub> and Cu-V<sub>CC</sub>, with the further increase of the d-electron number, the second step from HO\* to O\* becomes the potential-determining step (Fig. 4d and e). This trend is also true for the noble metals (Ru-V<sub>CC</sub>, Rh-V<sub>CC</sub>, Pd- $V_{CC}$ , Ir- $V_{CC}$  and Pt- $V_{CC}$ , Fig. 4f to 4j). Remarkably, the Rh-V<sub>CC</sub> among the considered systems is predicted to possess the best OER performance with an overpotential  $\eta^{OER}$  of 0.35 V, this is followed by Co-V<sub>CC</sub> of 0.43 V. Both of them are comparable to the calculated RuO<sub>2</sub> catalyst (0.42 V).<sup>78</sup>

As we known, the ORR is the reverse reaction of the OER. With the increase number of d-electron from Mn to Co, the corresponding  $\eta^{ORR}$  value decreases from 1.11 eV (Mn-V<sub>CC</sub>) to 0.42 eV (Co-V<sub>CC</sub>). The third step (O\*  $\rightarrow$  HO\*), fourth step (HO\*  $\rightarrow$  H<sub>2</sub>O) and the second step (HOO\*  $\rightarrow$  O\*) is the potential-determining step for Mn-V<sub>CC</sub>, Fe-V<sub>CC</sub> and Co-V<sub>CC</sub>,

Fig. 4 The free energy diagrams of OER and ORR on TM-V<sub>CC</sub>. The red and the blue dash lines are the rate-limiting step for OER and ORR, respectively.

Published on 23 April 2019. Downloaded by Idaho State University on 4/26/2019 11:23:07 AM.

Journal Name ARTICLE

respectively. Similar to the above OER performance, with the further increase of the d-electron number for Ni-V<sub>CC</sub> and Cu-V<sub>CC</sub>, the value of  $\eta^{ORR}$  increases

Fig. 5 The scaling relationship between  $\Delta G_{HO^*}$  and  $\Delta G_{HOO^*}$  on various TM-V  $_{CC}$  systems.

accordingly against the ORR performance. Among all the explored TM-V<sub>CC</sub>, the best catalyst for the ORR is Rh-V<sub>CC</sub> with the lowest  $\eta^{ORR}$  of 0.27 V, followed by Co-V<sub>CC</sub> (0.42 V). Notably, both of their ORR overpotentials are lower than the reported best catalyst Pt for ORR (0.45 V)<sup>59</sup> based on DFT calculation. For comparison, previous findings on OER/ORR catalytic performance for the metal doped carbon materials are listed in Table S4, especially the Co- and Rh- based SACs.  $^{26,\,45,\,79}$ 

The relationship between the Gibbs free energy of the intermediates ( $\Delta G_{HO^*}$ ,  $\Delta G_{O^*}$  and  $\Delta G_{HOO^*}$  of Eq.3 when U=0) can explored to analyze the OER and ORR trends for different catalysts. By comparing the  $\Delta G_{HO^*}$  and  $\Delta G_{HOO^*}$  for all the calculated cases in our study, we found that  $\Delta G_{HOO^*}$  can be expressed as a function of  $\Delta G_{HO^*}$  via equation  $\Delta G_{HOO^*}$ =0.86 $\Delta G_{HO^*}$ +3.13 eV as shown in **Fig. 5**. Apparently, the free energies of adsorbed HO\* and HOO\* species are linearly correlated as the coefficient of determination (R²) is 0.979. The slope close to the unity in the relationship between HO\* and HOO\* reflects the fact that both intermediates have a single bond between on O atom

and TM. The constant intercept implies that HO\* and HOO\* normally prefer the same projections additional site, 78 as shown in **Fig. S5 and S6**. Notably, similar relationships were also observed in carbon materials and metal surfaces.80 Note, that, if we assume the above slop is 1, then that means the  $\Delta G_{HOO}^*-\Delta G_{HO}^*$  is a constant. Given the fact, all the OER determining steps happen either at the step of HO\* to O\*, or O\* to HOO\* (with the exception of Pd, where its \* to HO\* step distance is almost the same as the HO\* to O\* distance), then the overpotential will be determined purely by the  $\Delta G_{O^*}$ - $\Delta G_{HO^*}$  distance. This is indeed true as the volcano plot shown in Figure 6a, where the overpotential falls into a line as a function of  $\Delta G_{O^*}$ - $\Delta G_{HO^*}$ . The theoretical line is the dashed line in **Fig. 6a** under the assumption  $\Delta G_{HOO}^*$ - $\Delta G_{HO}^*$  is a constant. The smallest overpotential happens around Rh and Co when their  $\Delta G_{O^*}$ - $\Delta G_{HO^*}$  is close to a half of  $\Delta G_{HOO^*}$ - $\Delta G_{HO*}$ .

As mentioned above, the overpotential of ORR is determined by the minimum step distance in Fig. 4. We notice that, this ORR step can be approximated as either happening at the first step: \* to HO\* (step1), or at the last step, from HOO\* to \*+O2 (step4). Note, for Mn, Ru, the determining step happen at HO\* to O\* step, but the \* to HO\* step is similarly small, thus can be approximated as the determining step. For Pt, the determining step happens at O\* to HOO\*, but once again the HOO\* to \*+O<sub>2</sub> step is similarly small, so can be approximated as the rate determining step. Now, if we assume  $\Delta G_{HOO^*}$ - $\Delta G_{HO^*}$  is fixed, then the step1+step4 distance is also fixed. If the ORR determining steps happens either in step1 or step4 (the minimum of them), then the ORR overpotential can be determined by the amplitude of step1 (e.g., the  $\Delta G_{HO^*}$ value). Indeed, Fig. 6b shows the volcano plot of the ORR overpotential as a function of  $\Delta G_{HO^*}$ . Theoretically, the minimum overpotential happens when  $\Delta G_{HO^*}$  equals half of the step1+step4 value, as indicated by the dashed line. In reality, Rh, Co and Ir have the minimum overpotentials. The results do fall into the single line volcano curve.

Finally, to evaluate the dynamic stabilities of the efficient Co-V<sub>CC</sub> and Rh-V<sub>CC</sub> catalysts for both OER and ORR, the diffusion barriers of Co and Rh atoms were calculated. As shown in **Fig. S7 and S8**, to

**Fig. 6** (a) The calculated negative overpotential  $(-\eta^{OER})$  against  $\Delta G_{O^*}$ - $\Delta G_{HOO^*}$  on TM-V<sub>CC</sub>, (b) The calculated ORR volcano curve of the  $-\eta^{ORR}$  as the function of  $\Delta G_{HO^*}$  on TM-V<sub>CC</sub>.

ARTICLE Journal Name

diffuse from the defect adsorption site to the neighboring hollow site, Co and Rh atoms need to overcome the energy barriers of 2.47 eV and 1.96 eV, respectively, suggesting that the adsorbed Co and Rh atoms can hardly diffuse to form clusters. Moreover, the AIMD simulations results (**Fig. S9**) show that the energies are oscillating near the equilibrium state, indicating the kinetic stability of Co-V<sub>CC</sub> and Rh-V<sub>CC</sub>. Thus, Co-V<sub>CC</sub> and Rh-V<sub>CC</sub> are indeed highly efficient and stable single-atom catalysts for both OER and ORR.

#### 4. Conclusions

Published on 23 April 2019. Downloaded by Idaho State University on 4/26/2019 11:23:07 AM.

In summary, by using computational screening method, we systematically studied a series of single transition metal atoms anchored on double carbon vacancy of C<sub>3</sub>N monolayer as the active sites for both OER and ORR catalytic processes. It was found that increasing d-electron number can lead to the lower dband center that weakens the interaction strength between intermediates species and the TM atoms. Thus, the ideal TM-V<sub>CC</sub> catalyst for OER and ORR can be screened by adjusting the TM element. The OER overpotential  $\eta^{OER}$  follow a volcano plot of  $\Delta G_{O^*}$ - $\Delta G_{HOO^*}$ , while the ORR overpotential  $\eta^{ORR}$ follow a volcano plot of  $\Delta G_{HO^*}$ . Among all the studied TM-V<sub>CC</sub> catalysts, the best TM atom for OER is Rh- $V_{CC}$  with  $\eta^{OER}$  of 0.35 V, followed by Co- $V_{CC}$  (0.43 V), and for ORR, Rh-V<sub>CC</sub> exhibits the lowest  $\eta^{ORR}$  of 0.27 V, followed by Co-V<sub>CC</sub> (0.42 V). It is also found that Co-V<sub>CC</sub> and Rh-V<sub>CC</sub> are stable against clustering and diffusion. These calculations suggest that Rh-V<sub>CC</sub> and Co-V<sub>CC</sub> are the highly promising candidate as catalysts for both OER and ORR, especially the nonnoble metal catalyst Co-V<sub>CC</sub> can be served as the efficient, stable and low-cost catalyst. Moreover, the catalyst is found to be electrically conductive. Our findings shed light on C<sub>3</sub>N-based materials as efficient OER and ORR catalyst and offer a useful guide to select the active catalytic center of single-atom catalysts on 2D carbon nitride-based materials.

### **Conflicts of interest**

There are no conflicts to declare.

#### **Acknowledgements**

This work was supported by the Assistant Secretary for Energy Efficiency and Renewal Energy of the U.S. Department of Energy under the Hydrogen Generation program. This theoretical work used the resources of the National Energy Research Scientific Computing Center (NERSC) that is supported by the Office of Science of the U.S. Department of Energy. We are

grateful to the Chinese Scholarship Council (CSC) for providing the Ph.D. scholarship and to 39 Sawrence Berkeley National Laboratory (USA) for financial support.

#### Notes and references

- M. S. Dresselhaus and I. L. Thomas, *Nat. Catal.*, 2001, 414, 332–337.
- N. L. Panwar, S. C. Kaushik and S. Kothari, Renew. Sust. Energ. Rev., 2011, 15, 1513-1524.
- G. S. Liu, S. J. You, Y. Tan and N. Q. Ren, *Environ. Sci. Technol.*, 2017, 51, 2339-2346.
- <span id="page-8-0"></span> A. B. Stambouli and E. Traversa, Renew. Sust. Energ. Rev., 2002, 6, 433-455.
- G. P. Gao, Y. Jiao, F. X. Ma, Y. L. Jiao, E. Waclawik and A. J. Du, *J. Catal.*, 2015, 332, 149-155.
- Y. C. Lu, Z. C. Xu, H. A. Gasteiger, S. Chen, K. Hamad-Schifferli and Y. Shao-Horn, J. Am. Chem. Soc., 2010, 132, 12170.
- Y. Jiao, Y. Zheng, M. Jaroniec and S. Z. Qiao, *Chem. Soc. Rev.*, 2015, 44, 2060-2086.
- <span id="page-8-1"></span>E. A. Paoli, F. Masini, R. Frydendal, D. Deiana, C. Schlaup, M. Malizia, T. W. Hansen, S. Horch, I. E. L. Stephens and I. Chorkendorff, *Chem. Sci.*, 2015, 6, 190-196.
- <span id="page-8-2"></span> J. Rossmeisl, Z. W. Qu, H. Zhu, G. J. Kroes and J. K. Nørskov, J. Electroanal. Chem., 2007, 607, 83-89.
- N.M. Markovic, T. J. Schmidt, V. Stamenkovic', and P. N. Ross, Fuel Cells., 2001, 1, 105–116.
- X. Q. Huang, Z. P. Zhao, L. Cao, Y. Chen, E. B. Zhu, Z. Y. Lin,
  M. F. Li, A. M. Yan, A. Zettl, Y. M. Wang, X. F. Duan, T. Mueller and Y. Huang, *Science*., 2015, 348, 1230-1234.
- <span id="page-8-3"></span>K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva and A. A. Firsov, Science., 2004, 306, 666-669.
- <span id="page-8-4"></span>X. P. Gao, Y. N. Zhou, Y. J. Tan, Z. W. Cheng, Q. I. Tang, J. P. Jia, and Z. M. Shen, *Energ. Fuel.*, 2018, 32, 5331–5337.
- 14. M. Shakourian-Fard, H. Heydari and G. Kamath, *Chemphyschem*, 2017, 18, 2328-2335.
- <span id="page-8-5"></span>15. M. Naguib, V. N. Mochalin, M. W. Barsoum and Y. Gogotsi, *Adv. Mater.*, 2014, **26**, 992-1005.
- 16. B. Anasori, M. R. Lukatskaya and Y. Gogotsi, *Nat. Rev. Mater.*, 2017, **2**, 1-17.
- J. C. Lei, X. Zhang and Z. Zhou, Front. Phys., 2015, 10, 107303.
- H. O. Churchill and P. Jarillo-Herrero, Nat Nanotechnol., 2014, 9, 330-331.
- <span id="page-8-6"></span> Y. Li, F. Ma and L. W. Wang, J. Mater. Chem. A., 2018, 6, 7815-7826.
- <span id="page-8-7"></span>X. K. Kong, C. L. Chen and Q. W. Chen, *Chem. Soc. Rev.*, 2014,
   43, 2841-2857.
- X. W. Wang, G. Z. Sun, P. Routh, D. H. Kim, W. Huang and P. Chen, Chem. Soc. Rev., 2014, 43, 7067-7098.
- 22. C. L. Tan, X. H. Cao, X. J. Wu, Q. Y. He, J. Yang, X. Zhang, J. Z.Chen, W. Zhao, S. K. Han, G. H. Nam, M. Sindoro and H. Zhang, *Chem. Rev.*, 2017, 117, 6225-6331.
- <span id="page-8-8"></span>23. G. L. Chai, Z. F. Hou, D. J. Shu, T. Ikeda and K. Terakura, *J. Am*.
  - Chem. Soc., 2014, 136, 13629-13640.
- J. T. Zhang, Z. H. Zhao, Z. H. Xia and L. M. Dai, *Nat. Nanotechnol.*, 2015, 10, 444-452.
- W. Liang, J. X. Chen, Y. W. Liu and S. L. Chen, ACS Catal., 2014, 4, 4170–4177.
- <span id="page-8-9"></span>26. Y. N. Zhou, G. P. Gao, Y. Li, W Chu and L. W. Wang, *Phys. Chem. Chem. Phys.*, 2019, **21**, 3024-3032.

Journal Name ARTICLE

- <span id="page-9-0"></span> S. C. Wang, Z. Y. Teng, C. Y. Wang and G. X. Wang, ChemSusChem, 2018, 11, 2267-2295.
- H. F. Wang, C. Teng and Q. Zhang, Adv. Funct. Mater., 2018, 28, 1803329-1803351.
- P. Z. Chen, T. P. Zhou, L. L. Xing, K. Xu, Y. Tong, H. Xie, L. D. Zhang, W. S. Yan, W. S. Chu, C. Z. Wu and Y. Xie, *Angew. Chem. Int. Ed.*, 2017, 56, 610-614
- X. F. YANG, A. Q. Wang, B. T. Qiao, J. Li, J. Y. Liu and T. Zhang, Acc. Chem. Res., 2013, 46, 1740–1748.
- 31. C. Z. Zhu, S. F. Fu, Q. R. Shi, D. Du and Y. H. Lin, *Angew. Chem. Int. Ed.*, 2017, **56**, 13944-13960.
- 32. J. Mahmood, E. K. Lee, M. Jung, D. B. Shin, H. J. Choi, J. M. Seo, S. M. Jung, D. Kim, F. Li, M. S. Lah, N. Park, H. J. Shin, J. H. Oh and J. B. Baek, *PNAS*., 2016, 113, 7414–7419.
- <span id="page-9-1"></span>X. D. Zhou, W. X. Feng, S. Guan, B. T. Fu, W. Y. Su and Y. G. Yao, *J. Mater. Res.*, 2017, 32, 2993–3001.
- Y. Hong, J. C. Zhang and X. C. Zeng, *Nanoscale.*, 2018, 10, 4301-4310.
- <span id="page-9-2"></span>35. X. F. Li, L. Zhu, Q. Z. Xue, X. Chang, C. C. Ling and W. Xing, *ACS App. Mater. Interfaces.*, 2017, 9, 31161-31169.
- <span id="page-9-3"></span>D. W. Ma, J. Zhang, X.X. Li, C. Z. He, Z. W. Lu, Z. S. Lu, Z. X. Yang and Y. X. Wang, Sensor. Actuat. B-Chem., 2018, 266, 664–673.
- 37. P. Bhauriyal, A. Mahata and B. Pathak, *J. Phys. Chem. C.*, 2018, **122**, 2481–2489.
- <span id="page-9-4"></span>38. J. T. Xu, J. Mahmood, Y. H. Dou, S. X. Dou, F. Li, L. M. Dai and J. B. Baek, *Adv. Mater*, 2017, **29**, 1702007-1702015.
- <span id="page-9-5"></span>B. L. He, J. S. Shen, D. W. Ma, Z. S. Lu and Z. X. Yang, J. Phys. Chem. C., 2018, 122, 20312–20322.
- <span id="page-9-6"></span> M. Makaremi, B. Mortazavi and C. V. Singh, J. Phys. Chem. C., 2017, 121, 18575–18583.
- <span id="page-9-7"></span>41. H. I. Rasool, C. Ophus and A. Zettl, Adv. Mater., 2015, 27, 5771-5777.
- <span id="page-9-8"></span> F. Banhart, J. Kotakoski and A. V. Krasheninnikov, ACS nano., 2011, 5, 26-41.
- <span id="page-9-9"></span>43. Y. N. Tang, Z. X. Yang and X. Q. Dai, *J. Chem. Phys.*, 2011, 135, 224704-224711.
- <span id="page-9-10"></span>44. X. F. Fan, W. T. Zheng and J. L. Kuo, *ACS App. Mater. Interfaces.*, 2012, **4**, 2432-2438.
- G. P. Gao, E. R. Waclawik and A. J. Du, J. Catal., 2017, 352, 579-585.
- T. W. He, S. K. Matta, G. Will and A. J. Du, Small. Methods., 2019, 1800419.
- <span id="page-9-11"></span>47. X. Zhang, A. Chen, Z. H. Zhang, M. G. Jiao and Z. Zhou, *J. Mater. Chem. A.*, 2018, **6**. 11446-11452.
- <span id="page-9-12"></span>48. G. Kresse and J. Furthmuller, Comput. Mater. Sci., 1996, 6, 15-
- <span id="page-9-13"></span>49. G. Kresse and J. Furthmuller, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1996, **54**, 11169–11186.
- <span id="page-9-14"></span> P. E. Blöchl, Phys. Rev. B: Condens. Matter Mater. Phys., 1994, 50, 17953-17979.
- <span id="page-9-15"></span>51. J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, 77, 3865–3868.
- <span id="page-9-16"></span> J. P. Perdew, M. Ernzerhof and K. Burke, *J. Chem. Phys.*, 1996, 105, 9982-9985.
- <span id="page-9-17"></span> S. Grimme, J. Antony, S. Ehrlich and H. Krieg, *J. Chem. Phys.*, 2010, 132, 154104-154123.
- <span id="page-9-18"></span> H. J. Monkhorst and J. D. Pack, *Phys. Rev. B.*, 1976, 13, 5188-5192.
- <span id="page-9-19"></span>55. G. Henkelman, B. P. Uberuaga and H. Jonsson, *J. Chem. Phys.*, 2000, **113**, 9901–9904.
- <span id="page-9-20"></span>G. Henkelman, A. Arnaldsson and H. Jonsson, *Comput. Mater. Sci*, 2006, 36, 354–360.
- <span id="page-9-21"></span> G. J. Martyna, M. L. Klein and M. Tuckerman, J. Chem. Phys., 1992, 97, 2635-2643.

- <span id="page-9-22"></span>58. K. Mathew, R. Sundararaman, K. Letchworth-Weaver Touched Arias and R. G. Hennig, J. Chem. Physiol 201403140970841999 084114.
- <span id="page-9-23"></span> J. K. Nørskov, J. Rossmeisl, A. Logadottir and L. Lindqvist, J. Phys. Chem. B., 2004, 108, 17886-17892.
- <span id="page-9-24"></span>60. M. T. Li, L. P. Zhang, Q. Xu, J. B. Niu and Z. H. Xia, *J. Catal.*, 2014, **314**, 66-72.
- <span id="page-9-25"></span>61. P. Atkins and J. D. Paula, Oxford University Press, 2014.
- <span id="page-9-26"></span>62. H. D. Wang, H. Wu and J. L. Yang, arXiv:1703.08754v1, 2017.
- <span id="page-9-27"></span>63. Y. C. Ma, P. O. Lehtinen, A. S. Foster and R. M. Nieminen, *New. J. Phys.*, 2004, **6**, 68-83.
- <span id="page-9-28"></span> A. A. El-Barbary, R. H. Telling, C. P. Ewels, M. I. Heggie and P. R. Briddon, *Phys. Rev. B.*, 2003, 68, 144107-144114.
- <span id="page-9-29"></span>D. W. Ma, J. Zhang, Y. N. Tang, Z. M. Fu, Z. X. Yang and Z. S. Lu, *Phys. Chem. Chem. Phys.*, 2018, 20, 13517-13527.
- <span id="page-9-30"></span> Y. N. Zhou, W. Chu, F. L. Jing, J. Zheng, W. J. Sun and Y. Xue, *Appl. Surf. Sci.*, 2017, 410, 166-176.
- <span id="page-9-31"></span> H. Tang and S. Ismail-Beigi, Phys. Rev. Lett., 2007, 99, 115501-115505.
- <span id="page-9-32"></span> H. X. Xu, D. J. Cheng, D. P. Cao and X. C. Zeng, *Nat. Catal.*, 2018, 1, 339-348.
- M. Mavrikakis, B. Hammer and J. K. Nørskov, *Phys. Rev. Lett.*, 1998, 81, 2819-2822.
- 70. B. Hammer, J. K. Nørskov, Adv. Catal., 2000, 45, 71–129.
- 71. J. R. Kitchin, J. K. Norskov, M. A. Barteau and J. G. Chen, *Phys. Rev. Lett.*, 2004, **93**, 156801-156805.
- V. Stamenkovic, B. S. Mun, K. J. J. Mayrhofer, P. N. Ross, N. M. Markovic, J. Rossmeisl, J. Greeley and J. K. Nørskov, *Angew. Chem. Int. Ed.*, 2006, 118, 2963-2967.
- <span id="page-9-33"></span>Y. Y. Liu, Y. M. Wang, B. I. Yakobson and B. C. Wood, *Phys. Rev. Lett.*, 2014, 113, 028304-028309.
- <span id="page-9-34"></span> F. Calle-Vallejo, A. Krabbe and J. M. Garcia-Lastra, *Chem. Sci.*, 2017, 8, 124-130.
- <span id="page-9-35"></span>75. M. T. de Groot and M. T. Koper, *Phys. Chem. Chem. Phys.*, 2008, **10**, 1023-1031.
- <span id="page-9-36"></span> C. Y. Ling, L. Shi, Y. X. Ouyang, X. C. Zeng and J. L. Wang, Nano. Lett., 2017, 17, 5133-5139.
- <span id="page-9-37"></span>J. K. Nørskov, T. Bligaard, A. Logadottir, J. R. Kitchin, J. G. Chen, S. Pandelov and U. Stimming, *J. Electrochem. Soc.*, 2005, 152, J23-J26.
- <span id="page-9-38"></span> I. C. Man, H. Y. Su, F. Calle-Vallejo, H. A. Hansen, J. I. Martínez, N. G. Inoglu, J. Kitchin, T. F. Jaramillo, J. K. Nørskov and J. Rossmeisl, *ChemCatChem.*, 2011, 3, 1159-1165.
- J. Rossmeisl, A. Logadottir and J. K. Nørskov, *Chem. Phys.*, 2005, 319, 178-184.

ARTICLE

Published on 23 April 2019. Downloaded by Idaho State University on 4/26/2019 11:23:07 AM.

#### Journal Name

View Article Online DOI: 10.1039/C9TA01389J

The best TM atom for OER is Rh-V<sub>CC</sub> with  $\eta^{OER}$  of 0.35 V, followed by Co-V<sub>CC</sub> (0.43 V), and for ORR, Rh-V<sub>CC</sub> exhibits the lowest  $\eta^{ORR}$  of 0.27 V, followed by Co-V<sub>CC</sub> (0.42 V).

**Graphical abstract** 

View Article Online DOI: 10.1039/C9TA01389J

Transition metal embedded two-dimensional C<sub>3</sub>N as highly active electrocatalysts for oxygen evolution and reduction reactions

Yanan Zhou, <sup>ab</sup> Guoping Gao, <sup>b</sup> Jun Kang, <sup>c</sup> Wei Chu, \*a and Lin-Wang Wang \*b

- <sup>a</sup> School of Chemical Engineering, Sichuan University, Chengdu, 610065, Sichuan, China
- <sup>b</sup> Materials Science Division, Lawrence Berkeley National Laboratory, Berkeley, 94720, California, United States

The best TM atom for OER is Rh-V<sub>CC</sub> with  $\eta^{OER}$  of 0.35 V, followed by Co-V<sub>CC</sub> (0.43 V), and for ORR, Rh-V<sub>CC</sub> exhibits the lowest  $\eta^{ORR}$  of 0.27 V, followed by Co-V<sub>CC</sub> (0.42 V).