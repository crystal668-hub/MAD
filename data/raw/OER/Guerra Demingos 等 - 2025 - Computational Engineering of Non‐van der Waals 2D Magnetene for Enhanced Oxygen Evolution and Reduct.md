---
source: Guerra Demingos 等 - 2025 - Computational Engineering of Non‐van der Waals 2D Magnetene for Enhanced Oxygen Evolution and Reduct.pdf
tool: marker
duration: 60.615s
generated: 2026-01-09T06:41:29.335565Z
---

Check for updates

www.chemsuschem.org

# Computational Engineering of Non-van der Waals 2D Magnetene for Enhanced Oxygen Evolution and Reduction Reactions

Pedro Guerra Demingos, [a] Zhiwen Chen,\*[a] Xiang Ni, [a] and Chandra Veer Singh\*[a]

Non-van der Waals two-dimensional materials containing exposed transition metal atoms are promising catalysts for green energy storage and conversion. For instance, hematene and ilmenene have been successfully applied as catalysts. Building on these reports, this work is the first investigation of recently synthesized magnetene towards the Oxygen Evolution Reaction (OER) and Oxygen Reduction Reaction (ORR). Using Density Functional Theory (DFT) calculations, we unveil the mechanism, performance and ideal conditions for OER and ORR on magnetene. With overpotentials of  $\eta_{OER} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$  and  $\eta_{ORR} = 0.50 \text{ V}$ 

0.41 V, the material is not only a bifunctional catalyst, but also superior to state-of-the-art systems such as Pt and IrO<sub>2</sub>. Additionally, its catalytic properties can be further enhanced through engineering strategies such as point defects and inplane compression. It reaches  $\eta_{ORR}\!=\!0.28\,\mathrm{V}$  at a compressive strain of only 2%, while the presence of Ni boosts it to  $\eta_{OER}\!=\!0.39\,\mathrm{V}$  and  $\eta_{ORR}\!=\!0.31\,\mathrm{V}$ , comparable to many reported single-atom catalysts. Overall, this work demonstrates that magnetene is a promising bifunctional catalyst for applications such as regenerative fuel cells and metal-air batteries.

## Introduction

The development of sustainable energy technologies is crucial in facing the current energy and environmental crisis. Water splitting,<sup>[1]</sup> hydrogen fuel cells<sup>[2,3]</sup> and metal-air batteries<sup>[4]</sup> are promising technologies for environmentally friendly energy conversion and storage, in which the Oxygen Evolution Reaction (OER)<sup>[5]</sup> and the Oxygen Reduction Reaction (ORR)<sup>[6]</sup> play major roles. For instance, the OER is involved in the splitting of  $H_2O$  into  $O_2$  and  $H_{2r}^{[1]}$  which can then be leveraged as a green fuel through the reverse process involving the ORR.[3] Furthermore, OER and ORR must both happen at the cathode surface to allow the charge and discharge cycles of metal-air batteries,[4] which have received great attention owing to their improved economy and safety.<sup>[7]</sup> However, these reactions are slow four-electron processes, making it necessary the usage of catalysts, with the most widely used commercial options being Pt for the ORR, [8] and RuO<sub>2</sub> and IrO<sub>2</sub> for the OER. [9] Despite their good activity, however, these materials suffer from prohibitively high cost.[10,11] Moreover, systems with good OER performance are often poor ORR catalysts, and vice-versa. [12,13] Since mixing two catalysts with good individual performance increases both cost and manufacturing complexity,<sup>[14]</sup> there is great interest in the development of low-cost bifunctional materials, i.e. materials that can catalyze both reactions.

Two-dimensional (2D) materials are promising for heterogeneous catalysis owing to their high surface-to-volume ratio combined with enhanced carrier mobility.[15] Successful examples include transition-metal chalcogenides and dichalcogenides (TMCs/TMDs),[16,17] carbon nitrides (C<sub>3</sub>N<sub>4</sub>),[18,19] covalent organic frameworks (COFs), [20] metal-organic frameworks (MOFs),<sup>[21]</sup> among others.<sup>[22]</sup> In particular, 2D materials can display OER/ORR bifunctionality, which makes them suitable for application in metal-air batteries. For instance, Zheng et al. successfully applied a hybrid of bimetallic CoNi-MOF nanosheets and reduced graphene oxide, [23] while Li et al. reported the application of 2D framework porphyrin materials.<sup>[24]</sup> In most cases, however, modifications are needed in order to reach bifunctionality. [25] For example, transition metal atoms can be immobilized on the surface of 2D materials, yielding singleatom catalysts (SACs) which display low cost and high atomic utilization.[26] For instance, Ma et al. dispersed FeN<sub>4</sub> and NiN<sub>4</sub> onto N-doped graphene to design a bifunctional catalyst that was leveraged for Zinc-air batteries.[27] SACs have also been widely investigated theoretically. For example, MXene-based SACs show OER (ORR) overpotentials as low as 0.29 (0.35) V across different systems.[28] Furthermore, the usage of black phosphorus carbide as substrate yielded 0.21 (0.21) V overpotentials on the same Ir active site.[29] However, in order to fully leverage the advantages of 2D morphology and to move past the need for complex synthesis processes, low cost materials with intrinsic bifunctionality must be developed. [30]

Non-van der Waals (non-vdW) 2D materials are a sub-class of 2D materials that do not have a layered bulk analogue, therefore displaying a high density of dangling bonds that

Correspondence: Dr. Zhiwen Chen and Dr. Chandra Veer Singh, Department of Materials Science and Engineering, University of Toronto, 184 College Street, Toronto ON M5S 3E4. Email: zhiw.chen@utoronto.ca and chandraveer.singh@utoronto.ca

<sup>[</sup>a] Department of Materials Science and Engineering, University of Toronto, Toronto

Supporting Information for this article is available on the WWW under https://doi.org/10.1002/cssc.202401157

<sup>© 2024</sup> The Authors. ChemSusChem published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution Non-Commercial NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

