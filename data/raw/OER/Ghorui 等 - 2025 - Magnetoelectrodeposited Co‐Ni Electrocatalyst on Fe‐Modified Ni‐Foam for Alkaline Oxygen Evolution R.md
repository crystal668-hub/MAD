---
source: Ghorui 等 - 2025 - Magnetoelectrodeposited Co‐Ni Electrocatalyst on Fe‐Modified Ni‐Foam for Alkaline Oxygen Evolution R.pdf
tool: marker
duration: 47.865s
generated: 2026-01-09T06:39:11.797048Z
---

Check for updates

www.chemcatchem.org

# Magnetoelectrodeposited Co-Ni Electrocatalyst on Fe-Modified Ni-Foam for Alkaline Oxygen Evolution Reaction

Bapi Ghorui, [a] Haribalakrishnammal Vaidyanathan, [b] Isha Singh, [b] Moitrayee Chatterjee, [b] and Rai Ganesh S. Pala\*[a, b, c]

Applying external magnetic field facilitates the oxygen evolution reaction (OER), but such a strategy is impractical for large-scale applications. We introduce a scalable alternative by applying magnetic fields only during catalyst electrodeposition. We further propose a design principle for magnetoelectrocatalyst wherein electrocatalysis of active sites is enhanced by magnetic field impressed in the vicinity of active sites using a less active element having high magnetic saturation. This principle is demonstrated using monometallic systems (FTO/Ni and FTO/Co) and then extended it to develop a multimetallic magnetoelectrodeposited (MED) catalyst (NF/Fe-NiCo-MED). A Fe-modified Ni-foam (NF/Fe) substrate was prepared via galvanic displacement, onto which Ni, Co, or NiCo were electrodeposited under a 0.6 T field. The resulting NF/Fe-NiCo-MED magneto catalysts exhibited enhanced remanence, saturation magnetization, and ECSA and lower charge-transfer resistance compared to counterparts NF/Fe-NiCo-no MED deposited without external magnetic field. The NF/Fe-NiCo-MED demonstrated excellent OER performance, with a low overpotential of 273.26 mV at 100 mA/cm<sup>2</sup> and sustained stability for 72 h in alkaline media. Notably, NF/Fe-NiCo-MED outperforms benchmark NiCo-based layered double hydroxide (LDH) catalysts and even multimetallic systems operated under an external magnetic field during alkaline OER.

#### 1. Introduction

Solar or wind-powered alkaline water electrolysis is being intensely explored for green H<sub>2</sub> generation, wherein a critical challenge is the high overpotential for oxygen evolution reaction (OER). Over the last decade, researchers have improved OER rates by coupling water electrolysis to an external magnetic field. [1-6] Imposing a magnetic field during OER assists in reorganizing magnetic domains of the spin-dependent transition metal-based-electrocatalyst.<sup>[7-9]</sup> However, applying magnetic field externally is impractical for large-scale industrial applications. To address this issue, we explore electrodeposition of ferromagnetic transition metals electrocatalysts in the presence of a magnetic field, so that magnetoelectrodeposited (MED) electrocatalysts can be retrofitted into electrolyzers without any further external magnetic field.

One operational mechanism for magnetoelectrodeposition (MED) is the magnetohydrodynamic (MHD) effect driven by the Lorentz force.[10] The Lorentz force is minimal when the magnetic field is parallel to the electric field, but still, a concentration

[a] B. Ghorui, R. G. S. Pala Material Science Programme, IIT Kanpur, Kanpur 208016, India E-mail: rpala@iitk.ac.in

[b] H. Vaidvanathan, I. Sinah, M. Chatteriee, R. G. S. Pala Department of Chemical Engineering, IIT Kanpur, Kanpur 208016, India

[c] R. G. S. Pala Nuclear Engineering & Technology Programme, IIT Kanpur, Kanpur 208016,

Supporting information for this article is available on the WWW under https://doi.org/10.1002/cctc.202500516

gradient can be generated, which affects electrodeposition.[11] It is maximized when the magnetic field is perpendicular to the electric field or current. The Lorenz force drive convection in the electrolyte, enhancing the transport of electroactive species. Thus, the MED technique improves mass loading, increases the surface coverage with finer granules of electroactive particles and results in increased electrochemically active surface area (ECSA) through the MHD effect and enhanced mass transport of the charged ions or radicals toward cathode by minimizing concentration gradients.[12]

$$\vec{f}_{\perp} = \vec{j} \times \vec{B} \tag{1}$$

$$\stackrel{\rightarrow}{f} \nabla_c = \frac{\chi_m B^2}{2\mu_0} \stackrel{\rightarrow}{\nabla}_c \tag{2}$$

In Equation (1)  $f_L$  is the Lorentz force, i and B represent current density (flux of ions in the electrolyte) and magnetic flux, respectively In Equation (2)  $f \nabla_c$  is the concentration gradient forces, c is the concentration of ions,  $\mu_0$  is the vacuum permeability, and  $\chi_m$  is the molar magnetic susceptibility.<sup>[13]</sup> Saha J et al. and Elias L et al. revealed that the MED technique can also modulate the coercivity, retentivity, and structural morphology of electrodeposits. [12,14] Aboelazm et al. reported that using the magnetic field during electrodeposition effectively improved the deposition of cobalt oxide (Co<sub>3</sub>O<sub>4</sub>) nanostructures with a larger electroactive surface area.[15] According to the Sabatier principle, the best OER catalyst should have the optimal binding energy or interaction strength to balance the adsorption and desorption of reactants and intermediates (OH\*, O\*, OOH\*).[16,17] The d-band center theory, along with the activity volcano plot,

<span id="page-1-0"></span>provides guideline in selecting appropriate materials.[18] Nickel foam (NF) offers high surface area, good mechanical scaffolding, flexibility, and chemical stability in alkaline medium and operational potential window for OER.[19,20] Ni is compatible with other magnetically active transition metals (e.g., Co and Fe) to form alloys or mixed oxides that often exhibit superior catalytic activity compared to individual metals.<sup>[21]</sup> Fe is known to significantly improve the OER performance when combined with Ni, providing additional active sites (ECSA) and altering the electronic structure to facilitate the reaction. Therefore, adding Fe to NF increases the local structure's roughness or disorder.[22-25] Bell et al.'s recent DFT analysis revealed that FeOOH is insufficiently conductive to function as a catalyst at low overpotential. [26] Zhao et al. performed a systematic computational screening of 3dlayered (oxy) (hydro)oxides electrocatalysts for both OER and ORR for metal double hydroxides M(OH)<sub>2</sub>, oxyhydroxides MOOH and oxides MO<sub>2</sub>(M = Fe, Ni, and Co). Based on first-principle calculations, they predicted that CoOOH/CoO2 and NiOOH/NiO2 are potentially active and stable alkaline OER catalysts. [27] However, Burke et al. reported that the addition of Fe in metal oxyhydroxides dramatically enhances OER electrokinetic and shows the best binding energy with -OH, -OOH intermediates when combined with a conductive host matrix, such as Ni or Co.[28,29] Therefore, we selected Fe-modified NF as an appropriate substrate to design OER electrocatalyst for this work. In this study, 6.5 to 7 wt% Fe was deposited onto the surface of NF by galvanostatic replacement to obtain Fe-modified NF electrocatalyst substrate denoted as NF/Fe. Also, we imagined that the Fe-layer on the Ni surface might introduce a spin-pinned long-range magnetic ordering of the metals (Co and Ni, in the present study) electrodeposited in the presence of an external magnetic field onto NF/Fe. The oxidation of Ni<sup>+2</sup> to Ni<sup>+3</sup> at lower potentials is facilitated by Co addition to NF/Fe.[25] Better OER activity enhancement was seen as ECSA augmented when the number of dopants increased from monometallic to multimetallic catalyst.[30] Hamal E et al. observed that addition of Co to NiFeOOH improved its overall electronic conductivity and decreased the OER overpotentials.[31] Yibing et al. studied Co<sub>x</sub>Ni<sub>1-x</sub>Fe<sub>2</sub>O<sub>4</sub>-nanosheet over NF by varying the Co content and found that Co promotes spin activation during OER as compared to Ni due to the greater magnetic saturation of Co.[32]

