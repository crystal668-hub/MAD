---
source: Karmodak和Nørskov - 2023 - Activity And Stability of Single‐ And Di‐Atom Catalysts for the O2 Reduction Reaction.pdf
tool: marker
duration: 83.305s
generated: 2026-01-09T12:07:25.301929Z
---

## *Forschungsartikel*

*Electrocatalysis*

Zitierweise: *Angew. Chem. Int. Ed.* **2023**, *62*, e202311113 [doi.org/10.1002/anie.202311113](https://doi.org/10.1002/anie.202311113)

# **Activity And Stability of Single- And Di-Atom Catalysts for the O2 Reduction Reaction**

*Naiwrit [Karmodak](http://orcid.org/0000-0002-6236-9634)\* and Jens K. Nørskov*

**Abstract:** Efficient and inexpensive catalysts for the O2 reduction reaction (ORR) are needed for the advancement of renewable energy technologies. In this study, we designed a computational catalyst-screening method to identify single and di-atom metal dopants from first-row transition elements supported on defect-containing nitrogenated graphene surfaces for the ORR. Based on formation-energy calculations and micro-kinetic modelling of reaction pathways using intermediate binding free energies, we have identified four potentially interesting single-atom catalysts (SACs) and fifteen di-atom catalysts (DACs) with relatively high estimated catalytic activity at 0.8 V vs RHE. Among the best SACs, MnNC shows high stability in both acidic and alkaline media according to our model. For the DACs, we found four possible candidates, MnMn, FeFe, CoCo, and MnNi doped on quad-atom vacancy sites having considerable stability over a wide pH range. The remaining SACs and DACs with high activity are either less stable or show a stability region at an alkaline pH.

## *Introduction*

H2 fuel cells are identified as promising devices for the conversion of chemical energies into electrical power via electrochemical oxidation of molecular H2. [1–3] The reaction efficiency of the O2 reduction reaction (ORR) plays a critical role in tuning the activity of H2 fuel cells.[4–7] This is due to the slow kinetics and high reaction overpotential for ORR. Efficient electrocatalysts are therefore needed for achieving higher reaction efficiency. So far, Pt-group metal surfaces serve as the best electrode materials.[8,9] Nevertheless, these electrode materials are very expensive and

[\*] Dr. N. Karmodak, Prof. J. K. Nørskov CatTheory Center, Dept. of Physics, Technical University of Denmark, 2800 Kongens Lyngby (Denmark)

Dr. N. Karmodak

Current affiliation: Department of Chemistry, Shiv Nadar Institute of Eminence, Greater Noida 201314 (India) E-mail: Naiwrit.karmodak@snu.edu.in

© 2023 The Authors. Angewandte Chemie published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution Non-Commercial NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

hence alternative ORR electro-catalysts composed of earthabundant elements are much sought after for industrial-scale applications.[10,11]

The recent development of large databases of twodimensional (2D) materials with extraordinary physical and chemical properties attracted research interest to understand their electrocatalytic activities for ORR.[12,13] However, due to the inert nature of their pristine surfaces, most often, the surfaces of 2D materials need to be activated by the introduction of dopants, defects or edge states.[14–16] A few studies show that embedding single transition metal atoms onto defected nitrogenated 2D graphene surfaces (MNCs) could have good ORR catalytic activity.[14,15,17–20] Reducing the number of metal atoms at the active center enhances the atom efficiency of the active site and provides a tunable catalytic activity by varying the nature of metal dopants.[21,22]

One major issue with these MNCs is the insufficient stability at the relevant ORR conditions.[23–26] The theoretical and experimental studies show that MNCs undergo rapid degradation under acidic conditions.[25–28] Among the various degradation mechanisms, the dissolution of the metal dopants due to the protonation of the surrounding coordinated N atoms has been proposed to be the most plausible pathway in acidic media.[26,29,30]

Recent experiments on metal-doped 2D materials indicate that increasing the number of metal dopants might allow effective tuning of both the catalytic activity and stability of SACs.[14,31] Several studies have reported the synthesis of diatom-doped graphene catalysts, with higher ORR activity compared to single atom-doped graphene catalysts.[31–35] Particularly, the diatom catalysts (DACs) FeCo and FeMn show higher half-wave potentials (0.86 V and 0.92 V respectively) than the Fe, Co, and Mn SACs.[32,34] We investigate whether screening different transition metal dimers and evaluating their ORR activity might lead to the discovery of several other promising catalysts. The diatom metal dopants could show differential binding motifs of the reaction intermediates, which could influence the reaction energetics and open new opportunities to tune the catalytic activity. Furthermore, due to the metal-metal interactions in DACs, the dissolution of the metal dopants under varied electrochemical conditions could be reduced. Therefore, the electrochemical stability of the catalysts will preferably enhance in comparison to SACs.

In this paper, we report a screening study of single and di-atom metal dopants on defected nitrogenated graphene surface based on the stability and activity of ORR. The firstrow transition metals from Sc and Zn have been chosen as metal dopants. The computational workflow involves three

15213757, 2023. 47, Downloaded from https://onlinelbitary.wiley.com/doi/10.1002/ange.202311113 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelbitary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons. Licensea

Angewandte

screening steps. The first step corresponds to the calculation of the binding energies of the metal dopants onto different C-atom vacancy sites of single-layer graphene to determine most favorable binding site motifs of di-atom dopants. The next two steps involve the activity and stability study respectively. Activity volcano plots are calculated using the binding energies of the intermediates as the activity descriptors calculated using the hybrid-DFT HSE06 functional and a continuum embedded solvent medium.[36-39] Based upon the catalytic activity, we have screened several single and diatom candidates with comparable activity to the Pt (111) surface. Assessing the electrochemical stability at both acidic and alkaline mediums using surface Pourbaix diagrams, we have found that N-atom coordination surrounding metal dopants considerably influences the stability of both the SACs and DACs.

#### Results and Discussion

We begin our screening study by determining the stable binding site motifs of metal dopants for SACs and DACs. The preferable doping sites of the single and di-atom dopants are determined by calculation of the formation energies using the eq. 1.

$$\Delta E_{form} = (E_{M1/M2-NC}^{DFT} - E_{M1/M2(bulk)}^{DFT} - E_{NC(Graphene)}^{DFT})/n \tag{1}$$

In this equation, the DFT calculated energy of DACs and SACs are denoted by  $E_{M1/M2-NC}$ . The bulk metal (E<sub>M1/M2(bulk</sub>) is used as the reference for the metal dopants and E<sub>NC</sub> is the energy of the defected nitrogenated graphene surface. These surfaces are generated by creating different carbon atom vacancies on nitrogenated graphene sheet. n is the number of metal dopants.

The di-atom carbon vacancy site is considered the possible doping site for SACs based on our earlier study. [40] By comparing the formation energies of single metal dopants on single and di-carbon-atom vacancy sites, we have observed that the di-carbon atom vacancy is the most preferred doping site for SACs. On the other hand, to determine the stable binding sites for di-atom metal dopants, the formation energies ( $\Delta E_{form}$ ) are calculated by varying the carbon-atom vacancy sites from two to six.

Figure 1a shows the formation energies of the di-atom catalysts per dopant on different carbon atom vacancy sites. The different vacancy sites are denoted by a two-letter symbol. For example, DV corresponds to di-atom, TV to triatom, QV to quad-atom, PV to penta-atom, and HV to hexa-atom carbon vacancy sites. The formation energies of the corresponding SACs (Figure 1b) are also given in this

The formation energy ( $\Delta E_{form}$ ) of di-atom metal dopants shows that the two quad-atom carbon vacancy sites QV2 and QV3 have the highest stability. Figure 1(c) shows the structural arrangement of these two quad-atom carbon

Figure 1. (a) The formation energy ( $\Delta E_{form}$ ) heatmap for the SACs and DACs. The first-row transition metals from Sc to Zn are used as the possible di-atom dopants embedded on different vacancy sites (shown in Figure S2, Supporting Information) of the defected nitrogenated graphene surface. The formation energy values for the corresponding single dopant sites are also shown here. The color map shows the energy values in eV/dopant site. We have used a two-letter symbol to denote the different vacancy sites. Such as DV denotes di-vacancy, TV for tri-vacancy, QV for quadvacancy, PV for pent-vacancy, and HV for hex-vacncy sites. (b) The di-carbon atom vacancy site is considered the most favorable doping site for the SACs. (c) The quad-atom vacancy sites QV2 and QV3 on which the di-atom dopants show the highest stability. The calculation details for the  $\Delta E_{\rm form}$  values are given in section S-II in the Supporting Information.

15213757, 2023. 47, Downloaded from https://onlinelbitary.wiley.com/doi/10.1002/ange.202311113 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelbitary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons. Licensea

Angewandte

vacancies. The atomic arrangements for the other vacancy sites are shown in the Supporting Information, Figure S2.

It is to be noted that for most of the diatom catalysts, the formation energies are comparable to or slightly greater than the corresponding SACs. Therefore, during the synthesis of these diatom catalysts, single atom doping configurations might be obtained simultaneously for these metal dopants. Therefore, to enhance the di-atom doping concentrations, the controlled synthetic pathways reported in the recent literature based upon the metal-organic templates would be more suitable.[31-35,41-43]

In addition to the doping site configurations based on the carbon-atom vacancies, the stability of the DACs is found to largely vary depending upon the surrounding N-atom coordination. For the diatom catalysts, three Natom coordination such as 2 N, 4 N, and 6/7 N for QV2/QV3 DACs are considered. Figure S4 and S5 in the Supporting Information show the comparison of the formation energies for the OV2 and OV3 DACs with varied N-atom coordination respectively. The formation energies show differing stability trends depending upon the metal dopants and quad-atom vacancy sites. On the QV2 sites, decreasing the number of N-atoms reduces the stability of the catalysts. However, for the QV3 site, a few of the diatom dopants show comparable stability for 7 N and 4 N surrounding coordination. The dimers with 2 N coordination have the lowest stability on both QV2 and QV3 sites.

In the next step of catalyst screening, the activity of the SACs and DACs with QV2 and QV3 geometry is analysed. The dissociative O<sub>2</sub> reduction pathway has been found to be unlikely on several catalysts surfaces due to the involved high dissociative barrier of the O-O bond. [1,48] Therefore, we have considered the following associative pathway as the possible mechanism for O2 reduction on the catalyst surfaces.

$$\begin{split} O_2(g) + ^* &\rightleftharpoons O_2^* \\ O_2^* + H^+ + e^- &\rightleftharpoons OOH^* \\ OOH^* + H^+ + e^- &\rightleftharpoons O^* + H_2O(g) \\ O^* + H^+ + e^- &\rightleftharpoons OH^* \\ OH^* + H^+ + e^- &\rightleftharpoons ^* + H_2O(g) \end{split}$$

In Figures 2a and 2b, the scaling relations for the adsorbate binding energies on the SACs and DACs are compared with the metal (111) scaling lines. The black solid lines correspond to SACs, whereas for the QV2 and QV3 catalysts, the scaling data has been shown in blue and red solid lines respectively. The green dotted line denotes the scaling relation for the metal (111) surfaces, plotted using the data obtained from the reference.<sup>[44]</sup>

The binding energies of OH\* vs OOH\* on both the SACs and DACs in Figure 2a follow the universal linear scaling relationship with similar intercept values as the metal (111) surfaces. [45] While OH\* vs O\* binding energies on the SACs and DACs also follow linear scaling relationships, the

scaling lines in Figure 2b considerably deviate with respect to the metal (111) surfaces. [44,46]

The scaling relations of OH\* vs O\* binding energies on the SACs and DACs show great similarity to the high indexed transition metal oxide surfaces.[44] Unlike the bridged configuration mostly preferred on the metal (111) surfaces, the O<sup>\*</sup> intermediate prefers an on-top binding motif on SACs and DACs. This results in a similar scaling relation as the transition metal oxide surfaces. [44] The type of binding site determines the intercept values. The preference for on-top binding motifs of OOH\*, OH\* and O\* adsorbates on the SACs and DACs result in similar intercept values for both the adsorption energy of OOH\* versus OH\* and O\* versus OH\*.

The variation in N-atom coordination surrounding the metal dopants for most of the SACs and DACs are found to have less effect on the scaling relations for the intermediate binding energies. However, by reducing the surrounding Natom coordination on some of the di-atom metal dopants, we have found that O\* intermediate prefers a bridged motif to a slightly greater extent than the on-top binding motif. In this bridged motif, the O intermediate is attached to the metal atom and one of the surrounding C-atoms.

We have found that the bridged motifs for O intermediate on these catalysts follow a different scaling relationship with the OH intermediate, shown in Figure S6 of the Supporting Information. However, OH and OOH show an ontop binding motif for these diatom catalysts and follows the universal scaling relationships as in

Having determined the scaling relationships, next we study the ORR activity on the SACs and DACs. A meanfield microkinetic modeling is performed based upon the scaling relations of the intermediate binding energies. We have used a similar micro-kinetic model for ORR developed by Hansen et al. and Kelly et al. in the recent studies using the CatMaP package (complete details in section II(b) in Supporting Information). [44,46–47] The activation barrier for the proton transfers steps is taken to be 0.26 eV and we have assumed an electron transfer of 0.5 at the transition state, following the similar approximations used in the earlier studies.[44,47]

Figure 2c to 2e show the activity volcano plot for the SACs and DACs with varying surrounding N-atom coordination at an applied potential of 0.8 V vs RHE. We have not included the diatom catalysts with 2 N surrounding coordination, due to lower thermodynamic stability (Figure S4 and S5 in Supporting Information) compared with higher Ncoordination. The activity of the catalysts denoted by log[TOF<sub>rel</sub>] corresponds to the relative TOF with respect to the Pt (111) surface. The binding energies of OH\* are used as the activity descriptor in these plots and are reported relative to Pt (111) surface  $(\Delta G_{OH} - \Delta G_{OH}^{Pt})$  along the x-axis. We have shown only the most active candidates in Figure 2-

While using the binding energies of OH\* as the descriptor, the candidates on the left leg of the activity volcano plot will have a stronger binding affinity of OH\* compared to the Pt (111) surface. On these catalysts surfaces, removal of

15213737, 2023, 47, Downloaded from https://onlinelbiary.wiley.com/doi/10.1002/ange.202311113 by University Of Science, Wiley Online Library on [06/0/12026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque Commons Licenseque

Figure 2. (a) and (b) show the scaling relations between the binding energies of OH\* (E<sub>OH</sub>) vs OOH\* (E<sub>OOH</sub>) and O\* (E<sub>O</sub>) intermediates respectively. The black, red, and blue solid lines correspond to the linear scaling lines for the SACs and DACs with QV2 and QV3 geometries with different metal dopants and varying surrounding N-atom coordination. The green dotted line shows the scaling relation for the metal (111) surface. (c)—(e) show the ORR activity volcano plots for the SACs and DACs on QV2 and QV3 doping sites plotted using the binding energies of OH\* as the activity descriptor at a potential of 0.8 V vs RHE. To compare the activity of SACs and DACs we have shown the relative TOF (log [TOF<sub>rel</sub>] in s<sup>-1</sup>) with respect to the Pt (111) surfaces on the y-axis. The x-axis shows the binding energies of OH\* intermediate with respect to Pt (111) surface. For both the SACs and DACs, the candidates with the activity comparable to or greater than Pt (111) surface are only shown. Different markers are used to denote the catalysts with varying surrounding N-atom coordination as shown in the Figures.

 ${\rm OH}^*$  will be the rate-determining step. [48] Furthermore, due to the stronger binding of  ${\rm OH}^*$ , the active sites will have higher coverages and will be poisoned during the reaction. The catalysts on the right leg of the volcano will have a lower binding affinity of  ${\rm OH}^*$  compared to the Pt (111) surface. Due to the weak binding of  ${\rm OH}^*$  on these catalyst surfaces, the rate-limiting step corresponds to the adsorption of  ${\rm O}_2$ . It is to be noted that, due to the higher lying scaling relations of both SACs and DACs with respect to metal (111) surfaces, the ORR activity is lower than Pt (111) surface.

The activity of SACs in Figure 2c show that most of the early transition elements from Sc to Cr have lower ORR TOF. Among the late transition metals, we identify four active candidates with the metal dopants Mn, Fe, Co, and Zn, lying on the top of volcano plot (Figure 2c).

The varying N-atom coordination has different trends depending upon the metal dopants. Reducing the N-atom coordination enhances the activity of FeNC catalysts. On the other hand, for CoNC and MnNC, the ORR activity is found to reduce slightly with the decrease in the surrounding N-atom coordination (Figure 2c). For ZnNC, we have not

found considerable changes in the activity with the variation in surrounding N-atom coordination. The surrounding N-atom coordination is also found to influence the rate determining step. In the earlier experimental studies, some of these SACs have been identified as good catalysts for ORR. [14,19]

Focusing on the diatom metal dopants, we have found more candidates than for SACs towards the top of activity volcano (Figure 2d and 2e). Different markers are used to denote the surrounding N-atom variation in these plots. The di-atom dopants which are active on both QV2 and QV3 sites are denoted in red, whereas the dopants in black are unique candidates. The ones represented with the \* have been obtained as good candidates for ORR in recent experiments. [32-34] However, unlike the SACs, we have not seen a promising activity trend depending upon the surrounding N-atom coordination for DACs.

With the QV2 geometry, we find 9 metal dimers lying on the top of the volcano plot. Among these candidates, the metal dimers FeNi, MnFe, MnZn, MnCu, and MnNi, are most active with 6 surrounding N atom coordination, whereas CoCo, FeFe and MnMn dimers show the highest activity

with 4 N surrounding coordination. FeCu is found to be active with both 6 N and 4 N surrounding coordination.

On the other hand, with QV3 geometry, eight candidates show good activity for ORR. With this doping geometry, we have found that the maximum number of the active metal dopants prefer 4 N surrounding coordination. These candidates are FeCo, MnNi, MnZn, and FeZn. With the 7 N surrounding coordination, only one candidate NiZn is obtained with high TOF.

On both QV2 and QV3 sites, we have not identified active dimer candidates with Sc, Ti, and V as the possible dopants. The higher binding affinity of  $O^*$  intermediates on these metal dimers is seen to reduce the ORR activity.

Among the diatom candidates found with the high catalytic activity, we find the three metal dimers FeCo, MnFe, and FeZn have been identified in the recent experiments as catalysts for ORR. [32-34] In our study, both MnFe and FeZn dimers are on the top of the activity volcano plot. MnFe shows good activity on the QV2 doping site, whereas FeZn dimer is found to have high activity on QV3 site. FeCo dimer on both QV2 and QV3 sites shows slightly lower activity in comparison to MnFe and FeZn. The greater binding strength of OH\* on this dimer reduces the catalytic activity compared to MnFe and FeZn dimers.

To explore the possibilities of  $H_2O_2$  production for the most active candidates screened for SACs and DACs, we have calculated the rate of the two-electron pathway leading to the formation of  $H_2O_2$ .<sup>[46]</sup> Section S-III in Supporting Information shows the reaction mechanism and corresponding activity volcano plots using the binding energies of  $OH^*$  intermediate. The metal dopants obtained with higher activity for ORR show lower efficiency for  $H_2O_2$  production.

While the high activity of the catalysts is a necessary condition, electrochemical stability plays an important role in determining the overall catalytic efficiency. Particularly, the catalysts should be stable towards electrochemical decomposition to aqueous species under the relevant electrochemical conditions for ORR. Therefore, in this screening step, we have studied the stability dependence of the SACs and DACs on the pH of the medium, under an electrochemical potential.

To understand the electrochemical stability of the catalysts, we have calculated the free energies for demetallation reactions as shown in eq. 2 to 4.

**SACs**: 
$$C_x N_y M O_a H_b + (2a - b + m) H^+$$
  
 $\rightleftharpoons C_x N_v H_m + M^q + a H_2 O + (q + 2a + b - m) e^-$ 
(2)

**DACs**: 
$$C_x N_y M_1 M_2 O_a H_b + (2a - b + m) H^+$$
  
 $\Leftrightarrow C_x N_4 M_{1/2} H_m + M_{2/1}^q + a H_2 O + (q + 2a + b - m) e^-$ 
(3)

$$\begin{split} \textbf{DACs}: & C_x N_y M_1 M_2 O_a H_b + (2a-b+m) H^+ \\ & \rightleftharpoons C_x N_y H_m + M_1^p + M_2^q + a H_2 O + (p+q+2a+b-m) e^- \end{split} \tag{4}$$

The eq. 2 represents the demetallation mechanism for the SACs upon hydrogenation of the surrounding N atoms, whereas eq. 3 and 4 correspond to the dissolution mechanisms of one or both the metal dopants respectively for the DACs. p and q denote the charges of the solvated metal ions and m represents the number of adsorbed H atoms. We have varied the values for a and b such as to represent the demetallation mechanism for catalysts without and with the possible ORR intermediates (OH\*, O\* and OOH\*). The demetallation free energy values are calculated following the similar method as used in references<sup>[12,49–51]</sup> to calculate the Pourbaix stability of the materials.

Using these demetallation free energies, Pourbaix diagrams are plotted in Figure 3 at different oxidative potentials vs SHE and varying pH for the most active SACs and DACs obtained from the activity volcano plot in Figure 2c to 2e.

Among the SACs identified with high ORR activity, we have found that only MnNC with the different surrounding N coordination shows both the acid and alkaline stability. Fe and Co SACs with 4 N and 3 N surrounding coordination are found to be unstable under acidic pH. The dissolution of the metal dopants is less feasible only under the basic medium. The electrochemical stability enhances by reducing the number of surrounding N coordination to 2 under acidic medium for both these metal dopants. Zn SAC with 4 N and 3 N coordination are found to be unstable under both acidic and basic mediums. The 2 N doped ZnNC shows a stability region beyond pH 10.

The demetallation free energies of the active di-atom catalysts on the QV2 site show that the three metal dimers MnMn, CoCo, and FeFe with 4 N surrounding coordination are stable for a wide range of pH. The active di-atom dopants with 6 N coordination except for MnZn and FeCu with surrounding 4 N coordination show a stability region in the alkaline medium.

On the other hand, for the QV3 site, the metal dimer MnNi with 4 N surrounding coordination is only found to be stable at all the pH ranges. The other two metal dimers, NiZn with 7 N coordination and FeZn with 4 N coordination show a stability region in the alkaline pH. MnZn on both the QV2 and QV3 sites is found to be less stable for all pH values

#### Conclusion

We study the stability and activity of single and di-atom doped catalysts on defected nitrogenated graphene surface for the  $O_2$  reduction reaction. The first-row transition metals are used as the possible dopants. We use a three-step screening workflow to screen the possible candidates with high activity for ORR. In the initial step, the formation energy calculations on the different C-atom vacancy sites of graphene are performed to determine the possible doping sites for single and di-atom metal dopants. The di-carbon atom vacancy is most preferable for single metal dopants, whereas the dimers prefer quad-atom carbon vacancy sites. Among the different quad-atom carbon vacancies, we have found that the two sites denoted as QV2 and QV3 have the highest stability. Comparing the relative stability of the

15213757, 2023, 47, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ange.202311113 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

*Figure 3.* The plots of electrochemical stability for the most active single and di-atom metal dopants obtained from the activity volcano plots for SACs and DACs in Figures 2(c) to 2(e). (a) The stability plot for FeNC, CoNC, MnNC, and ZnNC catalysts with surrounding N coordination varying from 4 to 2 atoms. (b) and (c) The stability plot for the QV2 and QV3 DACs respectively identified with good activity for ORR. The corresponding surrounding N-atom coordinations are given within the parenthesis. The colormap of the stability plot denotes the dematallation free energies calculated using the equation 2 to 4. The blue region denotes the stable electrochemical conditions (potential and solvent pH) at which the aqueous dissolution of the metal atoms from the catalyst surface as solvated metal ions would be less feasible. In the red region, the catalysts are expected to undergo aqueous decompositions and therefore would be unfavorable for catalytic activity.

DACs with the corresponding single doping sites, we find smaller differences in formation energies of single and diatom doping. Therefore, following the thermodynamic synthesis methods, both the doping sites could form simultaneously. For allowing the formation of specific doping sites, the controlled template-assisted synthetic methods should be preferable.

Following the four-electron pathway for ORR, in the second screening step, we perform an activity analysis of the catalysts. We observe linear scaling relations between the binding energies of the intermediates for both the SACs and DACs. The OH\* vs OOH\* follows the universal scaling relationship with the intercept values almost comparable to the metal (111) surfaces. However, the OH\* vs O\* scaling lines show considerable deviation with respect to the metal (111) surfaces. We have found that due to the preferential on-top binding affinity of O\* intermediate on the active center of SACs and DACs, the OH\* vs O\* scaling lines show similarity to the high indexed transition metal oxide surfaces.

Based on the scaling relations and binding energies of the intermediates, a micro-kinetic model is developed to plot activity volcanoes for screening the candidates. Due to the similarity in the scaling relationships with high indexed TMO surfaces, the activity of both SACs and DACs are lower than the Pt (111) surface. For SACs, we have found the four most interesting candidates to be FeNC, MnNC, CoNC, and ZnNC with relatively high TOF for ORR. For the DACs, on the QV2 and QV3 site we have identified ten and four possible candidates respectively with high activity. The varying surrounding N-atom coordination shows differing activity trends for SACs and DACs.

The third screening step involves the stability calculation under varied electrochemical environments. The demetallation free energy calculations of the catalysts are performed to reveal the electrochemical stability at varying pH. The calculation shows that most of the active SACs with 4 and 3 surrounding N-atom coordination have low stability in acidic pH. The stability increases by decreasing the surrounding Natom coordination to 2. We found that MnNC is the only SACs that is stable in both the acidic and alkaline pH for all values of surrounding N-atom coordination.

For the DACs, the Pourbaix plots at different pH and oxidative potential show that on the QV2 site the three metal dimers FeFe, MnMn and CoCo with 4 N coordination have high stability in both acidic and alkaline mediums. The QV3 site shows one di-atom dopant as MnNi with 4 N coordination having good stability at all considered pH

15213757, 2023, 47, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ange.202311113 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

ranges. The remaining metal dimers identified with high ORR activity on both QV2 and QV3 are either less stable or show a stability region in the alkaline pH.

In this study, we report four other possible candidates such as MnMn, FeFe, CoCo, and MnNi with relatively high activity for ORR and stability at both acidic and alkaline pH. These candidates are found to have similar activity as the three experimentally observed di-atom catalysts (FeCo, FeMn, and FeZn). The Pourbaix diagrams reported in this study will help in tuning the electrochemical stability of the SACs and DACs and allow specific selection of the metal dopants to be operative under acidic or alkaline pH.

### *Acknowledgements*

The research leading to these results has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement no. 899987. We also acknowledge the VILLUM Centre for the Science of Sustainable Fuels and Chemicals (#9455) from VILLUM FONDEN.

#### *Conflict of Interest*

The authors declare no conflict of interest.

#### *Data Availability Statement*

The data that support the findings of this study are available on request from the corresponding author. The data are not publicly available due to privacy or ethical restrictions.

**Keywords:** Catalysts **·** Density Functional Theory **·** Dopants **·** Oxygen Reduction Reaction **·** Pourbaix Diagram

- [1] A. Kulkarni, S. Siahrostami, A. Patel, J. K. Nørskov, *[Chem.](https://doi.org/10.1021/acs.chemrev.7b00488) Rev.* **2018**, *118*, [2302–2312.](https://doi.org/10.1021/acs.chemrev.7b00488)
- [2] H. A. Gasteiger, N. M. Marković, *[Science](https://doi.org/10.1126/science.1172083)* **2009**, *324*, 48–49.
- [3] M. K. Debe, *[Nature](https://doi.org/10.1038/nature11115)* **2012**, *486*, 43–51.
- [4] V. Viswanathan, H. A. Hansen, J. Rossmeisl, J. K. Nørskov, *ACS Catal.* **2012**, *2*, [1654–1660](https://doi.org/10.1021/cs300227s).
- [5] I. Katsounaros, S. Cherevko, A. R. Zeradjanin, K. J. J. Mayrhofer, *Angew. Chem. Int. Ed.* **2014**, *53*, [102–121.](https://doi.org/10.1002/anie.201306588)
- [6] N. Markovic, H. Gasteiger, P. N. Ross, *J. [Electrochem.](https://doi.org/10.1149/1.1837646) Soc.* **1997**, *144*, [1591–1597](https://doi.org/10.1149/1.1837646).
- [7] M. F. Li, L. W. Liao, D. F. Yuan, D. Mei, Y.-X. Chen, *[Electrochim.](https://doi.org/10.1016/j.electacta.2013.04.096) Acta* **2013**, *110*, 780–789.
- [8] M. Escudero-Escribano, P. Malacrida, M. H. Hansen, U. G. Vej-Hansen, A. Velazquez-Palenzuela, V. Tripkovic, J. Schiotz, J. Rossmeisl, I.E. L. Stephens, I. Chorkendorff, *[Science](https://doi.org/10.1126/science.aad8892)* **2016**, *352*, [73–76.](https://doi.org/10.1126/science.aad8892)
- [9] J. Greeley, I.E. L. Stephens, A. S. Bondarenko, T. P. Johansson, H. A. Hansen, T. F. Jaramillo, J. Rossmeisl, I. Chorkendorff, J. K. Nørskov, *Nat. Chem.* **2009**, *1*, [552–556.](https://doi.org/10.1038/nchem.367)
- [10] Z. W. Seh, J. Kibsgaard, C. F. Dickens, I. Chorkendorff, J. K. Nørskov, T. F. Jaramillo, *Science* **2017**, *355*, eaad4998.
- [11] J. Wu, H. Yang, *Acc. Chem. Res.* **2013**, *46*, [1848–1857.](https://doi.org/10.1021/ar300359w)

- [12] A. Jain, Z. Wang, J. K. Nørskov, *ACS [Energy](https://doi.org/10.1021/acsenergylett.9b00876) Lett.* **2019**, *4*, [1410–1411](https://doi.org/10.1021/acsenergylett.9b00876).
- [13] N. Karmodak, L. Bursi, O. Andreussi, *J. Phys. Chem. Lett.* **2021**, *125*, 58–65.
- [14] Z. Chen, D. Higgins, A. Yu, L. Zhang, J. Zhang, *[Energy](https://doi.org/10.1039/c0ee00558d) [Environ.](https://doi.org/10.1039/c0ee00558d) Sci.* **2011**, *4*, 3167.
- [15] W. Xia, A. Mahmood, Z. Liang, R. Zou, S. Guo, *[Angew.](https://doi.org/10.1002/anie.201504830) Chem. Int. Ed.* **2016**, *55*, [2650–2676](https://doi.org/10.1002/anie.201504830).
- [16] N. Karmodak, O. Andreussi, *J. Phys. [Chem.](https://doi.org/10.1021/acs.jpcc.1c02210) C* **2021**, *125*, [10397–10405](https://doi.org/10.1021/acs.jpcc.1c02210).
- [17] M. Shao, Q. Chang, J.-P. Dodelet, R. Chenitz, *[Chem.](https://doi.org/10.1021/acs.chemrev.5b00462) Rev.* **2016**, *116*, [3594–3657](https://doi.org/10.1021/acs.chemrev.5b00462).
- [18] X. Ge, A. Sumboja, D. Wuu, T. An, B. Li, F. W. T. Goh, T. S. A. Hor, Y. Zong, Z. Liu, *ACS Catal.* **2015**, *5*, [4643–4667.](https://doi.org/10.1021/acscatal.5b00524)
- [19] M. Lefèvre, E. Proietti, F. Jaouen, J.-P. Dodelet, *Science* **2009**, *324*, 71–74.
- [20] G. Wu, K. L. More, C. M. Johnston, P. Zelenay, *[Science](https://doi.org/10.1126/science.1200832)* **2011**, *332*, [443–447](https://doi.org/10.1126/science.1200832).
- [21] E. Proietti, F. Jaouen, M. Lefèvre, N. Larouche, J. Tian, J. Herranz, J.-P. Dodelet, *Nat. Commun.* **2011**, *2*, 416.
- [22] C. H. Choi, H.-K. Lim, M. W. Chung, J. C. Park, H. Shin, H. Kim, S. I. Woo, *J. Am. Chem. Soc.* **2014**, *136*, [9070–9077](https://doi.org/10.1021/ja5033474).
- [23] C. H. Choi, C. Baldizzone, J.-P. Grote, A. K. Schuppert, F. Jaouen, K. J. J. Mayrhofer, *[Angew.](https://doi.org/10.1002/anie.201504903) Chem. Int. Ed.* **2015**, *54*, [12753–12757](https://doi.org/10.1002/anie.201504903).
- [24] U. I. Kramm, M. Lefèvre, P. Bogdanoff, D. Schmeißer, J.-P. Dodelet, *J. Phys. Chem. Lett.* **2014**, *5*, [3750–3756](https://doi.org/10.1021/jz501955g).
- [25] V. Goellner, C. Baldizzone, A. Schuppert, M. T. Sougrati, K. Mayrhofer, F. Jaouen, *Phys. [Chem.](https://doi.org/10.1039/C4CP02882A) Chem. Phys.* **2014**, *16*, [18454–18462](https://doi.org/10.1039/C4CP02882A).
- [26] T. Patniboon, H. A. Hansen, *ACS Catal.* **2021**, *11*, [13102–](https://doi.org/10.1021/acscatal.1c02941) [13118](https://doi.org/10.1021/acscatal.1c02941).
- [27] C. H. Choi, H.-K. Lim, M. W. Chung, G. Chon, N. Ranjbar Sahraie, A. Altin, M.-T. Sougrati, L. Stievano, H. S. Oh, E. S. Park, F. Luo, P. Strasser, G. Dražić, K. J. J. Mayrhofer, H. Kim, F. Jaouen, *Energy Environ. Sci.* **2018**, *11*, [3176–3182.](https://doi.org/10.1039/C8EE01855C)
- [28] L. Osmieri, D. A. Cullen, H. T. Chung, R. K. Ahluwalia, K. C. Neyerlin, *Nano [Energy](https://doi.org/10.1016/j.nanoen.2020.105209)* **2020**, *78*, 105209.
- [29] Z. Chen, S. Jiang, G. Kang, D. Nguyen, G. C. Schatz, R. P. Van Duyne, *J. Am. Chem. Soc.* **2019**, *141*, [15684–15692.](https://doi.org/10.1021/jacs.9b07979)
- [30] Y. Nabae, Q. Yuan, S. Nagata, K. Kusaba, T. Aoki, N. Takao, T. Itoh, M. Arao, H. Imai, K. Higashi, T. Sakata, T. Uruga, Y. Iwasawa, *J. [Electrochem.](https://doi.org/10.1149/1945-7111/abdc64) Soc.* **2021**, *168*, 014513.
- [31] A. Pedersen, J. Barrio, A. Li, R. Jervis, D. J. Brett, M. M. Titirici, I.E. Stephens, *Adv. Energy Mater.* **2022**, *12*, 2102715.
- [32] J. Wang, Z. Huang, W. Liu, C. Chang, H. Tang, Z. Li, W. Chen, C. Jia, T. Yao, S. Wei, *J. Am. [Chem.](https://doi.org/10.1021/jacs.7b10385) Soc.* **2017**, *139*, [17281–17284](https://doi.org/10.1021/jacs.7b10385).
- [33] F. Li, X.-B. Ding, Q.-C. Cao, Y.-H. Qin, C. Wang, *[Chem.](https://doi.org/10.1039/C9CC07489A) Commun.* **2019**, *55*, [13979–13982.](https://doi.org/10.1039/C9CC07489A)
- [34] G. Yang, J. Zhu, P. Yuan, Y. Hu, G. Qu, B.-A. Lu, X. Xue, H. Yin, W. Cheng, J. Cheng, *Nat. Commun.* **2021**, *1734*, 1–10.
- [35] X. Han, X. Ling, D. Yu, D. Xie, L. Li, S. Peng, C. Zhong, N. Zhao, Y. Deng, W. Hu, *Adv. Mater.* **2019**, *31*, 1905622.
- [36] B. Hammer, L. B. Hansen, J. K. Nørskov, *[Phys.](https://doi.org/10.1103/PhysRevB.59.7413) Rev. B* **1999**, *59*, [7413](https://doi.org/10.1103/PhysRevB.59.7413).
- [37] J. Heyd, G. E. Scuseria, M. Ernzerhof, *J. [Chem.](https://doi.org/10.1063/1.1564060) Phys.* **2003**, *118*, [8207–8215](https://doi.org/10.1063/1.1564060).
- [38] J. Heyd, G. E. Scuseria, M. Ernzerhof, *J. Chem. Phys.* **2006**, *124*, 219906.
- [39] K. Mathew, V. S. C. Kolluru, S. Mula, S. N. Steinmann, R. G. Hennig, *J. Chem. Phys.* **2019**, *151*, 234101.
- [40] N. Karmodak, S. Vijay, G. Kastlunger, K. Chan, *ACS [Catal.](https://doi.org/10.1021/acscatal.1c05750)* **2022**, *12*, [4818–4824](https://doi.org/10.1021/acscatal.1c05750).
- [41] M. Feng, X. Wu, H. Cheng, Z. Fan, X. Li, F. Cui, S. Fan, Y. Dai, G. Lei, G. He, *J. Mater. Chem. A* **2021**, *9*, [23817–23827.](https://doi.org/10.1039/D1TA02833B)
- *Angew. Chem.* **2023**, *135*, e202311113 (7 of 8) © 2023 The Authors. Angewandte Chemie published by Wiley-VCH GmbH

# *Forschungsartikel*

15213757, 2023, 47, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ange.202311113 by University Of Science, Wiley Online Library on [06/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

- [42] Y. Wang, B. J. Park, V. K. Paidi, R. Huang, Y. Lee, K.-J. Noh, K.-S. Lee, J. W. Han, *ACS Energy Lett.* **2022**, *7*, [640–649.](https://doi.org/10.1021/acsenergylett.1c02446)
- [43] Z. Zeng, L. Y. Gan, H. B. Yang, X. Su, J. Gao, W. Liu, H. Matsumoto, J. Gong, J. Zhang, W. Cai, et al., *Nat. Commun.* **2021**, *4088*, 1–11.
- [44] H. Li, S. Kelly, D. Guevarra, Z. Wang, Y. Wang, J. A. Haber, M. Anand, G. T. K. K. Gunasooriya, C. S. Abraham, S. Vijay, J. M. Gregoire, J. K. Nørskov, *Nat. Catal.* **2021**, *4*, [463–468.](https://doi.org/10.1038/s41929-021-00618-w)
- [45] I. C. Man, H.-Y. Su, F. Calle-Vallejo, H. A. Hansen, J. I. Martínez, N. G. Inoglu, J. Kitchin, T. F. Jaramillo, J. K. Nørskov, J. Rossmeisl, *[ChemCatChem](https://doi.org/10.1002/cctc.201000397)* **2011**, *3*, 1159–1165.
- [46] a) H. A. Hansen, V. Viswanathan, J. K. Nørskov, *J. [Phys.](https://doi.org/10.1021/jp4100608) Chem. C* **2014**, *118*, [6706–6718](https://doi.org/10.1021/jp4100608); b) H. Wan, A. W. Jensen, M. Escudero-Escribano, J. Rossmeisl, *ACS [Catal.](https://doi.org/10.1021/acscatal.0c01085)* **2020**, *10*, 5979– [5989.](https://doi.org/10.1021/acscatal.0c01085)
- [47] S. R. Kelly, C. Kirk, K. Chan, J. K. Nørskov, *J. Phys. [Chem.](https://doi.org/10.1021/acs.jpcc.0c02127) C* **2020**, *124*, [14581–14591](https://doi.org/10.1021/acs.jpcc.0c02127).

- [48] J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard, H. Jónsson, *J. Phys. [Chem.](https://doi.org/10.1021/jp047349j) B* **2004**, *108*, [17886–17892](https://doi.org/10.1021/jp047349j).
- [49] a) K. A. Persson, B. Waldwick, P. Lazic, G. Ceder, *Phys. Rev. B* **2012**, *85*, 235438; b) L. P. Granda-Marulanda, I. T. McCrum, M. T. M. Koper, *J. Phys. [Condens.](https://doi.org/10.1088/1361-648X/abf19d) Matter* **2021**, *33*, 204001.
- [50] A. K. Singh, L. Zhou, A. Shinde, S. K. Suram, J. H. Montoya, D. Winston, J. M. Gregoire, K. A. Persson, *Chem. [Mater.](https://doi.org/10.1021/acs.chemmater.7b03980)* **2017**, *29*, [10159–10167](https://doi.org/10.1021/acs.chemmater.7b03980).
- [51] N. Karmodak, O. Andreussi, *ACS [Energy](https://doi.org/10.1021/acsenergylett.9b02689) Lett.* **2020**, *5*, 885– [891](https://doi.org/10.1021/acsenergylett.9b02689).

Manuscript received: August 1, 2023 Accepted manuscript online: September 27, 2023 Version of record online: October 16, 2023