make them promising for applications in energy storage and conversion.[31] Specifically, many of them have subcoordinated transition metal atoms at their surface without the need for modifications. Furthermore, these materials often benefit from superior abundance, stability and ease of processing when compared to conventional 2D materials.[31] In terms of applications, metallic materials such as PtPb/Pt core/shell nanoplates are promising for the ORR, with specific and mass activities of 7.8 mA/cm<sup>2</sup> and 4.4 A/mg at 0.9 V versus RHE.[32] Meanwhile, Cocontaining systems have high performance towards the OER: Co3O4 nanosheets displayed a current density of 12.26 mA/cm2 at 0.8 V (vs Hg/HgO) and long-term stability,[33] while Co9S8 nanosheets presented an overpotential of 0.27 V at 10 mA/ cm<sup>2</sup> . [34] Furthermore, non-vdW 2D iron oxides are promising towards the OER: both hematene (Fe2O3) [35] and ilmenene (FeTiO3) [36] have been applied as OER catalysts, with defective hematene reaching a current density of 10 mA/cm2 at an overpotential of 0.25 V.[37] Finally, ultrathin spinel hausmannitene (Mn3O4) exhibited catalytic activity towards both OER and

ORR.[38] Magnetene (Fe3O4) is another entry in the family of nonvdW 2D materials derived from iron ores, similarly to hematene and ilmenene.[39] It is exfoliated from magnetite, which is an abundant mineral that has been widely studied as an OER catalyst.[40,41] Magnetene is believed to be a ferrimagnetic material with a small band gap of 0.35 eV along its majority spin channel,[39] much smaller than the 1.80 eV gap of hematene.[35] While hematene has good electro-catalytic performance towards the OER,[37] based on band gap it can be expected that magnetene will outperform hematene. Despite the successes of its analogues hematene and ilmenene for the OER, however, to date magnetene has not been explored towards catalysis.

Therefore, in this work we use Density Functional Theory (DFT) calculations to demonstrate the great potential of magnetene as an OER/ORR bifunctional catalyst. Firstly we compare three different active sites across a pristine and a hydroxylated system in order to unveil the most likely catalysis mechanism as well as its optimal conditions. Secondly we investigate different strategies to engineer the material for enhanced catalysis, reporting the effect of oxygen vacancies, Ni and Co substitutions, and externally applied compressive strain. Finally we compare the different systems under the light of their electronic structure, explaining the superior performance of magnetene when compared to state-of-the-art catalysts such as Pt and IrO2.

## **Results and Discussion**

#### **Structure and Stability**

The structure of magnetene is shown in Figure 1. We model it following exfoliation along (110) facets, as this is the most likely arrangement of the real material based on both its experimental characterization[39] and a previous theoretical investigation of the stability of different magnetite surfaces.[42] Similarly to a

**Figure 1.** Structure of magnetene from top, front and side views. Unit cell, lattice parameters and active catalytic sites A, B and C are indicated.

previous DFT study of magnetene,[43] we include four atomic layers in order to (1) maintain the bulk stoichiometry Fe3O4, and (2) so that the stacking of magnetene layers would convert back into bulk magnetite. The relaxed structure of magnetene is therefore shown in Figure 1, with lattice parameters *a* ¼ 8*:*29Å, *b* ¼ 6*:*23Å and g ¼ 90� . Experimental characterization suggests it is a magnetic material at room temperature,[39] which is confirmed by our DFT calculations: magnetene displays a ferrimagnetic ground state with net magnetization of 4.83μ*<sup>B</sup>* per unit formula, with its other magnetic states summarized in Table S1. In the ferrimagnetic ground state, each of its two Fe<sup>3</sup><sup>+</sup> per unit formula has spin up, and its one Fe<sup>2</sup><sup>+</sup> per unit formula has spin down. Different active sites are expected to have different physical and chemical properties,[44] including OER/ ORR activity. As shown in Figure 1a, the surface of magnetene has three different Fe sites that are available for catalysis, namely A, B and C, whose properties are summarized in Table S2, including partial charge, magnetic moment and coordination number.

In order to assess the suitability of magnetene as a catalyst, we first discuss its stability. The main indicative that the material is stable is the fact that it has been successfully synthesized[39] and characterized,[43] and additional demonstrations can be made with DFT. For instance, the mechanical stability of a system depends on its elastic constants. Despite its structural anisotropy, magnetene has similar *C*11=174 GPa and *C*22=173 GPa, as well as *C*12=72 GPa and *C*66=151 GPa, making its elastic behavior similar to that of other 2D materials according to both theory and experimental characterization.[45] These values obey the necessary and sufficient relations for elastic stability in an orthorhombic 2D system, i. e. *C*11*>*0, *C*22*>*0, *C*11*C*22*>C*<sup>2</sup> <sup>12</sup> and *C*66*>*0.[46] Moreover, ab initio molecular dynamics (AIMD) simulations of a 2x2 supercell at 300 K showed no structural changes within 10 ps, as shown in Figure S1, which demonstrates thermal stability. Overall, these results suggest that the system used here to model magnetene is indeed stable.

### **Catalysis Mechanism**

Catalysis on a material can be studied by calculating the free energies of adsorption of the intermediate species on its active site.[8] Following the conventional adsorption evolution mechanism (AEM) for OER in an acidic environment, the intermediates are \*OH, \*O and \*OOH, which happen in the reverse order for the ORR. On magnetene, these will adsorb on site A, B or C, which are indicated in Figure 1. The intermediates adsorb on sites A and B through bonding with a single Fe atom, while on site C they bond to two Fe atoms. Figure 2a illustrates this catalytic process, while the adsorption energies are displayed in Figure 2b. A more detailed description of this well-established mechanism is provided in the Methods section. The main outcome of this analysis is the theoretical overpotential *η*, which comes from the maximum energy step of the reaction. This estimation is crucial as it is proportional to the experimental overpotential for metal oxides.[47] Estimated *ηOER* on sites A, B and C, respectively, is 0.75, 0.74 and 0.50 V, while *ηORR* is 0.61, 0.41 and 1.23 V. While all sites are equally available, these values suggest that on magnetene the OER will happen faster on site C, while the ORR will happen faster on site B. The limiting step of the OER on any magnetene site is \*OH!\*O, and for the ORR it is \*OH!H2O on two out of three sites (B and C). This illustrates the relative stability of OH groups on the surface of magnetene, especially on site C where D*Gads* � 0. This is supported by its experimental characterization, which suggests that the material is partially passivated by OH groups.[39,43] We note that DFT predicted pristine and defective hematene to have *ηOER* of 1.39 and 1.28 V, respectively, with the latter having an experimental current density of 10 mA/cm<sup>2</sup> at an overpotential of 0.25 V.[37] Meanwhile, bulk magnetite has a DFT-predicted *ηOER* of 0.67–0.73 V,[41] and hausmannitene has *ηOER* (*ηORR*) of 0.85 (0.90) V.[38] Therefore magnetene is expected to outperform not only its bulk analogue magnetite, but also its 2D cousins hematene and hausmannitene. Furthermore, as we discuss in the last section, magnetene is also superior to benchmark state-of-the-art catalysts such as IrO2 and Pt.