The OER activity of magnetoelectrocatalyst is governed by interconnected factors, such as composition, morphology, surface area, mass loading, and magnetic properties, all of which evolve simultaneously during MED. This complexity makes isolating individual effects challenging. To address this, we propose semi-quantitative design principles for effective magnetoelectrocatalyst, validated through control experiments involving individual electrodepositions of Ni and Co on nonmagnetic FTO substrates, with and without a magnetic field. These experiments brought out the symbiosis of Ni's superior OER activity and Co's excellent magnetic properties. Note that Co is a reasonable OER electrocatalyst, but less active than Ni, and Ni has reasonable magnetic properties, but lesser in strength compared to Co. The critical design principle is to utilize a strong "atomic magnet" Co in the vicinity of magnetically enhanceable Ni active site. The design trade-off is the gain in magnetic OER activation of Ni by Co versus the loss in inherent OER activity of the surface because of the replacement of Ni by Co, as Ni is inherently a better OER electrocatalysts (in the absence of the magnetic field) compared to Co. Therefore, the co-deposition of Ni with Co is expected to bring out a synergistic enhancement, combining catalytic efficiency and magnetic activation for optimal multimetallic catalyst performance.

We further explored two sets of electrocatalysts; one set is multimetallic (Fe, Ni, Co) MED and another is electrodeposited without applying a magnetic field. The electrocatalytic OER performance of three distinct compositions (NF/Fe-Ni, NF/Fe-Co, and NF/Fe-NiCo) was compared in 1 M KOH in the presence (OER-H) and absence of a magnetic field (OER-0). These OER electrocatalysts are abbreviated as EC-MED and EC-no MED where "EC" (electrocatalyst) refers to NF/Fe-Ni, NF/Fe-Co, and NF/Fe-NiCo. However, to differentiate the alkaline OER conditions, we have used these notations OER-H (OER in the presence of a magnetic field) and OER-0 (OER in the absence of a magnetic field). Among all the designed catalysts, NF/Fe-NiCo-MED [OER-0] showed the best activity in terms of lower OER overpotential (273.26 mV) compared to NF/Fe-NiCo-no MED [OER-H] (286.96 mV at 100 mA/cm<sup>2</sup>). The overpotentials (3.9% reduction) and the Tafel slope (8.2% reduction) can be further minimized by using an external magnetic field during OER performance for the electrocatalyst NF/Fe-NiCo-MED [OER-H] compared to NF/Fe-NiCo-MED [OER-0]. Overall, by exploring MED electrocatalysts via a rational design principle implementable via a scalable strategy, this work provides pointers to the practical implementation of magnetic enhancement of OER.

#### 1.1. Design Principle for Magnetoelectrocatalyst

#### 1.1.1. Monometallic Catalyst

Before we generalize, it is good to approach the design principle in a specific context of magnetic modulation of OER in Ni and Co. At first order, the electrocatalyst's activity is not only dependent on the inherent electrocatalytic activity of the individual components but also on the modulation of OER activity due to the magnetic field. Thus, the catalyst's OER activity (A) is the function of surface coverage  $(\theta)$  of the electrodeposited metals and the overall magnetization of the catalyst.

$$A = A \left( \theta_{\mathsf{Co}}, \theta_{\mathsf{Ni}}, M \right) \tag{3}$$

The variation in the catalysts can be accomplished by varying either the catalytic components or by varying the magnetization at the atomic level. In the modulation via premagnetized catalysts approach (as opposed to imposing an external magnetic field), the magnetic elements can be imagined to act as "atomic magnets" modulating the OER activity of sites in the vicinity.

Therefore,

$$\delta A = \left(\frac{\partial A}{\partial \theta_{CO}}\right)_{M} d\theta_{CO} + \left(\frac{\partial A}{\partial \theta_{Ni}}\right)_{M} d\theta_{Ni} + \left(\frac{\partial A}{\partial M}\right)_{\theta} dM \tag{4}$$

8673899,

| Table 1. Electrochemical OER performance of monometallic catalyst. |           |        |           |        |  |
|--------------------------------------------------------------------|-----------|--------|-----------|--------|--|
| Activity parameter                                                 | Catalyst  |        |           |        |  |
|                                                                    | Ni-no MED | Ni-MED | Co-no MED | Co-MED |  |
| Mass deposited (mg)                                                | 3.2       | 5.01   | 5.4       | 8.3    |  |
| ECSA (cm <sup>2</sup> )                                            | 89.8      | 273.5  | 55.8      | 123.9  |  |
| Over potential (V) at 10 mA/cm <sup>2</sup>                        | 153       | 146.5  | 361       | 348    |  |
| Current density J <sub>GSA</sub> (mA/cm <sup>2</sup> ) at 1.65 V   | 21.76     | 25.31  | 16.87     | 17.32  |  |
| Specific activity (mA/mg)                                          | 6.8       | 5.05   | 3.12      | 2.08   |  |
| Tafel slope (mV/dec.)                                              | 168       | 123    | 176       | 141    |  |

$$\frac{\partial A}{\partial M} = \frac{\partial A}{\partial \theta_{\text{co}}} \cdot \frac{\partial \theta_{\text{co}}}{\partial M} + \frac{\partial A}{\partial \theta_{\text{Ni}}} \cdot \frac{\partial \theta_{\text{Ni}}}{\partial M} \tag{5}$$

As inherent activity and capabilities of magnetization are intercoupled, an optimization of these coupled properties has to be accomplished. Toward this, we carried out individual electrodepositions of Co on nonmagnetic FTO substrates and Ni on nonmagnetic FTO substrates with and without a magnetic field (MED), using identical conditions (precursor concentration, pH, deposition time, and applied electrochemical potential, as outlined in Section 4.3 later).

The monometallic control experiments on FTO enable us to: i) assess the role of magnetic domain contribution independently from compositional variation in a bimetallic system. ii) Exclude magnetic substrate-induced effects on OER activity. Although some variation in mass loading is unavoidable (as the overpotential will be different for Co and Ni), the decrease in compositional complexity enables the culling out of some simple trends.

These experimental results suggest that:

Improvement of electrochemical OER performance via MED: Electrochemical analysis revealed that monometallic Co-MED and Ni-MED catalysts demonstrated superior alkaline OER performance relative to their non-MED counterparts. This includes lower overpotentials, smaller Tafel slopes, and higher current densities at 1.65 V. Electrochemical OER performance is briefly summarized in Table 1.

*Increase in mass loading via MED:* During electrodeposition, the application of a magnetic field generates a Lorentz force, inducing convective motion in the electrolyte (self-stirring) and enhancing the transport of Ni<sup>2+</sup> and Co<sup>2+</sup> ions due to a decrease mass transfer boundary layer thickness.<sup>[11]</sup> This resulted in higher metal deposition in the MED samples compared to the non-MED ones, as evidenced by the data in Table 2.

From the above data Table 2, it can be observed that although the mass deposition for Co-MED is higher than that for Ni-MED, the increment in current density (normalized by GSA) is greater for Ni-MED.

It is also important to note that the specific activity of MED catalysts is lower compared to their non-MED counterparts. This may be attributed to the increased thickness of the MED cata-

| Table 2. Effect of ME           | D on deposited mass and cu                                        | rrent density.                                                                                          |
|---------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Catalyst<br>deposited on<br>FTO | Deposited mass<br>difference<br>between MED<br>and no-MED<br>(mg) | Increament in<br>current density<br>with respect to<br>no-MED J <sub>GSA</sub><br>(mA/cm <sup>2</sup> ) |
| Ni                              | (5.01–<br>3.2) = 1.81mg                                           | 16.3%                                                                                                   |
| Со                              | (8.3-5.4) = 2.66 mg                                               | 2.66%                                                                                                   |

lyst, which enhances mass but does not significantly contribute to surface-level catalytic activity.

Different magnetic attributes of Ni and Co: The magnetic hysteresis loop results from the motion and partial reversal of magnetic domains under an external field, providing insights into domain wall pinning and magnetic anisotropy. In ferromagnetic materials, higher values of saturation magnetization (Ms), remanent magnetization (Mr), and coercive field (Hc) obtained from the hysteresis loop indirectly indicate a more ordered, anisotropic, and possibly single-domain structure—attributes that contribute to enhanced magnetic hardness. In this study, the reported values of Ms and Mr were normalized by the catalyst mass and hence, these are intensive properties.

In Ni-MED samples, the higher saturation magnetization (Ms) and remanent magnetization (Mr) correlate with a notable improvement in OER activity (16.3%) compared to the Ni-no MED sample. In contrast, although Co-MED exhibits similarly enhanced Ms and Mr values (Figure 2), its activity shows only a modest increase (2.66%). The crucial observation from the studies are: Ni has higher OER activity but moderate magnetization whereas Co has higher magnetization but only moderate OER activity. The change in activity with respect to magnetization  $\left(\frac{\partial A}{\partial M}\right)_{\alpha} dM$  suggests that Co can serve as a strong atomic magnet incorporated in the vicinity of Ni matrix, within the multimetallic magnetoelectrocatalyst. In this configuration, Co may function as an in situ magnet, promoting spin-polarized pathways for efficient triplet O2 formation via Ni OER active site. The higher coercive field of Co-MED suggests that for a catalytic application, the in situ magnets can sustain magnetic field to promote OER activity for longer time.

19, Downloaded from https://chemistry-urope.onlinelibrary.wie/.com/doi/10.1002/cctc.20250516 by University O'Science, Wiley Online Library on [07/01/205]. See the Terms and Conditions (https://onlinelibrary.wie/.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licenses

<span id="page-3-0"></span>Figure 1. a) XRD pattern, b) VSM analysis, and c) LSV plot.

Figure 2. VSM analysis of monometallic system.

Structural and morphological analysis: In Figure 1 the XRD and FESEM analyses (Figure S2) show that metallic Co-deposited via MED formed snowflake-like structures (predominantly hexagonal close-packed phase), whereas Ni formed fcc structures resembling acropora coral. In both cases, MED resulted in finer metallic particles and more uniform surface coverage compared to no-MED deposition—paralleling the morphological improvements observed in our NiFe/NF-MED samples having higher ECSA. The detailed description of structural and morphological changes of the monometallic electrocatalyst mention in the Figure S2.

#### 1.1.2. Multimetallic Catalyst

In multimetallic magnetoelectrocatalyst if we can in corporate Co in the host matrix (NF/Fe), the  $(\frac{\partial A}{\partial \theta_{CO}})_M d\theta_{CO}$  term in Equation (4) will decrease OER activity as Co has a lesser inherent OER activity compared to Ni. However, this decrease in activity can be compensated by  $(\frac{\partial A}{\partial M})_{\theta} dM$  term, which is indicative of the magnetic enhancement of OER activity. Therefore, in a codeposited MED catalyst (NF/Fe-NiCo), we anticipate a synergistic

effect: Co enhances the magnetic domain structure and acting as an in situ magnet, promotes spin-polarized mechanism for efficient triplet  $O_2$  formation via Ni. In Figure 3, we schematically illustrate the above enunciated design principle for an optimum magneto electrocatalyst (Figures 1, 2, and 8.)

#### 2. Results and Discussion

#### 2.1. Materials Characterization

#### 2.1.1. Structural Analysis Through FE-SEM and XRD

In the FE-SEM images (Figure 4), it was observed that the main basic mixed hexagonal and pentagonal network of porous nickel foam remains unchanged in all catalysts. In Fe-modified Ni-foam (NF/Fe), iron oxide deposits were observed on the surface of the NF (Figure 1b<sub>1</sub>). The "cauliflower-like spherical" morphology of electrodeposited Co was seen in both MED and electrodeposition without an external magnetic field. Different surface morphologies can be correlated to deposition rates, finer deposited particles, and high electrochemical surface areas. Ni and Co are magnetically active both in metallic form in solid state and ionic form in solution. Therefore, in the presence of a magnetic field Ni<sup>2+</sup> and Co<sup>2+</sup> ions containing electrolyte experience convective force due to the Lorentz force, which enhances the mobility of charged species toward the cathode and improves mass transfer via the MHD effect.

As a result, during MED, the electrodeposited mass of the individual metal (Ni, Co) increased (Table S1). Specifically, the Co deposition rate was greatly influenced by the external magnetic field compared to Ni, as is evident from the chronoamperometry plots during electrodeposition; the higher current indicates an increment in the Ni-Co amount during electrodeposition (Figure S3). The surface compositional information (in atomic wt%) was obtained from EDS elemental mapping. It was observed that for NF/Fe-NiCo-no MED (Figure 4C<sub>3</sub>) the amount of Co was 51.4%, Ni-46.1%, O-2.2%. and Fe-0.2% and in Figure 4d<sub>3</sub> for NF/Fe-NiCo-MED the percentage of Co-61.24%, Ni-34.3%, O-4.2%, and Fe-0.2%, respectively. In Figure 4, from C<sub>1</sub> and C<sub>2</sub>, it was observed that the electrodeposition of Ni-Co occurred on the edges of

18673899, 2025, 19, Downloaded from https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cctc.202500516 by University Of Science, Wiley Online Library on [07/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<span id="page-4-0"></span>**Figure 3.** Design of a multimetallic magnetoelectrocatalyst surface.

**Figure 4.** SEM images: row 1-over all network image 100 μm scale and row 2-magnified image 10 μm scale; row 3-EDS mapping of: a 1–3)-nickel foam (NF); b1–3)-iron modified nickel foam NF/Fe; c1–3)-NF/Fe-Ni Co-no MED; and d1–3)-NF/Fe-NiCo-MED.