Inspired by the stability of the \*OH adsorbate, we investigated the OER/ORR mechanism on hydroxylated magnetene as well, which correlates with catalysis in an alkaline environment. With OH already present on the Fe sites, the intermediates are \*O, \*OOH and \*OO,[48,49] as illustrated in Figure 2c. Similarly to the process in acidic environment, this mechanism involves four steps. Step 1 is the nucleophilic attack of OH onto adsorbed OH, forming adsorbed \*O and ejecting H2O+e . Step 2 is a second OH attack, forming adsorbed \*OOH and ejecting e . Step 3 is a third OH attack, forming adsorbed \*OO and ejecting H2O+e . Step 4 is a fourth OH attack, regenerating adsorbed OH and ejecting O2+e . As shown in Figure 2d, for every site (A, B and C) the limiting step for OER is the formation of \*O, again demonstrating the stability of OH groups on the surface. For this mechanism, *ηOER* on sites A, B and C is, respectively, 0.88, 1.16 and 1.04 V, while *ηORR* is 0.81, 0.76 and 0.49 V. For both OER and ORR, these values are greater than those found for the bare material, showing that OH coverage is not desired when applying magnetene as a catalyst. Since this mechanism is common in alkaline media, these results also show that magnetene performs better in acidic and neutral environments where OH coverage is less likely. We note that, according to the XPS characterization of non-vdW 2D iron oxides, magnetene has lesser OH coverage than other materials

**Figure 2.** Catalysis on magnetene. (a,c) Catalysis mechanism on site A and (b,d) free energy diagram for every active site on magnetene. (a,b) Bare magnetene and (c,d) hydroxylated magnetene.

such as hematene and chromiteen, which favors its lubricant properties.[43] As we have demonstrated here, this characteristic will also enhance its catalytic activity.

Other mechanisms and catalysis conditions are possible for OER/ORR.[41,50–53] For instance, in the lattice oxygen mechanism (LOM) an oxygen atom is removed from the lattice and then regenerated during the reaction.[50] This is different from a preexisting oxygen vacancy, which is discussed in the next section. The LOM has been reported to have a much higher overpotential on RuO2 than the AEM, making it less likely to happen.[50] However, the LOM is favored by the increase in the covalency of metal-oxygen bonds in MXene-based SACs.[51] Furthermore, real catalysis conditions may affect the stability and activity of magnetene surfaces. For instance, surface reconstructions have been observed and investigated on magnetite towards the OER.[41] Finally, a methodology was recently developed to explicitly account for higher pH values in computational catalysis.[53] All these aspects can be explored in future studies.

#### **Engineering Strategies**

Surface oxygen vacancies enhance the catalytic activity of nonvdW materials such as In2O3 [54] and hematene.[37] Therefore we studied the effects of pre-existing oxygen vacancies on the OER/ORR performance of magnetene, starting with their stability. There are six inequivalent oxygen atoms in the structure as displayed in Figure 3a, and the formation energy of their respective vacancies is shown in Figure 3b, all falling below 1.71 eV. These values are smaller than the ones predicted for magnetite surfaces at 2.60–3.28 eV,[55] and suggest that any oxygen vacancies in magnetene will tend to diffuse to positions *i* and *ii.* Interestingly, exposed vacancies are not necessarily more stable than inner ones. Instead, the formation energy correlates with whether the magnetene structure is able to relax around the vacancy to accomodate its local stress. For instance, the inner vacancy *vi* has lower formation energy than the outer vacancy *iii* because the iron atoms left subcoordinated by *vi* are able to move more upon relaxation, as shown in Figure S3. This effect has been discussed for other 2D materials such as MXenes.[56] To the best of our knowledge, this is the first analysis on the formation of any defects in magnetene.

Since the outer vacancies *i* and *ii* have the lowest formation energies, we explore them in more detail to illustrate the effect of surface oxygen vacancies on the catalytic performance of magnetene. Following the conventional adsorption evolution mechanism, Figure 3c illustrates the OER/ORR steps on vacancy *i*, in which the intermediate species replace the vacant oxygen.[57] Figure 3d shows the energy profile for the reaction on both vacancies, showcasing a relatively high stability of species \*OH and \*O when replacing a removed oxygen. As a result, from the OER perspective, the energy steps to form \*OOH and desorb O2 are relatively large, leading to *ηOER* of 1.38 and 1.36 V for vacancies *i* and *ii*, respectively. From the ORR point of view, the desorption of H2O from \*OH is the limiting step, leading to *ηORR* of 1.86 and 1.98 V, which are too high for practical use. Consequently, unlike hematene, magnetene does not benefit from surface oxygen vacancies when applied as an OER/ORR catalyst. We note that, despite the low formation energy of vacancies *i* and *ii*, this conclusion does not indicate that the performance of magnetene will be poor. On the contrary, these positions are likely to function as vacancy attractors, leaving active sites B and C to benefit from greater

**Figure 3.** Point defects and their effect on catalysis. (a) Oxygen vacancy positions. (b) Their formation energy. (c) Catalysis mechanism on an oxygen vacancy at position *i.* (d) Free energy diagram for this catalysis mechanism on different vacancy positions. (e,f) Free energy diagrams for Ni and Co substitutions at different active sites on magnetene.

coordination. As we discussed previously, these are the most active sites in pristine magnetene.

Next we look into the effect of impurities on the catalytic performance of magnetene. Specifically, we investigate Ni and Co substitutions at Fe active sites, since these two metallic species typically yield low overpotentials for OER/ORR. Furthermore, these cases are relevant for three more reasons. Firstly, impurities can exist in naturally occuring magnetite, from which magnetene is exfoliated.[58] Secondly, the amount of these metals can be increased in the material through synthesis or post-processing techniques such as heating under anoxic conditions.[59–61] Thirdly, other naturally occuring ores have the same structure as magnetite but stoichiometric ammounts of Ni or Co, for instance trevorite.[62] In addition, systems such as CoFe2O4, [63] NiFe2O4, [64] Co-doped Fe3O4 [65] and Ni-doped Fe3O4 [66] have been prepared and applied for the OER and/or ORR. In order to demonstrate the feasibility of producing Ni and Co substitutions on magnetene, we have calculated their formation energy by taking as reference the most stable phases of iron, nickel and cobalt. As shown on Table S3, all values are below 1.38 eV, which is low compared with the formation energy of point defects in graphene[67] and other 2D materials.[68,69] Therefore, these results demonstrate the possibility of introducing Ni and Co onto magnetene.