NF/Fe. When the metal substrate (like NF) is utilized, greater electrodeposition occurs at the edges, perhaps because of the greater concentration of the electric field along the edges. However, in the presence of the magnetic field (NF/Fe-NiCo–MED), the electrodeposition of Ni and Co not only occurred at the edges of NF/Fe but also at the basal area, which is evident from Figure [4d1,d2.](#page-4-0) In the case of NF/Fe-NiCo–MED, the electrodeposition of finer granules on NF/Fe surface influences the increment of overall ECSA and improves surface roughness of the electrocatalyst. The experimentally observed magnetic moment of Co<sup>2</sup><sup>+</sup> is 4.3–5.2 BM, which is higher than that for Ni2<sup>+</sup> is 2.8– 3.5 BM.[\[33\]](#page-11-0) As a result, in the presence of a magnetic field, the amount of Co deposition is much higher than Ni, as from atomic wt% from EDS. Therefore, increasing the amount of Co on NF/Fe can be correlated to improving the overall ECSA of NF/Fe-NiCo (Figure S5). Electrodeposition of Ni and Co (1:1 molar ratio) in the presence of a magnetic field promoted an increase in the active surface area 91.2% from 138.3 cm<sup>2</sup> (NF/Fe-NiCo–no MED) to 264.5 cm<sup>2</sup> (NF/Fe-NiCo–MED). The increment in electrochemically active accessible surface area would definitely help to increase catalytic activity. In case of NF/Fe-Co–MED the ECSA obtained was higher than that of NF/Fe-Ni–MED. However, the observed specific activity was less per active site because of the presence of higher percentage of Co which is less OER active than Ni which could be further justified by the higher charge transfer resistance obtained from EIS of NF/Fe-Co–MED.[\[27,34\]](#page-11-0)

We have performed BET surface area measurements of three representative samples: i) the catalyst substrate NF/Fe, ii) NF/Fe-NiCo prepared via MED, and iii) NF/Fe-NiCo prepared without a magnetic field (no MED). All three samples exhibited type IV isotherms, confirming the coexistence of mesoporous and microporous structures. Despite a reduction in the BET surface area for the MED sample, a significant increase in ECSA is observed. This apparent contradiction underscores the distinction between the total surface area and electrochemically accessible surface area. MED improves active site accessibility, thereby boosting ECSA. Additional comments of the BET surface analysis is provided in Figure S6.

In the XRD pattern (Figure 5), three crystal planes (111), (200) and (220) of FCC nickel foam are observed for all the catalysts at the diffraction angles 44.52°, 51.85°, and 76.37°, respectively (JCPDS card no-65–2865).[\[19,22\]](#page-11-0) In the Fe-modified NF, as the atomic radius of Fe (1.26 A°) is larger than Ni, a shift in the diffraction angle to larger 2θ (0.2 to 0.4°) is expected for each of the planes in NF/Fe. However, the intensity of the crystal planes gradually decreased in the case of NF/Fe-NiCo-MED catalyst due to surface coverage by metal oxide.

The peak broadening in the diffraction pattern indicates that the catalyst had a mixed amorphous and crystalline character. It was observed that after OER, the catalyst surface becomes more layered oxide of Co3O4 or NiCo2O4 and the intensity of the diffraction pattern further reduced.[\[35\]](#page-11-0)

The lattice parameter of Ni and Co are similar ∼3.535 A°, therefore in the XRD pattern of electrocatalyst, Ni-predominated crystal planes were observed (since it is present in high amounts as NF was used to prepare the catalyst support) and it was difficult to distinguish Co oxide and nickel oxide peak.

**Figure 5.** XRD pattern of the synthesized electrocatalyst.

#### *2.1.2. Analysis of Electronic Properties of Electrocatalysts*

XPS analysis, coupled with Gaussian fitting methods using XPS PEAK41 software, allows for a comprehensive characterization of the oxidation states and electronic structures of Ni, Co, and O in the material NF/Fe-NiCo catalyst, contributing to a deeper understanding of its electrical properties and potential applications.

For nickel, the XPS analysis after electrodeposition (Figure [6a\)](#page-6-0) reveals the presence of Ni<sup>2</sup><sup>+</sup> and Ni3<sup>+</sup> mixed oxidation states, characterized by distinctive peaks in the Ni 2p emission spectrum.[\[36–38\]](#page-11-0) The peaks at 855.43 eV (2p3/2) and 872.79 eV (2p1/2) correspond to Ni2+, whereas the peaks at 856.18 and 874.98 eV are ascribed to Ni<sup>3</sup>+. In addition, at 852.16 eV a metallic peak and three strong shakeup-type peaks of nickel at 861.409, 869.50, and 879.7 eV were also found, indicating complex electronic interactions within the material. We fitted Co 2p3/2 peaks (Figure [6b\)](#page-6-0) at binding energy values of 780.44 and 781.34 eV to Co<sup>3</sup><sup>+</sup> and Co<sup>2</sup>+, respectively, and Co 2p1/2 peaks at binding-energy values of 796.28 and 797.67 eV to Co<sup>3</sup><sup>+</sup> and Co<sup>2</sup>+, respectively, along with weak satellite peaks at 786.5, 805.08, 790.8, and 803.52 eV due to the presence of Co3O4 on the top of iron modified nickel foam.[\[39\]](#page-11-0) Three oxygen contributions are present in the O1s spectra (Figure [6c\)](#page-6-0), which we have identified as O1, O2, and O3. At 529.28 eV, the component O1 is characteristic of metal–oxygen bonding. The O2 component, which is typically linked to oxygen in OH∼ groups, is present at 530.67 eV in the O1s spectra, indicating the surface of the NiCo2O4. During electrodeposition the surface may hydroxylated to some extend in aqueous electrolyte by substitution of surface oxygen. The high binding energy oxygen component O3 at 531.583 eV has been linked to oxygen ions in low coordination at the surface. The spectral area ratio of atomic and ionic Ni and Co was calculated and compared between NF/Fe-NiCo-no MED and NF/Fe-NiCo–MED. It was observed that the ratio of Co2+/Co<sup>3</sup><sup>+</sup> was reduced in the case of NF/Fe-NiCo–MED. (1) Compared to NF/Fe-NiCo–no MED. (1.7) (Table S2). This is a clear indication that EC-MED contains a

<span id="page-6-0"></span>**Figure 6.** XPS fitting curve of NF/Fe-NiCo synthesized in different conditions (MED and no MED): a) Ni 2p, b) Co 2p, and (c) O 1s.

**Figure 7.** a) Hysteresis loop of NF, NF/Fe, NF/Fe-Ni-MED, NF/Fe-Co-MED, NF/Fe-Ni Co-no MED, and NF/Fe-Ni Co-MED. b–d) Comparative trends of remanence, magnetic saturation, and coercivity.

higher concentration of Co3<sup>+</sup> at the catalyst surface, which has a direct impact on the OER rates.[\[36\]](#page-11-0) In case of EC-MED, the atomic ratio of Ni/Co at the catalyst surface is close to unity (∼1.2), which implies 1:1 stoichiometric ratio of Ni-Co at the surface.

#### *2.1.3. Comparison of Magnetic Properties of As-Prepared EC-No MED and EC-MED Catalyst*

The magnetic properties of the MED catalyst were evaluated using hysteresis loops (Figure 7a). The loop reflects the behavior of magnetic domains under an external field, revealing domain wall pinning and magnetic anisotropy. Due to internal stress from crystal defects, impurities, and grain boundaries, magnetic domains do not fully revert to their original state when the field is removed, resulting in hysteresis.[\[40\]](#page-11-0) This causes a lag in magnetic induction (B) or magnetization (Ms) relative to changes in the applied field (H). Compared to the NF/Fe-NiCo–no MED catalyst, the NF/Fe-NiCo– MED catalyst exhibited significant improvements: a 60.79% increase in remanence (Figure 7b), a 16.63% increase in saturation magnetization (Figure 7c), and a 51.6% increase in coercivity (Figure 7d). These enhancements indirectly suggest that the applied magnetic field during electrodeposition promotes the formation of larger magnetic domains; hence, the domains for EC-MED > EC-no MED . The presence of higher remanence, saturation magnetization and higher coercivity in

<span id="page-7-0"></span>

| Table 3. EIS analysis. |               |          |        |       |
|------------------------|---------------|----------|--------|-------|
| Catalyst               | Description   | Cdl (mF) | Rct () | Rs () |
| NF/Fe-Ni               | MED, EIS-0    | 340      | 18.14  | 3.47  |
| NF/Fe-Co               | MED, EIS-0    | 333      | 27.34  | 3.12  |
| NF/Fe-NiCo             | MED, EIS-0    | 367      | 16.57  | 3.6   |
|                        | MED, EIS-H    | 347      | 15.75  | 4.15  |
|                        | no–MED, EIS-H | 333      | 19.82  | 3.31  |

**Figure 8.** Nyquist plot collage with Randles circuit.

as-prepared NiCo-MED, OER-0 catalysts are responsible for the improvement in OER activity without applying a magnetic field during OER. The larger coercive field of NiCo-MED suggests that for a catalytic application, these in situ magnets can sustain magnetization to activate OER activity. While our results suggest that magnetic ordering particularly through cobaltinduced effects may facilitate spin-polarized pathways that enhance OER activity, we acknowledge that this link remains inferential. Direct experimental evidence confirming a causal relationship between intrinsic magnetic properties and catalytic performance is still required. Therefore, the proposed spin-polarization mechanism should be viewed as a working hypothesis that warrants further investigation, particularly via operando spin-resolved measurements that are able to map spin structure at an atomic level. Such studies will be able to establish a definitive basis for magnetic underpinnings of OER electrocatalysis.

#### **2.2. Electrochemical Impedance Spectroscopic Characterization of the Electrocatalysts**

In Table 3, different resistances (Rsolution and Rct) and the capacitance of the electrical double layer (EDL) in the Faradaic region are listed, which were obtained from simulated Nyquits plot (Figure 8). The EIS results were measured at 1.47 V (versus RHE) which is beyond the potential required for the phase transition of Ni(OH)2 to NiOOH. The capacitance(Cdl) was due to reactive intermediates (O\*, OH\*, and OOH\*).[\[41\]](#page-11-0) In case of NF/Fe-NiCo-MED, [OER-0] electrocatalytic activity is higher in terms of current density and lower Tafel slope, which is correlated to the lower charge transfer resistance(Rct) value of 16.57 Ω and higher capacitance value (average 367 mF). Although using a magnetic field of 0.6 T during the OER process decreases the Rct of MED catalyst by 4.9%, this is not an industrially viable method. Magnetic fields can influence the organization and orientation of the charged species in the double layer, affecting the surface charge density and the thickness of the double layer of MED catalysts. This, in turn, can impact on the double-layer capacitance (Cdl) and electroactive surface area.[\[42\]](#page-11-0)

Although NF/Fe-Co-MED had a higher Cdl value (333 mF) due to higher electrodeposited mass loading (Table S1), the in-plane conductivity decreased and hence, the electron transfer was hindered by the insulating particles which were reflected from the highest Rct value (27.34 Ω) among all the Ni-foam modified catalysts and makes NF/Fe-Co-MED as bad OER performer.[\[43\]](#page-11-0) The oxidation of Ni(OH)2 to conducting NiOOH is facilitated by the addition of Co into the NF/Fe matrix. Although the charge transfer resistance of NF/Fe-Co is the largest among all the synthesized catalysts, the Rct value of NF/Fe-NiCo decreased by 65% (27.34 to 16.57 ), which is the highest decrement compared to Ni and NiCo- no MED. To summarize, although Co reduces its Rct value to a great extent, its value is still greater than NF/Fe-Ni and NF/Fe-NiCo. Thus, it is always better to use co-deposited NiCo as a catalyst rather than using NF/Fe-Ni or NF/Fe-Co individually. The solution resistance remained constant within the range of 3.1–4.2 for all NF-modified catalysts.

#### **2.3. Alkaline OER Performance of the Electrocatalyst**

Figure [9](#page-8-0) compares the electrochemical activity and stability toward the alkaline OER of the electrocatalysts prepared under different conditions. There were two signature peaks at 1.33 V and 1.41 V in the case of multimetallic NF/Fe-NiCo and all other catalysts in the LSV curve Figure [9a,b.](#page-8-0) The first peak is the formation of Ni (OH)2 and the next one depicts the Ni(OH)2 to NiOOH transformation.[\[44,45\]](#page-11-0) In NF/Fe-Co and NF/Fe-NiCo, the increase in peak height suggests that Co promotes a more facile transition of Ni (OH)2 to NiOOH.[\[25\]](#page-11-0) Hence, the formation of the more conductive NiOOH at a lower potential is responsible for the further OER enhancement of the NF/Fe-NiCo catalyst. For MED NF/Fe-NiCo-MED, we observed a drastic change in the peak pattern peaks for Co as well as Ni.

The peak at 1.22 V is the signature peak of the transformation of Co (OH)2 to CoOOH.[\[46\]](#page-11-0) Peaks of Ni are also shifted to a lower potential region from 1.41 to 1.37 V in the case of NiCo-MED. As expected from the experimentally observed magnetic spin moment value, the cobalt ion (3d<sup>7</sup> ) is more magnetic in nature compared to the Nickel ion (3d8). Therefore, during MED, the surface concentration Co on NF/Fe is higher as supported by EDX (Figure [4\)](#page-4-0) and chronoamperometry plots (Figure S3 and Table S1). Thus, in case of MED catalyst NF/Fe-NiCo-MED it was observed

<span id="page-8-0"></span>**Figure 9.** Electrochemical performance measurement: a) LSV of all electrocatalyst in absence of magnetic field; b) LSV of NF/Fe-NiCo in presence and absence of magnetic field. c) Possible OER reaction mechanism for MED catalysts. d) Tafel (80% iR compensated). e) Stability test.

| Catalyst [OER condition]<br>(NF/Fe is the substrate for<br>all catalyst) | ECSA cm2 | Specific<br>activity<br>mA/mg at 1.5V | Current<br>density/GSA<br>mA/cm2 at 1.5V | Current<br>density/ECSA<br>mA/cm2 at 1.5V | Tafel slope<br>mV/dec | Over potential (mV)<br>at 100 mA/cm2 |
|--------------------------------------------------------------------------|----------|---------------------------------------|------------------------------------------|-------------------------------------------|-----------------------|--------------------------------------|
| Ni–MED [OER-0]                                                           | 114.65   | 5.815                                 | 43.07                                    | 0.375                                     | 65                    | 318.5                                |
| Co–MED [OER-0]                                                           | 190.57   | 2.749                                 | 32.76                                    | 0.171                                     | 83                    | 337.2 at 91.41 mA<br>cm−2            |
| NiCo–MED [OER-0]                                                         | 264.5    | 5.567                                 | 83.51                                    | 0.315                                     | 61                    | 273.26                               |
| NiCo–MED [OER-H]                                                         | 315.1    | 6.898                                 | 104.85@1.492V                            | 0.332                                     | 56                    | 262.73                               |
| NiCo–no MED [OER-0]                                                      | 138.3    | 5.643                                 | 61.51                                    | 0.445                                     | 66                    | 305.39                               |
| NiCo–no MED [OER-H]                                                      | 168.85   | 7.073                                 | 76.39                                    | 0.452                                     | 59                    | 286.96                               |

that the transformation of Co(OH)2 to CoOOH is more compared to Ni(OH)2 to NiOOH transformation in Figure 9b. At lower overpotential, the current density/GSA of NF/Fe-NiCo-MED, [OER-0] is 2 to 3 times greater than NF/Fe-Ni-MED or NF/Fe-Co-MED, which confirms that NF/Fe-NiCo is the best among all the MED electrocatalyst. The enhancement in the current density (at1.5 V versus RHE) from NiCo-no MED, [OER-H] to NiCo-MED, [OER-0] is 9.32%, which can be further increased 37.25% for NiCo-MED, [OER-H]. Later, on further studying the OER of NiCo-MED catalyst under magnetic field we see further increment in ECSA as well as activity at lower over potential and Tafel slope (Table 4). It is also important to note that the specific activity of MED catalysts is lower compared to their non-MED counterparts. This may be attributed to the increased thickness of the MED catalyst layer, which enhances mass but does not significantly contribute to surface-level catalytic activity.

To the best of our knowledge NF/Fe-NiCo-MED outperforms benchmark NiCo-based layered double hydroxide (LDH) catalysts (Table S4) and even better than any multimetallic OER electrocatalyst that has been reported that uses an external magnetic field in alkaline OER (Table S3). Based on the adsorbate evolution mechanism (AEM), a possible catalytic cycle of OER using MED catalysts is represented in Figure 9c where M\* is the active site of the catalyst.[\[10\]](#page-11-0) The proposed mechanism is intended as a hypothesis-generating model rather than a definitive explanation. It is supported by LSV data indicating redox transitions of Ni and Co species, consistent with known AEM pathway intermediates. The formation of NiOOH and CoOOH suggests active catalytic states relevant to OER. Additionally, the observed Tafel slope (∼60 mV/dec) suggests that the rate-determining step occurs after the formation of surface-bound intermediates (e.g., MOH and MO,

where M is the active metal site), which is consistent with an AEM-based mechanism(Figure [9c\)](#page-8-0).[\[47\]](#page-11-0) One of reasons for the magnetic enhancement of OER is based on the effect of Lorentz force that creates a convective flow near the electrode surface which leads to rapid O2 evolution using MED catalyst. However, we see that the overpotential here was reduced by different magnitudes for different catalyst (Table [4\)](#page-8-0) with respect to NiCo-no MED, [OER-0] hence we note that Lorentz force is not the only governing property that causes changes in OER.[\[48,4\]](#page-11-0) The local magnetization of the active site of the catalyst and spin modulation mechanism play an important role in this aspect.[\[9,49\]](#page-11-0) Although NF/Fe-Co-MED electrocatalyst showed the highest magnetic remanence (14.76 emu/g) and highest saturation magnetization (95.08 emu/g), its high charge transfer resistance (27.34 Ω) (Table [3\)](#page-7-0) leads to lower OER activity. This observation is also justified further by the Tafel plot as shown in Figure 9d.[\[50,51\]](#page-11-0) The chronoamperometric stability test was performed at a potential 1.62 V (versus RHE) for the best performing catalyst, NF/Fe-NiCo, both with and without MED treatment. The NF/Fe-NiCo-MED catalyst exhibited excellent stability for up to 72 h with no significant loss in current density. In contrast, the NF/Fe-NiCo catalyst without MED treatment showed a gradual decrease in performance, with a maximum current density loss of approximately 8% after 24 h (Figure [9e\)](#page-8-0). As noted earlier, the higher coercive field of NF/Fe-NiCo-MED will facilitate sustained magnetic field to promote OER activity.

# **3. Conclusion**

This study explores rational design principles and implementable strategies for magnetic field-assisted synthesis to improve alkaline OER performance. We demonstrate that adding a magnetic field during electrodeposition of the catalysts results in performance improvements comparable to those obtained with externally applied magnetic fields during water electrolysis. A rational design strategy has been proposed, leveraging the complementary properties of Ni and Co: Ni provides high intrinsic OER activity, whereas Co imparts strong magnetic influence, enabling spin-polarized reaction pathways. In the co-deposited MED catalyst, NF/Fe-NiCo, cobalt acts as an in situ atomic magnet, enhancing the magnetic domain structure and promoting triplet O2 formation at the Ni active sites. Compared to catalysts prepared without a magnetic field, MED catalysts exhibit intrinsic remanence, higher saturation magnetization, and an increased electrochemical active surface area (ECSA), collectively leading to superior catalytic activity and stability. The NF/Fe-NiCo-MED catalyst achieves a low overpotential of 273.26 mV at 100 mA cm<sup>2</sup> and maintains stability over 72 h, outperforming benchmark NiCo-based systems and multimetallic catalysts operated under external magnetic fields. These findings highlight the potential for broader applicability of MED catalysts across a range of electrochemical processes.

## **4. Catalyst Preparation**

#### **4.1. Pretreatment of Nickel Foam (NF)**

Nickle foam (NF) of area 1 cm<sup>2</sup> (h = 1 cm, l = 0.5 cm, A = 2hl) was used to prepare the catalyst support for all the samples synthesized.[\[21\]](#page-11-0) The NF was de-greased with acetone via sonication for 5 min to remove any organic contaminants. Following that, the NF was soaked in 3 M HCl for 5 min followed by sonication for 1 min to remove the oxide layer that may have formed on the Ni surface due to storage. After this, the NF was washed with DI water and sonicated in DI water for 5 min to eliminate lingering acid. Finally, it was sonicated in ethanol for the same amount of time.

#### **4.2. Preparation of Iron-Modified NF by Galvanostatic Replacement Method**

From the electrochemical series, it is evident that there is an appreciable difference in electrochemical potential between the Fe3+/Fe0 (E° = −0.04 V) and Ni2+/Ni0 (E° = −0.26 V). This gives rise to a galvanic exchange reaction at the surface of NF.[\[24,52\]](#page-11-0)

$$3Ni + 2Fe^{3+} \rightarrow 3Ni^{2+} + 2Fe$$
 (6)

Hence, the Fe-displaced Ni-foam (NF/Fe) catalyst substrate was prepared by immersing the dry NF in 50 mM FeCl3 in ethanol for 1 h. The substrate was then rinsed thoroughly with water and dried in a vacuum. The resulting Fe-modified Ni-foam (NF/Fe) contains 6.5 to 7 wt% Fe as obtained from SEM-EDS analysis. It was observed that more than this percentage makes the NF slightly brittle.

#### **4.3. Electrodeposition of Ni and Co on NF/Fe**

Figure [10](#page-10-0) illustrates the synthesis of electrocatalysts in the presence of constant external magnetic field. The chronoamperometry technique was used at −1.54 V versus Ag/AgCl in two consecutive steps (10 min each step) with 5 min waiting time in between the steps to electrodeposit Ni on NF/Fe from 40 mM NiCl2 + 120 mM (NH4)2SO4; Co on NF/Fe from 40 mM CoCl2 + 120 mM (NH4)2SO4; and co-deposition of Ni and Co on NF/Fe from 1:1 molar ratio of 40 mM Ni2<sup>+</sup> and 40 mM Co<sup>2</sup><sup>+</sup> precursor salts in 120 mM ammonium sulphate solution (pH 4.3).[\[53\]](#page-11-0) During electrodeposition, a blank (with precursor salts) chronoamperometry data was recorded for the same time interval to subtract the current contribution from the competitive hydrogen evolution reaction (HER). The resulting electrocatalysts, such as NiCo-based electrocatalysts supported by Fe-modified nickel foam will be referred to as NF/Fe-NiCo. Two sets of electrocatalysts (EC) were electrodeposited (ED): one set in the presence a constant external magnetic field of 0.6T during electrodeposition and another set in the absence of external magnetic field following the same experimental parameters, such as temperature, deposition potential, deposition time duration, and as

<span id="page-10-0"></span>**Figure 10.** Schematic illustration of MED electrocatalyst synthesis.

mentioned earlier, will be denoted as EC-MED and EC–no MED respectively. After electrodeposition, the catalysts were washed thoroughly with DI water and dried overnight in a vacuum desiccator. The amount of metal electrodeposited in both sets was calculated by taking the weight difference before and after electrodeposition.

# **5. Electrochemical Measurement**

To activate the catalyst surface, initially, 50 cycles of cyclic voltammetry (CV) were performed in 1 M KOH at a scan rate of 10 mV/s for each of the catalysts. OER was performed at oxidative scan (linear sweep voltammetry) in the potential range 0 to 1 V versus Hg/HgO/1 M KOH. LSV with a very slow scan rate 0.1 mV/s was executed to plot overpotential (η) versus log (j) (current density mA/cm2 ) to calculate the Tafel slope. The measured current–voltage data spans a range beginning with the OER onset potential., i.e., from 0.5 to 0.85 V versus Hg/HgO. EIS was utilized to analyze the electrode cell setup's impedance (resistance and capacitance) behavior by providing an AC voltage of 0.55 V against Hg/HgO (1.47 V versus RHE) which is beyond OER's onset potential, i.e., catalytic turnover regions where appreciable activity was observed for all the electrocatalyst within an optimized frequency range of 10,000 Hz–0.05 Hz. The Nyquist plot obtained from the impedance data is then simulated using the NOVA software to fit the Randles circuit. The OER onset for NF and NF-Fe catalysts occurs at higher potentials (above 1.5 V, as shown in Figure [9a\)](#page-8-0), these materials exhibit poor OER performance—characterized by higher overpotentials and lower current densities. Due to their limited catalytic activity and relevance to practical applications, we did not include EIS measurements and other OER characterization for these specific samples. For ECSA, cyclic voltammetry was performed in 1 M KOH at several scan speeds (20, 50, 100, 150, 200, and 250 mV/s) in the potential range near the OCP value of 0 V to 0.12 V versus Hg/HgO (Figure S4). The obtained value of double-layer capacitance (Cdl) can be correlated to the ECSA by the following Equation (7).

$$ECSA = \frac{C_{dl}}{C_{s}} \tag{7}$$

A specific capacitance (Cs) value of 40 μF cm2 was assumed for all samples to estimate ECSA. While this is a commonly used approximation, for Ni/Co oxyhydroxide systems, it may vary depending on surface composition and morphology. As a result, the absolute ECSA values carry some uncertainty. However, since all catalysts were synthesized on the same NF/Fe substrate and ECSA was measured under identical electrochemical conditions, the comparative trends are meaningful and useful to estimate the relative performance of different electrocatalysts.[\[30\]](#page-11-0) Chronoamperometry was used to test the stability of the prepared catalyst with a set potential 1.62 V versus RHE). The stability test was run for 72 h.

## *Acknowledgments*

The authors are grateful to the Department of Science and Technology (DST), Ministry of Science and Technology, Government of India, for their financial assistance for this project (grant no: DST/CHE/2021478). They are also thankful to the Advance Centre for Materials Science, Centre for Nanoscience, and Post Graduate Research Laboratory, IIT Kanpur. They would like to

<span id="page-11-0"></span>express their gratitude to Mr. Anuj Awasthi for standardizing the magnetic setup. They would especially like to thank Mr. Mahendra Nishad and Mr. Dhirendra Kumar, for their assistance in designing and fabricating electrochemical cells as well as their continuous support to accomplish the research project.

# *Conflict of Interests*

The authors declare no conflict of interest.

## *Data Availability Statement*

Research data are not shared.

**Keywords:** Alkaline oxygen evolution reaction (OER) • Magnetoelectrocatalyst • Magnetoelectrodeposition (MED) • Spin polarization • Transition metal electrocatalysts

- [1] A. A. Krishnan, S. Harikumar, M. A. Aneesh Kumar, R. B. Nair, S. Kurian, M. Ameen Sha, P. S. Arun, Catal. Sci. Technol. **2024**, 14, 6155– 6175.
- [2] Y. Sun, H. Lv, H. Yao, Y. Gao, C. Zhang, Carbon Ener. **2024**, 6, e575.
- [3] S. Ma, Q. Fu, J. Han, T. Yao, X. Wang, Z. Zhang, P. Xu, B. Song, Adv. Funct. Mater. **2024**, 34, 2316544.
- [4] Y. Zhang, P. Guo, S. Li, J. Sun, W. Wang, B. Song, X. Yang, X. Wang, Z. Jiang, G. Wu, P. Xu, J. Mater. Chem. A Mater. **2022**, 10, 1760–1767.
- [5] F. A. Garcés-Pineda, M. Blasco-Ahicart, D. Nieto-Castro, N. López, J. R. Galán-Mascarós, Nat. Ener. **2019**, 4, 519–525.
- [6] J. T. Mefford, A. R. Akbashev, M. Kang, C. L. Bentley, W. E. Gent, H. D. Deng, D. H. Alsem, Y. S. Yu, N. J. Salmon, D. A. Shapiro, P. R. Unwin, W. C. Chueh, Nature **2021**, 593, 67–73.
- [7] T. Wu, X. Ren, Y. Sun, S. Sun, G. Xian, G. G. Scherer, A. C. Fisher, D. Mandler, J. W. Ager, A. Grimaud, J. Wang, C. Shen, H. Yang, J. Gracia, H. J. Gao, Z. J. Xu, Nat. Commun. **2021**, 12, 3634.
- [8] X. Ren, T. Wu, Y. Sun, Y. Li, G. Xian, X. Liu, C. Shen, J. Gracia, H. J. Gao, H. Yang, Z. J. Xu, Nat. Commun. **2021**, 12, 2608.
- [9] Z. Fang, W. Zhao, T. Shen, D. Qiu, Y. Lv, X. Hou, Y. Hou, Prec. Chem. **2023**, 1, 395–417.
- [10] D. Szalay, A. Radford, Y. Li, S. C. E. Tsang, Small **2025**, 2500001, [https://](https://doi.org/10.1002/smll.202500001) [doi.org/10.1002/smll.202500001.](https://doi.org/10.1002/smll.202500001)
- [11] J. M. D. Coey, Magnetism and Magnetic Materials, Cambridge University Press, England, **2010**, pp. 547–549.
- [12] L. Elias, P. Cao, A. C. Hegde, RSC Adv. **2016**, 6, 111358–111365.
- [13] A. Ispas, H. Matsushima, W. Plieth, A. Bund, Electrochim. Acta **2007**, 52, 2785–2795.
- [14] J. Saha, R. Ball, C. Subramaniam, ACS Sustain. Chem. Eng. **2021**, 9, 7792– 7802.
- [15] E. A. A. Aboelazm, G. A. M. Ali, H. Algarni, H. Yin, Y. L. Zhong, K. F. Chong, J. Phys. Chem. C **2018**, 122, 12200–12206.
- [16] H. Ooka, J. Huang, K. S. Exner, Front. Ener. Res. **2021**, 9, [https://doi.org/](https://doi.org/10.3389/fenrg.2021.654460) [10.3389/fenrg.2021.654460.](https://doi.org/10.3389/fenrg.2021.654460)
- [17] W. T. Hong, M. Risch, K. A. Stoerzinger, A. Grimaud, J. Suntivich, Y. Shao-Horn, Ener. Environ. Sci. **2015**, 8, 1404–1427.
- [18] S. Bhattacharjee, U. V. Waghmare, S. C. Lee, Sci. Rep. **2016**, 6, 35916.
- [19] S. Vijayan, R. Narasimman, K. Prabhakaran, Mater. Lett. **2016**, 181, 268– 271.
- [20] A. Peugeot, C. E. Creissen, M. W. Schreiber, M. Fontecave, ChemElectroChem **2022**, 9, e202200148.
- [21] W. Zheng, M. Liu, L. Y. S. Lee, ACS Ener. Lett. **2020**, 5, 3260–3264.
- [22] C. Zhang, Y. Bai, Y. Zhang, C. Li, S. Zhou, Results Phys **2019**, 14, 102522.

- [23] S. Anantharaj, S. Kundu, S. Noda, Nano Ener. **2021**, 80, 105514.
- [24] M. P. Browne, J. M. Vasconcelos, J. Coelho, M. O'Brien, A. A. Rovetta, E. K. Mccarthy, H. Nolan, G. S. Duesberg, V. Nicolosi, P. E. Colavita, M. E. G. Lyons, Sustain. Ener. Fuels **2017**, 1, 207–216.
- [25] M. K. Bates, Q. Jia, H. Doan, W. Liang, S. Mukerjee, ACS Catal. **2016**, 6, 155–161.
- [26] M. W. Louie, A. T. Bell, J. Am. Chem. Soc. **2013**, 135, 12329–12337.
- [27] Z. Zhao, P. Schlexer Lamoureux, A. Kulkarni, M. Bajdich, ChemCatChem **2019**, 11, 3423–3431.
- [28] M. S. Burke, M. G. Kast, L. Trotochaud, A. M. Smith, S. W. Boettcher, J. Am. Chem. Soc. **2015**, 137, 3638–3648.
- [29] S. Zou, M. S. Burke, M. G. Kast, J. Fan, N. Danilovic, S. W. Boettcher, Chem. Mater. **2015**, 27, 8011–8020.
- [30] S. Jiang, F. Chen, L. Zhu, Z. Yang, Y. Lin, Q. Xu, Y. Wang, ACS Appl. Mater. Interf. **2022**, 14, 10227–10236.
- [31] E. K. Hamal, M. C. Toroker, ChemCatChem **2020**, 12, 2801–2806.
- [32] Y. Ma, T. Wang, X. Sun, Y. Yao, H. Chen, G. Wu, C. Zhang, Y. Qin, ACS Appl. Mater. Interf. **2023**, 15, 7978–7986.
- [33] J. E. Huheey, E. A. Keiter, R. L. Keiter, O. K. Medhi, Inorganic Chemistry : Principles of Structure and Reactivity, Dorlingkindersley (India) Pvt. Ltd., New Delhi, 2006, p. 489.
- [34] R. Subbaraman, D. Tripkovic, K. C. Chang, D. Strmcnik, A. P. Paulikas, P. Hirunsit, M. Chan, J. Greeley, V. Stamenkovic, N. M. Markovic, Nat. Mater. **2012**, 11, 550–557.
- [35] K. Kishor, S. Saha, S. Sivakumar, R. G. S. Pala, ChemElectroChem **2016**, 3, 1899–1907.
- [36] M. Cheng, H. Fan, Y. Song, Y. Cui, R. Wang, Dalton Trans. **2017**, 46, 9201– 9209.
- [37] J. F. Marco, J. R. Gancedo, M. Gracia, J. L. Gautier, E. Ríos, F. J. Berry, J. Solid State Chem. **2000**, 153, 74–81.
- [38] Q. Lu, ACS Nano **2024**, 18, 13973–13982.
- [39] C. Alex, S. C. Sarma, S. C. Peter, N. S. John, ACS Appl. Ener. Mater. **2020**, 3, 5439–5447.
- [40] D. Jiles, Introduction to Magnetism and Magnetic Materials, CRC Press, Boca Raton **2016**, pp. 85–91.
- [41] S. S. Jeon, P. W. Kang, M. Klingenhof, H. Lee, F. Dionigi, P. Strasser, ACS Catal. **2023**, 13, 1186–1196.
- [42] S. Sasmal, S. Roy, P. K. Gupta, K. Ramkumar, P. Biswas, B. Ghorui, S. K. Saju, P. M. Ajayan, S. Valiyaveettil, R. G. S. Pala, S. Sivakumar, Ener. Technol. **2025**, 2400531, [https://doi.org/10.1002/ente.202400531.](https://doi.org/10.1002/ente.202400531)
- [43] M. E. Kreider, H. Yu, L. Osmieri, M. R. Parimuha, K. S. Reeves, D. H. Marin, R. T. Hannagan, E. K. Volk, T. F. Jaramillo, J. L. Young, P. Zelenay, S. M. Alia, ACS Catal. **2024**, 14, 10806–10819.
- [44] M. S. Burke, S. Zou, L. J. Enman, J. E. Kellon, C. A. Gabor, E. Pledger, S. W. Boettcher, J. Phys. Chem. Lett. **2015**, 6, 3737–3742.
- [45] M. S. Burke, L. J. Enman, A. S. Batchellor, S. Zou, S. W. Boettcher, Chem. Mater. **2015**, 27, 7549–7558.
- [46] F. Dionigi, J. Zhu, Z. Zeng, T. Merzdorf, H. Sarodnik, M. Gliech, L. Pan, W. X. Li, J. Greeley, P. Strasser, Angew. Chem.–Int. Ed. Engl. **2021**, 60, 14446– 14457.
- [47] T. Shinagawa, A. T. Garcia-Esparza, K. Takanabe, Sci. Rep. **2015**, 5, 13801.
- [48] K. Wang, Q. Yang, H. Zhang, M. Zhang, H. Jiang, C. Zheng, J. Li, J. Mater. Chem. A Mater. **2023**, 11, 7802–7832.
- [49] Q. Huang, H. Sheng, Chem.–A Eur. J. **2024**, 30, e202400352.
- [50] W. Zheng, ACS Ener. Lett. **2023**, 8, 1952–1958.
- [51] S. Anantharaj, S. Noda, J Mater. Chem. A Mater. **2022**, 10, 9348–9354.
- [52] D. Sengupta, S. M. S. Privitera, R. G. Milazzo, C. Bongiorno, S. Scalese, S. Lombardo, RSC Adv. **2020**, 10, 25426–25434.
- [53] Z. Yan, H. Sun, X. Chen, H. Liu, Y. Zhao, H. Li, W. Xie, F. Cheng, J. Chen, Nat. Commun. **2018**, 9, 2373.

Manuscript received: March 23, 2025 Revised manuscript received: July 5, 2025 Accepted manuscript online: July 6, 2025 Version of record online: August 6, 2025