Following the convetional adsorption evolution mechanism, Figure 3e,f shows the energy pathway of OER/ORR on Ni/Comodified magnetene, which again showcase the relative stability of \*OH. Based on the calculated overpotentials, both Ni and Co enhance the catalytic performance of the material towards the OER. For Ni placed at sites A, B and C, *ηOER* is 0.79, 0.39 and 0.90 V, while for Co *ηOER* is 1.04, 0.47 and 0.98 V, respectively. This shows that the most active site is shifted from C to B upon Ni/Co substitution. When it comes to the ORR, Ni placed on sites A, B and C leads to *ηORR* of 0.67, 0.31 and 1.08 V, respectively, while for Co *ηORR* is 0.90, 0.57 and 1.12 V. This shows that, while Co is less active than Fe for the ORR on magnetene, Ni enhances catalysis considerably: from an *ηORR* of 0.41 V in the pristine material to only 0.31 V in the modified system. Interestingly, in all three cases the most active site for the ORR is B, making Ni@B a bifunctional site for OER/ORR catalysis with low *ηOER* (*ηORR*) of 0.39 (0.31) V. This performance is competitive with that of many reported bifunctional SACs, including Ni- and Co-based ones,[70,71] as well as the optimal Pd on 1T-MoSe2 at 0.49 (0.32) V[72] and the optimal Rh on g-C3N4 at 0.32 (0.43) V.[73] When it comes to graphene-based SACs, several values have been reported, for instance Ni-C4 at 0.31 (0.43) V and Rh-N4 at 0.31 (0.36) V, according to a revised PBE with Tkatchenko Scheffler methodology (RPBE-TS).[74]

Another way to tune the catalytic properties of a material is by applying strain to the system.[75] Although the mechanism behind this effect can be complicated, in essence when a *d*band metal is strained in tension, there is less *d*-orbital overlap and therefore narrower *d*-band width. This causes an upwards shift of the *d*-band center, strenghtening interactions between surface and adsorbate. In compression, the opposite happens. Furthermore, studying the effects of strain is particularly relevant for 2D materials since there are several ways to induce tension or compression in these systems, for instance by using substrates with a mismatched lattice[76] or a flexible substrate that can undergo bending or stretching.[77]

Motivated by this, we investigated the effect of strain on the catalytic properties of magnetene. The OER is particularly interesting in this regard: its active site on the material (site C) bonds to the intermediates through two Fe O bonds, therefore we hypothesize that \*O will remain relatively more stable under applied strain when compared to \*OH and \*OOH, in which the bonding oxygen makes three bonds in total. This hypothesis is confirmed by our calculations. Firstly, the expected effect is observed on the electronic properties of the active sites: their *d*band center decreases under compression along the *a* axis, as shown in Figure 4a. This, in turn, causes the adsorption energies to shift, but not in a proportional way. As shown in Figure 4b, at ~0.07 compressive strain the limiting step for the OER changes from \*O formation to \*O decomposition, clearly indicating an increase in its stability. As a result, *ηOER* is reduced to 0.41 eV. As

**Figure 4.** Effect of compressive strain applied to the *a* direction. (a) Shift in *d*-band center of different active sites. (b,c) Shifts in different steps of the OER and ORR, respectively, with changes of the limiting step.

shown in Figure 4c, the ORR case is more complex, with three steps being alternated as the highest activation energy. Nonetheless, compression along the *a* axis reduces *ηORR* to 0.28 eV at 0.02 compression. These results show that magnetene is not only a tunable catalyst, but also a powerful platform for studying the effects of applied strain on catalytic performance.

## **Comparative Performance and Insights from Electronic Structure**

We now compare the OER/ORR performance of the previously discussed systems. The overpotentials are summarized in Figure 5a, where red asterisks denote the two most promising materials. Pristine magnetene has *ηOER* (*ηORR*) of 0.50 (0.41) V on site C (B), while the modified system with Ni@B has *ηOER* (*ηORR*) of 0.39 (0.31) V. Both materials have lower overpotentials than the benchmark IrO2 (Pt) of 0.65 (0.43) V for OER (ORR),[9,78] demonstrating not only their superior performance but also bifunctionality. In fact, these values are close to the theoretical limit for the OER/ORR overpotential through the conventional adsorption evolution mechanism.[47] Ideally one would want intermediates that are equally spaced in energy in order to minimize the activation energy for the reaction, the best-case scenario being steps of 1.23 eV leading to an overpotential of zero. However, since the intermediate species are similar and therefore all bond to the metal through an oxygen bond, their adsorption energies follow linear scaling relationships that deviate from the 1.23 eV steps. As a result, the minimum overpotential expected for OER/ORR catalysts is 0.20–0.40 eV. Therefore, the performance of magnetene is within the theoretical limit that is possible without breaking linear scaling relationships. These relationships are present in the studied magnetene systems, as shown in Figure 5b, following similar equations as those reported in the literature.[71]

Another way to visualize and compare the performance of different materials is through volcano plots, as shown in Figure 5c,d. This is a quantitative expression of the Sabatier principle, which states that the interactions between the catalyst and the adsorbed molecules should have intermediate strength, since if they are too weak the reagents will fail to bind, whereas if they are too strong the product will fail to dissociate.[79] Therefore we plot the OER overpotential against D*G*(\*O) D*G*(\*OH), and ORR overpotential against D*G*(\*OH). This approach is typically used in the literature,[70,71] and the volcano shape obtained here confirms that these descriptors can be used to capture the catalytic behavior of magnetene towards OER/ORR. According to the plots, the optimal performance for OER happens at D*G*(\*O) D*G*(\*OH) �1.6 eV, and for ORR it happens at D*G*(\*OH) �1.0 eV. This means that the ideal bifunctional catalyst would have D*G*(\*O) �2.6 eV, which is closely reached by Ni@B with D*G*(\*O)=2.56 eV, explaining its optimal performance for both reactions. Furthermore, the plots help illustrate why other systems yield large overpotentials, such as the material with vacancies: the negative value of D*G*(\*OH) impacts the ORR performance, while the proximity D*G*(\*OH) � D*G*(\*O) enlarges the OER overpotential. Finally, we note that the same systems stand near the vertex of the volcano for the two reactions: the previously discussed pristine magnetene (Fe) and modified Ni@B (Ni), both of which have lower overpotential than the benchmarks displayed as green lines.

**Figure 5.** Compared performance. (a) OER and ORR overpotentials across different systems: pristine, hydroxylated (OH), with vacancies (Vac), and with Ni and Co substitutions. (b) Linear scaling relationships. (c,d) Volcano plots.

1864564x, 2025, 3, Downloaded from https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.202401157 by University Of Science, Wiley Online Library on [07/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

The electronic structure of a material can provide great insight into its catalytic properties. A key parameter is the center of the *d*-band of the active transition metal site: higherenergy *d* states generate higher energy antibonding states, which are more reactive and therefore lead to stronger adsorption.[79] Therefore we plotted the *d*-electron-projected Density of States of atoms Fe, Co and Ni placed at magnetene sites A, B and C, as shown in Figure S3. Although it is not trivial to make comparisons between different active sites, a trend can be pointed out. The most active sites Fe@C and Ni@B have high-energy *d*-band centers, indicating that their superior catalytic performance is due to strong catalyst-substrate interactions. This is further illustrated by the adsorption energy of intermediates on Fe@C (Figure 1b), which tend more towards negative values than Fe@A and Fe@B. Furthermore, as shown in Figure S4, there is a correlation in which higher *d*-band centers favor lower overpotentials. However, this interaction strength is not the only effect at play. In fact, from the definition of the OER/ORR overpotentials one would want intermediate steps with equally spaced energies.[47] Ni@B is closer to this picture than Ni@C, despite the latter having lower adsorption energies, which explains the superior catalytic performance of the former.

# **Conclusions**

Using DFT, we have systematically investigated the catalytic performance of magnetene towards OER and ORR. OER happens preferably on active site C with *ηOER*=0.50 V, while ORR happens preferably on site B with *ηORR*=0.41 V. For both reactions, the presence of a hydroxyl coverage layer is detrimental to catalytic performance. Oxygen vacancies have formation energy below 1.71 eV, and their presence increases overpotential. Interestingly, placements with the lowest formation energies might act as vacancy attractors, keeping them away from active sites B and C where the reactions take place. Ni and Co impurities, on the other hand, boost catalysis, especially in the case of Ni at the B site: *ηOER*=0.39 V, *ηORR*= 0.31 V. These impurities can be introduced with formation energies below 1.38 eV. Comparing across all these systems, the free energy of the intermediates \*OH, \*O and \*OOH were found to follow linear scaling relationships and to give rise to volcano plots. Finally, compression of the pristine material along the *a* axis results in a decrease of the *d*-band center energy and consequential improvement of the catalytic performance, with lowest *ηOER* of 0.41 V at 7% strain and lowest *ηORR* of 0.28 V at 2% strain. Overall, these results not only point out magnetene as a bifunctional catalyst with performance superior than its analogues magnetite and hematene, but also than benchmark systems like Pt and IrO2, therefore being apar with many reported single-atom catalysts. We hope this work will spark further interest on magnetene as a functional material, leading to applications in water splitting, green fuel cells, and next generation battery devices.

# **Computational Details**

DFT calculations were performed with Hubbard's correction (DFT+U) with *U* ¼ 4*:*0 eV for Fe atoms, as previously reported for magnetene. Calculations were done with the GGA/PBE approximation, PAW pseudopotentials, and a wave-plane basis set as implemented in the VASP software.[80] Spin-polarization was included, with the ferrimagnetic ground state of magnetene used in all calculations. Dispersion forces were accounted for with Grimme's D3 correction. An energy cutoff of 550 eV was used along with a Gamma-centered k-point mesh of 7×5×1. A vacuum of 15 Å was added in the *z* direction in order to avoid spurious interactions between images across the periodic boundaries of the system. Calculations were performed with an energy threshold of 10 <sup>5</sup> eV, and ionic relaxation was performed for all systems until forces were lower than 10 <sup>2</sup> eV/ Å. AIMD simulations were performed at 300 K using the Nosé-Hoover thermostat and a timestep of 2 fs.

Unless stated otherwise, the modelling of the OER was done through the conventional adsorption evolution mechanism (AEM), which happens in four steps that are described in the SI as well as the literature.[71] In acidic environments, the chemical reactions of the four steps are:

$$^* + H_2O_{(f)} \rightarrow ^*OH + (H^+ + e^-)$$
 (1)

$$^*OH \to ^*O + (H^+ + e^-)$$
 (2)

$$^*O + H_2O_{(I)} \rightarrow ^*OOH + (H^+ + e^-)$$
 (3)

\*OOH 
$$\to$$
 \* + O<sub>2</sub>( $g$ )+(H<sup>+</sup>+e<sup>-</sup>) (4)

While the global OER is:

$$2H_2O_{(I)} \rightarrow O_2(g) + 4(H^+ + e^-)$$
 (5)

And the ORR is the reverse process.

Taking the OER as an example, each elementary step has a free energy change: Δ*G*1, Δ*G*2, Δ*G*<sup>3</sup> and Δ*G*4, respectively. These can be calculated with:

$$\Delta G_1 = \Delta G_{^{*}OH} \tag{6}$$

$$\Delta G_2 = \Delta G_{^{*}O} - \Delta G_{^{*}OH} \tag{7}$$

$$\Delta G_3 = \Delta G_{^{*}OOH} - \Delta G_{^{*}O} \tag{8}$$

$$\Delta G_4 = 4.92 - \Delta G_{^*OOH} \tag{9}$$

where D*G*�*OH*, D*G*�*<sup>O</sup>* and D*G*�*OOH* are the free energies of formation of \*OH, \*O and \*OOH, respectively. Here, the 4.92 eV comes from the experimental energy of the reaction 2H2O ! 2H2+O2. [71] The D*G* values, in turn, can be computed using the Computational Hydrogen Electrode (CHE) model.[78] We start with:

Chemistry Europe

European Chemical Societies Publishing

$$\Delta G = \Delta E_{ele} + \Delta ZPE - T\Delta S \tag{10}$$

where  $\Delta E_{ele}$  is the electronic energy calculated from DFT,  $\Delta ZPE$ is the zero-point energy, T is the temperature (298.15 K), and S is the entropy. For the adsorbed species, the terms  $\triangle ZPE$  and TSare estimated using DFT calculations of the vibrational frequencies (with the aid of VASPKIT<sup>[81]</sup>), while for the molecules they are taken from standard thermodynamic tables.

In order to compute these changes in energy upon formation of adsorbed species, one must take into consideration the chemical potential of oxygen and hydrogen atoms, which are computed from the molecules H<sub>2</sub> and H<sub>2</sub>O. By doing so we are taking the energy of the proton-electron pair as half of that of H<sub>2</sub> at 298.15 K, following the CHE model. <sup>[78]</sup> The changes in energy are calculated from:

$$\Delta E_{ele}(^{*}OH) = E_{ele}(^{*}OH) - E(^{*}) - [E_{ele}(H_{2}O) - 0.5E_{ele}(H_{2})]$$
(11)

$$\Delta E_{ele}(^{*}O) = E_{ele}(^{*}O) - E(^{*}) - [E_{ele}(H_{2}O) - E_{ele}(H_{2})]$$
(12)

$$\Delta E_{ele}(^{*}OOH) = E_{ele}(^{*}OOH) - E(^{*})$$

$$-[2^{*}E_{ele}(H_{2}O) - 1.5E_{ele}(H_{2})]$$
(13)

Finally, the overpotential is calculated from the free energy change of the determining step. For the OER and ORR, respectively:

$$\eta_{OER} = \frac{max[\Delta G_1, \Delta G_2, \Delta G_3, \Delta G_4]}{e} - 1.23V$$
(14)

$$\eta_{ORR} = \frac{max[-\Delta G_1, -\Delta G_2, -\Delta G_3, -\Delta G_4]}{e} + 1.23V \tag{15}$$

where e is the elementary charge.

## **Acknowledgments**

The authors acknowledge the Research Alliance of Canada for computational resources and the Natural Sciences and Engineering Research Counsel (NSERC) for funding. Additionally, PGD acknowledges the University of Toronto, the Ontario Graduate Scholarship (OGS), and the Vanier Canada Graduate Scholarship (CGV-186898) for funding.

#### Conflict of Interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

- [1] Z. P. Ifkovits, J. M. Evans, M. C. Meier, K. M. Papadantonakis, N. S. Lewis, Energy Environ. Sci. 2021, 14, 4740.
- [2] M. K. Singla, P. Nijhawan, A. S. Oberoi, Environmental Science and Pollution Research 2021, 28, 15607.
- [3] M. Aminudin, S. Kamarudin, B. Lim, E. Majilan, M. Masdar, N. Shaari, Int. J. Hydrogen Energy 2023, 48, 4371.
- [4] Y. Chen, J. Xu, P. He, Y. Qiao, S. Guo, H. Yang, H. Zhou, Sci. Bull. 2022.
- [5] N.-T. Suen, S.-F. Hung, Q. Quan, N. Zhang, Y.-J. Xu, H. M. Chen, Chem. Soc. Rev. 2017, 46, 337.
- [6] X. Tian, X. F. Lu, B. Y. Xia, X. W. D. Lou, Joule 2020, 4, 45.
- [7] V. V. Kulish, O. I. Malyi, C. Persson, P. Wu, Phys. Chem. Chem. Phys. 2015, 17, 13921.
- [8] J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard, H. Jonsson, J. Phys. Chem. B 2004, 108, 17886.
- [9] J. Rossmeisl, Z.-W. Qu, H. Zhu, G.-J. Kroes, J. K. Nørskov, J. Electroanal. Chem. 2007, 607, 83.
- [10] C. Sealy, Mater. Today 2008, 11, 65.
- [11] Y. Li, S. Guo, Nano Today 2019, 28, 100774.
- [12] Z. Xue, X. Zhang, J. Qin, R. Liu, J. Energy Chem. 2021, 55, 437.
- [13] E. Antolini, ACS Catal. 2014, 4, 1426.
- [14] Z.-F. Huang, J. Wang, Y. Peng, C.-Y. Jung, A. Fisher, X. Wang, Adv. Energy Mater. 2017, 7, 1700544.
- [15] F. R. Fan, R. Wang, H. Zhang, W. Wu, Chem. Soc. Rev. 2021, 50, 10983.
- [16] Y. Liu, J. Wu, K. P. Hackenberg, J. Zhang, Y. M. Wang, Y. Yang, K. Keyshar, J. Gu, T. Ogitsu, R. Vajtai, et al., Nat. Energy 2017, 2, 1.
- [17] Y. Liu, X. Hua, C. Xiao, T. Zhou, P. Huang, Z. Guo, B. Pan, Y. Xie, J. Am. Chem. Soc. 2016, 138, 5087.
- [18] L. Wang, X. Zhang, X. Yu, F. Gao, Z. Shen, X. Zhang, S. Ge, J. Liu, Z. Gu, C. Chen, Adv. Mater. 2019, 31, 1901965.
- [19] W. Xue, D. Huang, J. Li, G. Zeng, R. Deng, Y. Yang, S. Chen, Z. Li, X. Gong, B. Li, Chem. Eng. J. 2019, 373, 1144.
- [20] F.-M. Zhang, J.-L. Sheng, Z.-D. Yang, X.-J. Sun, H.-L. Tang, M. Lu, H. Dong, F.-C. Shen, J. Liu, Y.-Q. Lan, Angew. Chem. Int. Ed. 2018, 57, 12106.
- [21] A. Dhakshinamoorthy, A. M. Asiri, H. Garcia, Adv. Mater. 2019, 31, 1900617.
- [22] X. Wu, S. Xiao, Y. Long, T. Ma, W. Shao, S. Cao, X. Xiang, L. Ma, L. Qiu, C. Cheng, et al., Small 2022, 18, 2105831.
- [23] X. Zheng, Y. Cao, D. Liu, M. Cai, J. Ding, X. Liu, J. Wang, W. Hu, C. Zhong, ACS Appl. Mater. Interfaces 2019, 11, 15662.
- [24] B.-Q. Li, S.-Y. Zhang, X. Chen, C.-Y. Chen, Z.-J. Xia, Q. Zhang, Adv. Funct. Mater. 2019, 29, 1901301.
- [25] X. Wu, S. Xiao, Y. Long, T. Ma, W. Shao, S. Cao, X. Xiang, L. Ma, L. Qiu, C. Cheng, et al., Small 2022, 18, 2105831.
- [26] R. Gusmão, M. Vesely, Z. Sofer, ACS Catal. 2020, 10, 9634.
- [27] Y. Ma, H. Fan, C. Wu, M. Zhang, J. Yu, L. Song, K. Li, J. He, Carbon 2021, 185, 526,
- [28] Y. Dai, X. Zhao, D. Zheng, Q. Zhao, J. Feng, Y. Feng, X. Ge, X. Chen, J. Colloid Interface Sci. 2024, 660, 628.
- [29] D. Chen, Z. Chen, Z. Lu, X. Zhang, J. Tang, C. V. Singh, Nanoscale 2020,
- [30] X. Yang, H. Liu, Z. Qu, Y. Xie, Y. Ma, Chem. Sci. 2022, 13, 11048.
- [31] A. P. Balan, A. B. Puthirath, S. Roy, G. Costin, E. F. Oliveira, M. Saadi, V. Sreepal, R. Friedrich, P. Serles, A. Biswas, et al., Mater. Today 2022.
- [32] L. Bu, N. Zhang, S. Guo, X. Zhang, J. Li, J. Yao, T. Wu, G. Lu, J.-Y. Ma, D. Su, et al., Science 2016, 354, 1410.
- [33] Y. Dou, T. Liao, Z. Ma, D. Tian, Q. Liu, F. Xiao, Z. Sun, J. H. Kim, S. X. Dou, Nano Energy 2016, 30, 267.
- [34] Z. Wu, H. Zou, T. Li, Z. Cheng, H. Liu, Y. Liu, H. Zhang, B. Yang, Chem. Commun. 2017, 53, 416. [35] A. P. Balan, S. Radhakrishnan, C. F. Woellner, S. K. Sinha, L. Deng, C.
- De Los Reves, B. M. Rao, M. Paulose, R. Neupane, A. Apte, et al., Nat. Nanotechnol. 2018, 13, 602.
- [36] A. Puthirath Balan, S. Radhakrishnan, R. Kumar, R. Neupane, S. K. Sinha, L. Deng, C. A. de los Reyes, A. Apte, B. M. Rao, M. Paulose, et al., Chem. Mater. 2018, 30, 5923.
- [37] B. Mohanty, Y. Wei, M. Ghorbani-Asl, A. V. Krasheninnikov, P. Rajput, B. K. Jena, J. Mater. Chem. A 2020, 8, 6709.

- [38] C. C. Gowda, A. Mathur, A. Parui, P. Kumbhakar, P. Pandey, S. Sharma, A. Chandra, A. K. Singh, A. Halder, C. S. Tiwary, *J. Ind. Eng. Chem.* **2022**, *113*, 153.
- [39] A. B. Puthirath, S. N. Shirodkar, G. Gao, F. C. R. Hernandez, L. Deng, R. Dahal, A. Apte, G. Costin, N. Chakingal, A. P. Balan, et al., *Small* **2020**, *16*, 2004208.
- [40] M. Mullner, M. Riva, F. Kraushofer, M. Schmid, G. S. Parkinson, S. F. Mertens, U. Diebold, *J. Phys. Chem. C* **2018**, *123*, 8304.
- [41] G. Righi, S. Fabris, S. Piccinin, *J. Phys. Chem. C* **2021**, *125*, [18752.](https://doi.org/10.1021/acs.jpcc.1c05804)
- [42] X. Yu, C.-F. Huo, Y.-W. Li, J. Wang, H. Jiao, *Surf. Sci.* **[2012](https://doi.org/10.1016/j.susc.2012.02.003)**, *606*, 872.
- [43] P. Serles, T. Arif, A. B. Puthirath, S. Yadav, G. Wang, T. Cui, A. P. Balan, T. P. Yadav, P. Thibeorchews, N. Chakingal, et al., *Sci. Adv.* **2021**, *7*, eabk2041.
- [44] A. Thesing, E. J. Damiani, L. F. Loguercio, P. G. Demingos, A. R. Muniz, N. L. Carreno, S. Khan, M. J. Santos, A. G. Brolo, J. F. Santos, *ACS [Omega](https://doi.org/10.1021/acsomega.0c04343)* **2020**, *5*, [33007.](https://doi.org/10.1021/acsomega.0c04343)
- [45] J. H. Kim, J. H. Jeong, N. Kim, R. Joshi, G.-H. Lee, *J. Phys. D* **2018**, *52*, 083001.
- [46] F. Mouhat, F.-X. Coudert, *Phys. Rev. B* **2014**, *90*, 224104.
- [47] I. C. Man, H.-Y. Su, F. Calle-Vallejo, H. A. Hansen, J. I. Martínez, N. G. Inoglu, J. Kitchin, T. F. Jaramillo, J. K. Nørskov, J. Rossmeisl, *[ChemCatCh](https://doi.org/10.1002/cctc.201000397)em* **[2011](https://doi.org/10.1002/cctc.201000397)**, *3*, 1159.
- [48] X. Kong, Z. Peng, *Materials Today [Chemistry](https://doi.org/10.1016/j.mtchem.2018.10.011)* **2019**, *11*, 119.
- [49] J. T. Mefford, X. Rong, A. M. Abakumov, W. G. Hardin, S. Dai, A. M. Kolpak, K. P. Johnston, K. J. Stevenson, *Nat. Commun.* **2016**, *7*, 11053.
- [50] A. M. Harzandi, S. Shadman, A. S. Nissimagoudar, D. Y. Kim, H.-D. Lim, J. H. Lee, M. G. Kim, H. Y. Jeong, Y. Kim, K. S. Kim, *Adv. Energy Mater.* **2021**, *11*, 2003448.
- [51] R. Anand, A. S. Nissimagoudar, M. Umer, M. Ha, M. Zafari, S. Umer, G. Lee, K. S. Kim, *Adv. Energy Mater.* **2021**, *11*, 2102388.
- [52] A. Meena, P. Thangavel, A. S. Nissimagoudar, A. N. Singh, A. Jana, D. S. Jeong, H. Im, K. S. Kim, *Chem. Eng. J.* **2022**, *430*, [132623.](https://doi.org/10.1016/j.cej.2021.132623)
- [53] Q. Liang, G. Brocks, A. Bieberle-Hütter, *Journal of Physics: Energy* **2021**, *3*, 026001.
- [54] F. Lei, Y. Sun, K. Liu, S. Gao, L. Liang, B. Pan, Y. Xie, *J. Am. [Chem.](https://doi.org/10.1021/ja501866r) Soc.* **[2014](https://doi.org/10.1021/ja501866r)**, *136*, 6826.
- [55] D. Santos-Carballal, A. Roldan, R. Grau-Crespo, N. H. de Leeuw, *[Phys.](https://doi.org/10.1039/C4CP00529E) [Chem.](https://doi.org/10.1039/C4CP00529E) Chem. Phys.* **2014**, *16*, 21082.
- [56] J. D. Gouveia, J. R. Gomes, *Physical Review Materials* **2022**, *6*, 024004.
- [57] J. Zaffran, M. C. Toroker, *[ChemElectroChem](https://doi.org/10.1002/celc.201700445)* **2017**, *4*, 2764.
- [58] A. Doriguetto, N. Fernandes, A. Persiano, E. N. Filho, J. Greneche, J. Fabris, *Phys. [Chem.](https://doi.org/10.1007/s00269-003-0310-x) Miner.* **2003**, *30*, 249.
- [59] T. Ishikawa, H. Nakazaki, A. Yasukawa, K. Kandori, M. Seto, *[Mater.](https://doi.org/10.1016/S0025-5408(98)00162-7) Res. Bull.* **[1998](https://doi.org/10.1016/S0025-5408(98)00162-7)**, *33*, 1609.
- [60] O. Farr, E. J. Elzinga, N. Yee, *Geochemical Transactions* **2022**, *23*, 3.

- [61] V. Brabers, F. Walz, H. Kronmüller, *Phys. Rev. B* **1998**, *58*, [14163.](https://doi.org/10.1103/PhysRevB.58.14163)
- [62] U. Wooyong, K. Dong-Sang, et al., *Environ. Sci. Technol.* **2016**, *50*, 5216– 5224.
- [63] Y. Xu, W. Bian, J. Wu, J.-H. Tian, R. Yang, *[Electrochim.](https://doi.org/10.1016/j.electacta.2014.11.042) Acta* **2015**, *151*, [276.](https://doi.org/10.1016/j.electacta.2014.11.042)
- [64] M. Al-Hoshan, J. Singh, A. Al-Mayouf, A. AlSuhybani, M. Shaddad, *[Int.](https://doi.org/10.1016/S1452-3981(23)19595-2) J. [Electrochem.](https://doi.org/10.1016/S1452-3981(23)19595-2) Sci.* **2012**, *7*, 4959.
- [65] S. Han, S. Liu, S. Yin, L. Chen, Z. He, *[Electrochim.](https://doi.org/10.1016/j.electacta.2016.05.194) Acta* **2016**, *210*, 942.
- [66] F. Mirabella, M. Müllner, T. Touzalin, M. Riva, Z. Jakub, F. Kraushofer, M. Schmid, M. T. Koper, G. S. Parkinson, U. Diebold, *[Electrochim.](https://doi.org/10.1016/j.electacta.2021.138638) Acta* **2021**, *389*, [138638](https://doi.org/10.1016/j.electacta.2021.138638).
- [67] S. T. Skowron, I. V. Lebedeva, A. M. Popov, E. Bichoutskaia, *[Chem.](https://doi.org/10.1039/C4CS00499J) Soc. Rev.* **[2015](https://doi.org/10.1039/C4CS00499J)**, *44*, 3143.
- [68] H. Zheng, Y. Choi, F. Baniasadi, D. Hu, L. Jiao, K. Park, C. Tao, *2D [Mater.](https://doi.org/10.1088/2053-1583/ab3beb)* **2019**, *6*, [041005](https://doi.org/10.1088/2053-1583/ab3beb).
- [69] F.-Q. Li, Y. Zhang, S.-L. Zhang, *[Nanomaterials](https://doi.org/10.3390/nano11061395)* **2021**, *11*, 1395.
- [70] B. Xiao, L. Yang, H. Liu, X. Jiang, B. Aleksandr, E. Song, Q. Jiang, *[Appl.](https://doi.org/10.1016/j.apsusc.2020.147846) Surf. Sci.* **2021**, *537*, [147846](https://doi.org/10.1016/j.apsusc.2020.147846).
- [71] X. Liu, Y. Zhang, W. Wang, Y. Chen, W. Xiao, T. Liu, Z. Zhong, Z. Luo, Z. Ding, Z. Zhang, *ACS Appl. Mater. Interfaces* **2021**, *14*, 1249.
- [72] Z. Qin, J. Zhao, *J. Colloid [Interface](https://doi.org/10.1016/j.jcis.2021.07.087) Sci.* **2022**, *605*, 155.
- [73] H. Niu, X. Wan, X. Wang, C. Shao, J. Robertson, Z. Zhang, Y. Guo, *[ACS](https://doi.org/10.1021/acssuschemeng.0c09192) [Sustainable](https://doi.org/10.1021/acssuschemeng.0c09192) Chem. Eng.* **2021**, *9*, 3590.
- [74] M. Ha, D. Y. Kim, M. Umer, V. Gladkikh, C. W. Myung, K. S. Kim, *[Energy](https://doi.org/10.1039/D1EE00154J) [Environ.](https://doi.org/10.1039/D1EE00154J) Sci.* **2021**, *14*, 3455.
- [75] A. Khorshidi, J. Violet, J. Hashemi, A. A. Peterson, *Nature [Catalysis](https://doi.org/10.1038/s41929-018-0054-0)* **2018**, *1*, [263](https://doi.org/10.1038/s41929-018-0054-0).
- [76] L. Zhang, Y. Yuan, J. Lapano, M. Brahlek, S. Lei, B. Kabius, V. Gopalan, R. Engel-Herbert, *ACS [Nano](https://doi.org/10.1021/acsnano.7b07539)* **2018**, *12*, 1306.
- [77] S. Deng, A. V. Sumant, V. Berry, *Nano [Today](https://doi.org/10.1016/j.nantod.2018.07.001)* **2018**, *22*, 14.
- [78] J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard, H. Jonsson, *J. Phys. Chem. B* **2004**, *108*, [17886.](https://doi.org/10.1021/jp047349j)
- [79] A. Kulkarni, S. Siahrostami, A. Patel, J. K. Nørskov, *[Chem.](https://doi.org/10.1021/acs.chemrev.7b00488) Rev.* **2018**, *118*, [2302.](https://doi.org/10.1021/acs.chemrev.7b00488)
- [80] G. Kresse, J. Hafner, *Phys. Rev. B* **[1993](https://doi.org/10.1103/PhysRevB.47.558)**, *47*, 558.
- [81] V. Wang, N. Xu, J.-C. Liu, G. Tang, W.-T. Geng, *Comput. Phys. [Commun.](https://doi.org/10.1016/j.cpc.2021.108033)* **2021**, *267*, [108033.](https://doi.org/10.1016/j.cpc.2021.108033)

Manuscript received: May 30, 2024 Revised manuscript received: August 21, 2024 Accepted manuscript online: August 30, 2024 Version of record online: October 30, 2024