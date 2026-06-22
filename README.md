# huckleberry_script.py

This script executes an informational audit comparing classical physical formulations to a unified geometric model with no free parameters. The audit evaluates both structures across three computational metrics:

1. Informational content (bits): Compares the description length by measuring the bit-depth of empirical primitives under a Minimum Description Length (MDL) criterion.
2. Algorithmic execution cost (FLOPs): Measures the weighted mathematical operations required to compute the dynamic state, reflecting the raw computational effort of the equations.
3. Cyclomatic complexity (branching nodes): Uses a native AST parser to calculate the cyclomatic complexity (CC) and measure the topological continuity of the logic flow.

The source code maintains algebraic-computational isomorphism in order to prevent notation artifacts from distorting the intrinsic complexity of either framework.

## Expected output

```python
===============================================================================
HUCKLEBERRY SCRIPT
Minimal logical complexity and algorithmic information audit
===============================================================================

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
EPISTEMOLOGICAL NOTE
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Under the framework of Algorithmic Information Theory (AIT) and the Minimum Description
Length (MDL) principle, the quality of a theory is evaluated by: L(model) + L(data|model).
Because both the classical (3PN) and geometric models evaluated here yield numerically identical
outputs across all evaluated scenarios (Discrepancy = 0.000000), the data-error term L(data|model)
cancels out. The comparison therefore reduces to L(model): the intrinsic algorithmic description
length. This audit evaluates structural compression under the assumption of numerical
equivalence within the benchmark.

1. AXIOMATIC COMPRESSION: The geometric model reduces the informational bit-depth by eliminating G
   and k_e as independent empirical primitives, deriving them from the dimensionless invariant alpha.
2. ONTOLOGICAL CONTINUITY & BOUNDARY CONDITIONS: The geometric model resolves the singularity
   branchlessly (CC=1) using continuous mathematical bounds (F_max) as natural structural limits.
   The classical model achieves CC=1 in Test B only by allowing unphysical mathematical infinities.
3. COMPUTATIONAL EFFICIENCY (Weighted FLOPs): Approximates typical IEEE 754 FPU clock
   cycle latencies (Add/Mul=1, Div=4, Sqrt=8, Pow=10) to evaluate true execution cost.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
NUMERICAL VERIFICATION
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TEST A: HEURISTIC FRAGMENTATION
Implication: To match the float64 precision of the unified geometric root, the classical model
is forced to compute a costly 3rd-order post-Newtonian (3PN) Taylor expansion. At the mesoscopic gap,
uncertainty forces a superposition. The geometric model unifies natively.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Interaction                  Classical formula                                                             Classical value (m/s**2)      Geometric formula                                               Geometric value (m/s**2)      Discrepancy (ppm)      
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Electron-Proton              F_e = k_e*|q_1*q_2| / r**2                                                    9.04422332410169e+22          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      9.04422332410169e+22          0.000000               
Proton-Earth                 F_g = F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3) [3PN]                         9.79845418864094e+00          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      9.79845418864094e+00          0.000000               
Sub-mesoscopic (< mz)        F_m = [F_N * 3PN] + [k_e*|q_1*q_2| / r**2]                                    2.31375185461968e-06          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      2.31375185461968e-06          0.000000               
Super-mesoscopic (> mz)      F_m = [F_N * 3PN] + [k_e*|q_1*q_2| / r**2]                                    6.90501002321038e-07          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      6.90501002321038e-07          0.000000               
1 kg-Earth                   F_g = F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3) [3PN]                         9.79845111611091e+00          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      9.79845111611091e+00          0.000000               
Sun-Earth                    F_g = F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3) [3PN]                         5.93033394901687e-03          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      5.93033394901686e-03          0.000000               
Sun-Mercury                  F_g = F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3) [3PN]                         3.95760817722685e-02          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      3.95760817722684e-02          0.000000               
PSR J0737-3039               F_g = F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3) [3PN]                         2.45778667822101e+02          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      2.45778667822101e+02          0.000000               
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TEST B: ONTOLOGICAL SUPERPOSITION
Implication: If physical reality is governed by the superposition of independent fundamental forces,
ontological consistency mandates their simultaneous evaluation across all scales. This test shows
the hidden algorithmic cost of manually superposing forces as separate classical entities.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Interaction                  Classical formula                                                             Classical value (m/s**2)      Geometric formula                                               Geometric value (m/s**2)      Discrepancy (ppm)      
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Electron-Proton              F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      9.04422332410169e+22          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      9.04422332410169e+22          0.000000               
Proton-Earth                 F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      9.79845418864094e+00          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      9.79845418864094e+00          0.000000               
Sub-mesoscopic (< mz)        F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      2.31375185461968e-06          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      2.31375185461968e-06          0.000000               
Super-mesoscopic (> mz)      F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      6.90501002321038e-07          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      6.90501002321038e-07          0.000000               
1 kg-Earth                   F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      9.79845111611091e+00          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      9.79845111611091e+00          0.000000               
Sun-Earth                    F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      5.93033394901687e-03          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      5.93033394901686e-03          0.000000               
Sun-Mercury                  F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      3.95760817722685e-02          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      3.95760817722684e-02          0.000000               
PSR J0737-3039               F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]      2.45778667822101e+02          F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)      2.45778667822101e+02          0.000000               
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
COMPUTATIONAL METRICS
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                               AUDIT A (heuristic)                                        AUDIT B (ontological)                                      
Metric                                                         Classical      Geometric      Compression ratio            Classical      Geometric      Compression ratio            
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. INFORMATIONAL CONTENT (precision bit-depth)                 48.11          32.63          1.47x                        48.11          32.63          1.47x                        
2. ALGORITHMIC EXECUTION COST (weighted FLOPs)                 75             57             1.32x                        73             57             1.28x                        
3. CYCLOMATIC COMPLEXITY (AST static decision nodes) [CC]      3              1              3.00x                        1              1              1.00x                        
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

# GEOMETRIC UNIFICATION OF PHYSICAL INTERACTIONS

Albert Roca  
albert.roca.mz@gmail.com  

v53 · 21 / 6 / 2026

DOI: https://doi.org/10.5281/zenodo.17847770

## Abstract

This work proposes a background-independent geometric framework where gravitation, electrostatics, quantum synchronization, and subatomic confinement emerge as complementary asymptotic regimes of a single discrete three-dimensional spatial metric. The fundamental resolution limit of this causal graph is defined by the geometric pixel ℓ = 2 · l_P. The framework removes the necessity of treating fundamental interactions as independent forces, replacing them with a unified intrinsic acceleration (a_i) governed by the finite causal resolution of space. This underlying metric response dictates two fundamental geometric scaling limits: a volumetric regime scaling as m^(1/3) corresponding to gravitation, and a structural surface regime scaling as m^(-5/3) corresponding to electrostatics. The continuous transition between these regimes is governed by the mesoscopic dynamic stability scale m_φ ≈ 4.157 × 10^(-9) kg, which represents the unique minimum of geometric coherence cost. The physical state of any localized topological defect is quantified by its geometric intensity (Ψ), a dimensionless variable measuring its effective structural occupancy within the lattice. The complete interaction dynamics are governed by a single unified equation of intrinsic acceleration, which yields the macroscopic gravitational limit, the Coulomb limit, and the Schwarzschild saturation limit as asymptotic extremes of the same continuous geometric curve. Ultimately, the model shows that independent physical forces are merely emergent properties of a single geometric topology. The framework reframes the fundamental mass of elementary fermions as the deterministic topological yield strength (Ψ_max) of this discrete spatial metric, reducing the origin of matter to an explicit boundary condition of geometric saturation. Furthermore, the framework derives the fundamental electron mass from the macroscopic radius of the universe, providing a geometric boundary for the inflationary horizon and establishing mass as a dynamic relational state that scales inversely with cosmological expansion. The Planck length is derived not as a primitive background constant, but as a deterministically emergent limit of the discrete spatial metric resolution. The model reveals that the structural mismatch between the volumetric and surface scaling exponents generates a persistent topological shear pressure, frame-shifting cosmological expansion from an exogenous dark energy phenomenon into the inevitable mechanical relaxation rate of the discrete spatial metric itself. This derivation culminates in a closed-form geometric expression for the gravitational constant (G), establishing it as a deterministically emergent relational property of the global cosmological volume and the fundamental particle boundary limit. The mutual dependence between the fundamental mass and the cosmological radius formalizes Mach's principle, proving that absolute dimensionful scale is not a pre-existing background property, but a dynamic and emergent relational state. An algorithmic information-theoretic audit evaluates the structural complexity and computational execution cost of the framework against classical post-Newtonian approximations, validating the model's predictive equivalence under a minimum description length (MDL) criterion with zero residual divergence.

## Parameters

G = 6.67430(15) × 10^(-11) m^3 · kg^(-1) · s^(-2) (gravitational constant)

k_e = 8.9875517923 × 10^9 N · m^2 · C^(-2) (electrostatic constant)

e = 1.602176634 × 10^(-19) C (elementary charge)

α = 7.2973525643(11) × 10^(-3) (fine-structure constant)

ħ = 1.054571817 × 10^(-34) J · s (reduced Planck constant)

c = 299792458 m / s (speed of light)

m_P = 2.176434(24) × 10^(-8) kg (Planck mass)

l_P = 1.616255(18) × 10^(-35) m (Planck length)

ƛ = 0.2103089 × 10^(-15) m (reduced Compton wavelength)

m_p = 1.67262192595 × 10^(-27) kg (proton mass)

m_e = 9.109 383 7139 × 10^(-31) kg (electron mass)

Source: CODATA internationally recommended 2022 values of the fundamental physical constants.  
http://physics.nist.gov/constants

## 1. Unified Model of Gravitation and Electrostatics

### 1.1. Formulation

The Unified Model of Gravitation and Electrostatics (Roca, 2025) proposes a single equation that reproduces the combined results of Newton's and Coulomb's laws:

F_u = (U / r^2) · ((m_1 · m_2 / z) + s)

Where:

U = α · ħ · c

U = 2.30707755 × 10^(-28) kg · m^3 · s^(-2)

z = α · m_P^2

z = 3.45665728 × 10^(-18) kg^2

s = n_1 · n_2

n = n_p - n_e

Where n_p is the number of protons and n_e is the number of electrons. This establishes s as a purely geometric integer.

The model can be alternatively formalized in terms of G:

F_u = G · (m_1 · m_2 + z · s) / r^2

The formulations written in terms of U and z represent the SI-normalized macroscopic projection of the interaction. A later geometric reformulation removes the explicit dependence on α and rewrites the primitive interaction directly in terms of the universal geometric prefactor ħ · c / m_P^2.

### 1.2. Dimensional coherence

Dimensional structure:

G = L^3 · M^(-1) · T^(-2)

U = L^3 · M^1 · T^(-2)

z = L^0 · M^2 · T^0

Validation:

U / z = (L^3 · M^1 · T^(-2)) / (M^2)

U / z = L^3 · M^(1 - 2) · T^(-2)

U / z = L^3 · M^(-1) · T^(-2) = G

### 1.3. Equilibrium mass: m_z

The Unified Model defines the equilibrium mass (m_z) as the transition point where the magnitudes of F_e and F_g become equal when s = 1.

m_z = √z

m_z = m_P · √α

m_z ≈ 1.85920878 × 10^(-9) kg

Gravitational term (F_g) generated by m_z:

F_g = G · m_z^2 / r^2

Since z = m_z^2 and G = U / z:

F_g = U / r^2

F_g = 2.307 × 10^(-28) / r^2 N · m^2

This magnitude is equivalent to the electrostatic interaction between two elementary charges:

F_e = k_e · e^2 / r^2

Therefore:

F_g = F_e = 2.307 × 10^(-28) / r^2 N · m^2

### 1.4. Law of acceleration symmetry

The unification of interactions reveals a perfect symmetry of inversion regarding the kinematic behavior of mass. By isolating the acceleration (a) imposed by a source object of mass (m) at a fixed distance (r), the dynamics are described by a single function dependent on the unified constant U.

The intrinsic acceleration is defined by the geometric regime of the source mass relative to the equilibrium mass (m_z):

a = (U / r^2) · Y

Where Y is the geometric scaling factor of the mass.

#### 1.4.1. Volumetric term

In the gravitational domain, the geometric influence scales linearly with mass. The interaction is dominated by the volumetric term:

Y = m / m_z^2

a_g = (U / r^2) · (m / m_z^2)

a_g = G · m / r^2

Since F = m · a:

F_g = m · (G · m / r^2)

F_g = G · m^2 / r^2

This recovers Newton's law.

#### 1.4.2. Surface term

In the electrostatic domain, the geometric influence scales with the inverse of the mass. The interaction is dominated by the surface term:

Y = 1 / m

a_e = (U / r^2) · (1 / m)

Since F = m · a:

F_e = m · ((U / r^2) · (1 / m))

F_e = U / r^2

This recovers Coulomb's law.

#### 1.4.3. Topological inversion

At the equilibrium point (m = m_z), both regimes converge:

m / m_z^2 = 1 / m

m^2 = m_z^2

a_g = a_e

This derivation shows that electric charge is not an independent physical entity, but the kinematic signature of mass when operating in the inverse scaling regime (1 / m).

### 1.5. Dimensional anchoring with fundamental constants

The characteristic mesoscopic stability scale, denoted as m_φ, is not an arbitrary free parameter adjusted to fit empirical observation. Instead, it anchors directly to the fundamental constants of the universe through a pure geometric scale factor.

The baseline scale for interaction equilibrium is established by the mass m_z, which marks the point where the classical gravitational and electrostatic forces between two elementary charges reach identical magnitudes. This equilibrium mass relates directly to the Planck mass m_P and the primitive structural action scale U:

m_z = m_P · √α

m_z = 1.85920878 × 10^(-9) kg

The unique minimum of the intrinsic acceleration function defines the mass of dynamic stability m_φ. This scale is displaced from the static equilibrium mass m_z by the geometric scaling factor δ, which represents the ratio between the spatial degrees of freedom involved in the volumetric and structural interaction regimes. The scaling factor δ is defined as:

δ = 5^(1/2)

Consequently, the characteristic mesoscopic scale m_φ is derived entirely from first principles without external parameterization:

m_φ = δ · m_z

m_φ = 5^(1/2) · m_z

m_φ = 4.15731777 × 10^(-9) kg

This dimensional anchoring shows that the mesoscopic stability domain is fundamentally constrained by the underlying coupling between the discrete metric structure and the macroscopic interaction constants.

### 1.6. Informational reduction of the electrogravitational sector

Within the contemporary SI system, several quantities historically treated as independent constants no longer carry independent empirical information. The quantities c, h, ħ and e are fixed by definition, while the electrostatic normalization satisfies:

k_e · e^2 = α · ħ · c

Consequently, the conventional electrogravitational sector is fully specified by two experimentally independent quantities:

{G, α}

The informational content associated with an experimentally determined primitive is defined through its relative uncertainty:

K_i = -log_2(δ_i)

where:

δ_i = σ_i / x_i

The total informational content of the description becomes:

K = Σ K_i

Using the CODATA 2022 recommended uncertainties:

δ_G = 2.2 × 10^-5

δ_α = 1.5 × 10^-10

the corresponding informational contents are:

K_G = -log_2(2.2 × 10^-5)

K_G = 15.47 bits

K_α = -log_2(1.5 × 10^-10)

K_α = 32.63 bits

The total informational content of the conventional electrogravitational description is therefore:

K_conv = K_G + K_α

K_conv = 48.10 bits

Within the geometric framework, the interaction scale is defined as:

U = α · ħ · c

while the equilibrium scale becomes:

z = α · m_P^2

The gravitational coupling is subsequently recovered through:

G = U / z

The quantity G therefore ceases to represent an experimentally independent primitive and becomes a derived geometric quantity.

The electrogravitational sector is consequently specified by a single experimentally independent invariant:

{α}

The informational content of the geometric description becomes:

K_geo = K_α

K_geo = 32.63 bits

The reduction in informational content is therefore:

ΔK = K_conv - K_geo

ΔK = 15.47 bits

The corresponding compression ratio is:

C = K_conv / K_geo

C = 1.47

while the relative reduction becomes:

R = 1 - K_geo / K_conv

R = 0.322

R = 32.2 %

The geometric formulation therefore reproduces the electrogravitational sector while requiring 32.2 % less experimentally independent information than the conventional description.

The reduction originates from the elimination of G as an independent primitive. Gravitation and electrostatics become different projections of the same underlying geometric structure, both generated from the single dimensionless invariant α.

## 2. Intrinsic acceleration

### 2.1. Superposition principle

While the volumetric and structural contributions become negligible in opposite asymptotic regimes, both remain simultaneously present at the mesoscopic scale.

Intrinsic acceleration (a_i) is therefore defined not as a transition between independent interactions, but as the geometric superposition of two complementary propagation modes.

For an object with mass m and structural topology |n|, the intrinsic acceleration is defined as:

a_i = a_g + a_e

Where:

a_g = (U / (z · r^2)) · m

a_e = (U / r^2) · (|n| / m)

Thus:

a_i = (U / r^2) · ((m / z) + (|n| / m))

The quantity a_i does not represent the free kinematic acceleration of an isolated object.

Instead, it describes the intrinsic geometric response capacity associated with the internal volumetric and structural configuration of the excitation.

The volumetric contribution scales proportionally with mass, while the structural contribution scales inversely with mass and depends on the existence of discrete topology through |n|.

For perfectly neutral objects:

|n| = 0

and therefore:

a_e = 0

which reduces the intrinsic acceleration to the purely volumetric regime:

a_i = a_g

The characteristic geometric radius r represents the effective internal propagation scale associated with the excitation itself.

### 2.2. Transition curve

The intrinsic acceleration curve reveals that inertial behavior becomes non-linear in the transition region between the volumetric and structural regimes.

For all objects:

a_i = a_g + a_e

The structural contribution depends on the existence of discrete topology through |n|.

For neutral objects:

|n| = 0

and therefore:

a_e = 0

which reduces the intrinsic acceleration to the purely volumetric regime:

a_i = a_g

For objects with |n| ≠ 0, both contributions coexist simultaneously.

For small masses, the structural contribution dominates and the curve follows the electrostatic asymptotic regime.

For large masses, the volumetric contribution dominates and the curve converges toward the gravitational regime.

The crucial geometric equilibrium appears at the scale m_z.

At this point, the volumetric and structural contributions acquire equal magnitude:

a_g = a_e

However, the minimum of the intrinsic acceleration curve does not occur at m_z.

Because the structural contribution decreases five times faster than the volumetric contribution increases, the minimum of the combined curve appears at a larger scale:

m_ϕ = √5 · m_z

At m_ϕ, the structural contribution satisfies:

a_e = (1 / 5) · a_g

The quantity m_ϕ therefore corresponds not to equal geometric contribution, but to the point of minimal total intrinsic acceleration generated by the convex superposition of both regimes.

The transition does not occur through the disappearance of one regime and the abrupt emergence of the other.

Both contributions coexist continuously across the entire geometric spectrum.

Consequently, the intrinsic acceleration curve does not form a discontinuous geometric vertex at m_z, but instead develops a smooth convex minimum generated by the superposition of both propagation modes.

The asymptotic scaling laws associated with the volumetric and structural regimes emerge subsequently from the geometric scaling properties of the interacting configurations.

### 2.3. Relational intrinsic acceleration

Intrinsic acceleration does not describe observable interaction in isolation, but the internal geometric response structure associated with an excitation.

Observable acceleration emerges only through the interaction between two objects separated by a distance d.

For two interacting objects, the relational acceleration is expressed as:

a_r = (U / d^2) · ((m_2 / z) + (s / m_1))

Where:

s = n_1 · n_2

The volumetric contribution scales with the mass of the external source m_2, while the structural contribution depends on the topological interaction between both excitations.

When:

s = 0

the structural contribution vanishes and the interaction reduces to the purely gravitational regime:

a_r = (U / d^2) · (m_2 / z)

When the structural contribution dominates over the volumetric contribution, the interaction converges toward the electrostatic regime.

The relational equation therefore describes the external projection of the intrinsic geometric structure encoded by a_i.

The quantities a_i and a_r do not represent independent mechanisms, but complementary levels of description.

The first characterizes the internal geometric balance of an excitation, while the second describes the observable interaction generated between two geometric configurations.

The characteristic radius r and the interaction distance d describe different geometric scales within the model.

The radius r corresponds to the effective internal propagation scale associated with the excitation itself, while d represents the relational separation between interacting objects.

The asymptotic scaling regimes derived later emerge when the interaction distance scales geometrically with the characteristic size of the interacting excitation.

Acceleration therefore emerges not from an external force acting independently between bodies, but from the local geometric compatibility between two structural projections of space.

## 3. Electric charge

### 3.1. Dimensional closure of interactions

Two physically independent interactions producing the same observable quantity must admit representation within a common dimensional basis.

Gravitational interaction is defined as:

F_g = G · (m_1 · m_2) / r^2

Dimensional structure:

G = L^3 · M^(-1) · T^(-2)

Electrostatic interaction is defined as:

F_e = k_e · (q_1 · q_2) / r^2

Dimensional structure:

k_e = L^3 · M · T^(-2) · Q^(-2)

Where Q denotes the Coulomb dimension.

Both interactions generate the same physical observable:

F_g = F_e = M · L · T^(-2)

Minimal dimensional closure requires that both interactions can be expressed within a common dimensional framework. If Q were a truly fundamental independent dimension, electrostatic interaction would require an additional primitive dimensional axis absent from gravitation. This would imply that the two interactions are not dimensionally closed under a shared geometric description.

To preserve dimensional closure, the charge dimension must therefore admit a mapping onto the existing mechanical basis:

Q^2 ~ M^2

Substituting this equivalence into the electrostatic constant yields:

k_e = L^3 · M · T^(-2) · Q^(-2)

k_e = L^3 · M · T^(-2) · M^(-2)

k_e = L^3 · M^(-1) · T^(-2)

Therefore, k_e and G share the same dimensional structure. The Coulomb ceases to be a necessary fundamental dimension.

Electric charge is thus reinterpreted not as an independent physical substance, but as a derived normalization convention arising from the historical separation between mechanical and electrostatic unit systems.

### 3.2. Ontological interpretation

The geometric framework removes the ontological necessity of dimensional electric charge as an independent physical substance. Electric polarity reduces to the dimensionless topological orientation |n|.

Consequently, Coulombs cease to represent fundamental physical units, and electric charge becomes a derived macroscopic normalization convention.

The theory establishes a single underlying geometric interaction operator:

ħ · c / r^2

Gravitation, electrostatic interaction, and structural confinement emerge as asymptotic scaling regimes of the same geometric substrate. The apparent distinction between gravitational and electric interaction arises only after projection into macroscopic SI normalization conventions.

Acceleration therefore does not emerge from the action of autonomous forces or fields, but from the geometric admissibility of motion within a constrained three-dimensional topology.

### 3.3. Geometric equivalence

The integration of the electrostatic term into the acceleration equation reveals the geometric nature of the parameter |n|.

From the electrostatic component of intrinsic acceleration:

a_e = (U / r^2) · (|n| / m)

If the electrostatic regime is interpreted as the projection of the maximum energy density of the metric (c^2) onto a linear topology, |n| can be expressed as:

|n| = (r_s · m · c^2) / (w · U)

Where r_s represents the structural or physical radius of the object.

Substituting this definition back into the acceleration equation:

a_e = (U / r^2) · (1 / m) · ((r_s · m · c^2) / (w · U))

a_e = (c^2 / w) · (r_s / r^2)

Mass cancels identically.

Unlike the gravitational regime, which scales volumetrically with m, the electrostatic regime scales through linear structural projection. The interaction magnitude is therefore determined by the projection of c^2 onto the topology of the object.

The parameter |n| is thus interpreted as a normalized geometric measure of structural radius. Charge quantization becomes the observational consequence of discrete geometric resolution.

The electrostatic regime is not generated by an independent charge substance, but by the geometric response of confined topology within a finite metric structure.

## 4. Geometric cost

### 4.1. Causal relationship

The transition between regimes reveals a fundamental asymmetry: if physical interactions depended solely on the fundamental properties of the objects (m and r), the equilibrium point (m_z) should coincide with the point of maximum system stability.

Mathematically, m_z represents the point where the magnitudes of F_e and F_g are equal, but this point does not coincide with the minimum value of the intrinsic acceleration curve (m_φ). Since both points represent the minimum value of their respective magnitudes, there must be a causal relationship between them. m_s provides the geometric structural bridge between m_z and m_φ.

The analysis of the discrepancy between m_z and the point of structural stability of the system requires a dimensionless correction term. As the magnitudes of m and r are already taken into account, this term is identified as a structural cost.

### 4.2. Topology in a three-dimensional space

Inertia is not an intrinsic property of an object, but the measure of the geometric constraint of three-dimensional space. Without this structural condition, an object would have no geometric basis to limit its acceleration under a given interaction. The factor w is a topological constant derived directly from the geometric properties of space.

In a three-dimensional universe (D = 3), any physical object is defined by the scaling relationship between its linear dimension, its surface area, and its volume. Assuming a constant structural density, since mass (m) corresponds to volume (V), the linear size (r) scales with m as:

r ~ m^(1 / 3)

However, the surface area (A) scales with the linear dimension as r^2. Expressing A in terms of m:

A ~ r^2 ~ (m^(1 / 3))^2 ~ m^(2 / 3)

The structural constant w is defined as the ratio between the surface scaling exponent (2 / 3) and the linear scaling exponent (1 / 3):

w = (2 / 3) / (1 / 3)

w = 2

Alternatively, w is expressed as the relationship between the volumetric dimension (D) and the surface dimension (D - 1):

w = (D - 1) / 1 = D - 1

w = 3 - 1 = 2

w = 2 is the dimensional rate of scaling between a surface (2D) and a line (1D) within a volume (3D).

The gravitational (a_g) and electrostatic (a_e) components of acceleration (a = F / m) are derived based on how they interact with m.

Gravitational component:

F_g ~ m^2 / r^2

F_g ~ m^2 · m^(-2 / 3)

a_g ~ (m^2 · m^(-2 / 3)) / m

a_g ~ m^(1 / 3)

Electrostatic component:

F_e ~ 1 / r^2

F_e ~ 1 / m^(2 / 3) ~ m^(-2 / 3)

a_e ~ m^(-2 / 3) / m

a_e ~ m^(-5 / 3)

The exponents 1 / 3 and -5 / 3 are, therefore, topological constants. w is not a numerical accident, but an unavoidable topological requirement of the three-dimensional nature of space. Any physical interaction can be described as an equilibrium between surface (m^(-2 / 3)) and volume (m^(1 / 3)).

The framework excludes the possibility of a universe with D ≠ 3. Postulating additional dimensions is mathematically incompatible with Newton's second law:

a = F / m

### 4.3. Structural term

The surface or structural contribution does not represent ordinary material surface area. The exponents emerge from the geometric relation between volumetric scaling and inverse-square propagation, but the structural regime corresponds physically to geometric tension generated by finite spatial confinement.

For a volumetric distribution:

m ~ r^3

Therefore:

r ~ m^(1 / 3)

The structural regime (a_s) scales through inverse-square geometric confinement combined with inverse volumetric capacity:

a_s ~ 1 / (m · r^2)

Substituting the volumetric relation yields:

a_s ~ 1 / (m · m^(2 / 3))

Therefore:

a_s ~ m^(-5 / 3)

The structural contribution therefore increases naturally as finite geometric deformation becomes confined within decreasing volumetric capacity. For large masses, geometric deformation is distributed volumetrically and the interaction converges to the bulk gravitational regime. For small masses, the same geometric deformation is confined within progressively smaller volumetric capacity, causing the structural regime to dominate. The structural term thus measures geometric resistance of the metric rather than literal material surface.

## 5. Geometry and dynamics

### 5.1. Geometric nature of mass

The underlying conceptual postulate of the model is that matter is not a substance or an assembly of independent particles residing in a passive medium, but a local configuration of space itself.

### 5.2. Scaling of geometric cost

Housing mass in space has a geometric or structural cost (C_s). Since the volumetric cost scales with m through the exponent 1 / 3 and the superficial cost scales with m through the exponent -2 / 3, the function becomes:

C_s ~ m^(1 / 3) + m^(-2 / 3)

### 5.3. Mass of optimal structural cost: m_s

The equilibrium mass m_z defines the scale at which the volumetric and structural contributions acquire equal magnitude:

a_g = a_e

However, this equilibrium point does not correspond to the minimum of the intrinsic acceleration curve.

Because the structural contribution decreases asymmetrically with respect to the volumetric contribution, the minimum geometric configuration is displaced from m_z by the structural constant:

w = 2

The structural mass m_s is therefore defined as:

m_s = w · m_z

m_s = 2 · m_z

m_s = 2 · √α · m_P

m_s ≈ 3.71841756 × 10^(-9) kg

The quantity m_s does not represent an independent physical mass, but the structural geometric component associated with the displacement between equilibrium and minimum intrinsic acceleration.

Together, m_z and m_s generate the characteristic mesoscopic scale m_ϕ through the geometric relation:

m_ϕ^2 = m_z^2 + m_s^2

which yields:

m_ϕ = √5 · m_z

The quantity m_ϕ therefore emerges as the resultant geometric scale generated by the superposition between the equilibrium contribution m_z and the structural displacement m_s.

The mesoscopic minimum is not generated directly at the equilibrium point itself, but through the geometric composition between volumetric balance and structural asymmetry.

The structural constant w consequently does not appear as an arbitrary parameter, but as the geometric factor governing the displacement between equilibrium and minimal intrinsic acceleration.

### 5.4. Scaling of intrinsic acceleration

Intrinsic acceleration represents the dynamic response of an object to the geometric cost of motion. It is defined from Newton's second law:

a_i = F_u / m

This relationship allows the transformation of structural exponents into acceleration exponents.

Intrinsic acceleration contains the components:

a_i = a_e + a_g

For the gravitational component (a_g), F depends on the product of masses (m · m = m^2) and the inverse geometry (1 / r^2):

F_g ~ m^2 / r^2

F_g ~ m^2 · m^(-2 / 3)

F_g ~ m^(4 / 3)

Gravitational acceleration (F_g / m):

a_g ~ m^(4 / 3) / m

a_g ~ m^(1 / 3)

For the electrostatic component (a_e), F depends on the factor s and the inverse geometry (1 / r^2):

F_e ~ 1 / r^2

F_e ~ m^(-2 / 3)

Electrostatic acceleration (F_e / m):

a_e ~ m^(-2 / 3) / m

a_e ~ m^(-5 / 3)

The total intrinsic acceleration function is given by the sum of the two dynamic terms:

a_i ~ m^(1 / 3) + m^(-5 / 3)

This allows defining the mass of minimum intrinsic acceleration: m_φ

#### 5.4.1. Inertial amplification of structural scaling

The geometric exponents governing the acceleration regimes do not emerge directly from the interaction laws themselves, but from the interaction laws combined with Newton's inertial relation:

F = m · a

Before the inertial transformation, the geometric force contributions scale as:

F_g ~ m^(4 / 3)

and:

F_e ~ m^(-2 / 3)

The gravitational exponent originates from the product of masses combined with inverse-square geometric dilution, while the structural exponent originates solely from inverse-square geometric confinement.

The transformation from force to acceleration introduces an additional inverse mass factor:

a = F / m

Applying this transformation yields:

a_g ~ m^(4 / 3 - 1)

a_g ~ m^(1 / 3)

and:

a_e ~ m^(-2 / 3 - 1)

a_e ~ m^(-5 / 3)

The structural exponent therefore undergoes a stronger inertial amplification than the volumetric exponent.

The displacement between m_z and m_φ originates from this asymmetry.

At the force level, the equilibrium condition:

F_g = F_e

defines the static crossover scale m_z.

At the acceleration level, the additional inertial weighting shifts the minimum of the combined response function away from m_z and generates the dynamic stability scale m_φ.

The factor:

|-5 / 3| / |1 / 3| = 5

therefore emerges as a direct consequence of the inertial transformation imposed by Newton's second law upon the underlying geometric force structure.

The dynamic stability scale m_φ consequently reflects not only geometric equilibrium, but the geometric response of that equilibrium under inertial propagation.

### 5.5. Mass of dynamic stability: m_φ

The equilibrium relationship between m_z and the mass of dynamic stability (m_φ) arises from the relationship between the geometric exponents corresponding to the electrostatic component (-5 / 3) and the gravitational component (1 / 3):

|-5 / 3| / |1 / 3| = 5

This relationship indicates the displacement factor of the dynamic stability point with respect to the equilibrium point (m_z). However, given that the intensity of the gravitational interaction does not scale linearly with mass, but with the product of masses (F ~ m^2), this scale factor must be applied over the quadratic basis of the interaction:

m_φ^2 = 5 · m_z^2

m_φ = √5 · m_z

m_φ ≈ 4.15731777 × 10^(-9) kg

This defines the scale factor δ:

δ = √5

m_φ = δ · m_z

m_φ = δ · √α · m_P

m_φ represents the point of maximum inertial stability, where the geometric cost of motion imposes the minimum total acceleration on the object.

The intrinsic acceleration function can be defined as the linear superposition:

a_i = A · m^(1 / 3) + B · m^(-5 / 3)

Where A and B are positive constants derived from U and z.

In the domain m > 0 and |n| ≠ 0, when m tends to 0, a_i tends to ∞, and when m tends to ∞, a_i tends to ∞. The function is convex, since the second derivative is positive.

A continuous and convex function that tends to ∞ at both ends of the domain must have, by mathematical necessity, one and only one minimum point (m_φ), where the first derivative cancels out.

#### 5.5.1. Functional derivation of the stability scale

The relationship:

m_φ = √5 · m_z

can be derived independently from the unified geometric response function.

The framework previously established the scale-dependent geometric response:

T_3(r) = r + r^(-5)

where the first term represents cooperative volumetric redistribution and the second term represents unresolved structural exposure.

The dynamic stability scale corresponds to the point at which the total geometric response reaches a minimum. This condition is obtained by differentiating the response function with respect to the normalized radial coordinate:

dT_3/dr = 1 - 5r^(-6)

Setting the derivative equal to zero:

1 - 5r^(-6) = 0

gives:

r^6 = 5

and therefore:

r_φ = 5^(1/6)

The framework relates mass and characteristic radius through volumetric scaling:

m ~ r^3

Consequently:

m_φ / m_z = (r_φ / r_z)^3

Using the normalized equilibrium condition:

r_z = 1

yields:

m_φ / m_z = (5^(1/6))^3

m_φ / m_z = 5^(1/2)

m_φ / m_z = √5

Therefore:

m_φ = √5 · m_z

This result reproduces the dynamic stability scale obtained from the acceleration formalism, but derives it directly from the extremum structure of the unified geometric response function.

The factor:

δ = √5

therefore emerges as a geometric invariant associated with the minimum of the unified response function. The characteristic mass m_φ represents the mass scale corresponding to the optimal balance between cooperative volumetric redistribution and unresolved structural exposure within the discrete metric.

The agreement between the acceleration-based derivation and the functional minimization of T_3(r) provides an independent consistency condition for the framework and supports the interpretation of m_φ as a fundamental scale of dynamic geometric stability.

#### 5.5.2. Static and dynamic equilibrium

The geometric framework reveals that the characteristic scales m_z and m_φ do not represent the same physical condition.

The equilibrium mass m_z is defined as the static geometric crossover point at which the magnitudes of the volumetric and structural interaction terms become equal (F_g = F_e). This scale therefore represents a purely structural equilibrium of the geometric interaction.

However, the point of minimum intrinsic acceleration does not occur at m_z, but at:

m_φ = √5 · m_z

This displacement emerges because physical propagation is governed not only by static interaction balance, but by the dynamic efficiency of geometric redistribution across the spatial metric.

The scale m_φ consequently represents a distinct physical condition: the point of optimal dynamic propagation stability.

At m_φ, the cooperative volumetric redistribution of radial attenuation reaches equilibrium with the amplified structural cost associated with unresolved geometric exposure. The system minimizes the total geometric coherence cost required for stable propagation through the discrete metric.

The distinction between m_z and m_φ therefore reflects the difference between static structural equilibrium and dynamic propagation equilibrium.

Within this interpretation:

* m_z defines the geometric crossover between volumetric and structural interaction magnitudes. 
* m_φ defines the point of maximal propagation efficiency and minimal intrinsic geometric cost. 
This distinction becomes increasingly important in the later informational interpretation of the framework, where coherent propagation, attenuation redistribution, and geometric uncertainty emerge as fundamentally dynamical phenomena rather than purely static geometric states.

#### 5.5.3. Ontological necessity of the mesoscopic minimum

The emergence of the mesoscopic minimum does not originate from the introduction of an additional phenomenological hypothesis, but from the unavoidable coexistence of the volumetric and structural acceleration regimes under three-dimensional geometric scaling.

The Newtonian contribution scales as:

a_g ~ m^(1 / 3)

while the structural contribution derived from inverse-square confinement scales as:

a_e ~ m^(-5 / 3)

These exponents emerge directly from:

F_g ~ m^2 / r^2

F_e ~ 1 / r^2

combined with the geometric volumetric relation:

r ~ m^(1 / 3)

under constant density scaling.

The observable acceleration of a physical configuration cannot exclude either contribution whenever both interaction regimes coexist physically.

The total acceleration therefore necessarily becomes:

a_i ~ m^(1 / 3) + m^(-5 / 3)

The resulting function is continuous, convex, and diverges asymptotically for both m → 0 and m → ∞. Consequently, the existence of a unique minimum is not an optional interpretation of the model, but a mathematical necessity of the combined interaction structure itself. 

The characteristic scale m_φ = √5 · m_z emerges as the unavoidable geometric consequence of the coexistence between volumetric propagation and inverse structural confinement within a three-dimensional metric. It emerges necessarily from the simultaneous validity of:

* Newtonian interaction.

* Coulomb interaction.

* Inverse-square propagation.

* Acceleration superposition.

* Volumetric geometric scaling.

If physically realizable systems satisfying these conditions failed experimentally to exhibit the predicted mesoscopic behavior, the inconsistency would not affect exclusively the present geometric interpretation. At least one of the underlying assumptions commonly regarded as universally valid would necessarily fail within the corresponding regime.

The mesoscopic minimum therefore does not constitute an auxiliary hypothesis added to the interaction laws, but a necessary structural consequence of their simultaneous geometric validity under three-dimensional scaling.

### 5.6. Origin of δ

The ratio between m_z and m_φ is √5. This factor is not arbitrary but arises from minimizing the intrinsic acceleration function. The point of minimum intrinsic acceleration (m_φ) is found by calculating the root of the derivative with respect to mass:

a_i = A · m^(1 / 3) + B · m^(-5 / 3)

d a_i / d m = (1 / 3) · A · m^(-2 / 3) - (5 / 3) · B · m^(-8 / 3) = 0

A · m^(-2 / 3) = 5 · B · m^(-8 / 3)

m^(-2 / 3) / m^(-8 / 3) = 5 · (B / A)

m^(6 / 3) = 5 · (B / A)

m^2 = 5 · (B / A)

m_φ = √5 · √(B / A)

The term √(B / A) represents the point where the magnitudes of the two force terms are equal (m_z).

Therefore:

m_φ = √5 · m_z

The factor √5 is a necessary consequence of the optimization between volumetric inertia and holographic surface tension.

### 5.7. Law of dimensional displacement

The displacement of the dynamic stability point (m_φ) with respect to the equilibrium point (m_z) is interpreted as a function of the dimensionality (D) of space.

The relationship between m_z and m_φ allows generalizing the displacement factor (δ) to any number of dimensions:

δ = √(2 · D - 1)

In a one-dimensional universe, the dynamic stability point would coincide with the equilibrium point (m_φ = m_z).

Therefore, the dimensionality of space is not a free variable. In a universe with 10, 11 or 26 dimensions, however compactified they might be, the geometric scaling exponents would reach values incompatible with the stability of objects.

The observable phenomena are an emergent property of the three-dimensionality of space.

### 5.8. Dimensional collapse of geometric shielding

The geometric model suggests that the gravitational and electrostatic regimes are not generated by distinct interactions, but emerge from different shielding behaviors against the same radial geometric tension. The collapse of volumetric shielding induces an effective reduction in the dimensionality of geometric propagation.

For a spatial geometry of dimension D, the fundamental geometric cost of occupying space dilutes radially following the standard boundary law:

r^(-(D - 1))

which corresponds to the expansion of radial tension over a D-dimensional hypersurface.

In the macroscopic regime, an object possesses a functional internal volume. This volume acts as a geometric shield: the internal structure is protected from the boundary tension, and the topological cost is cooperatively redistributed across the available spatial degrees of freedom. The effective geometric response is therefore the product of the shielded volume and the boundary dilution:

T_D(r) ~ r^D · r^(-(D - 1))

which simplifies to:

T_D(r) ~ r

For D = 3, this naturally recovers the previously derived macroscopic or gravitational regime, where the interaction scales linearly with the physical radius:

a_g ~ r ~ m^(1 / 3)

Gravity is thus identified as the weak, residual boundary interaction of a fully shielded geometric volume.

As the characteristic scale of the object approaches the fundamental geometric penetration limit (λ), the internal volume progressively loses its ability to redistribute radial attenuation cooperatively.

When r → λ, the internal volume can no longer shield the topological core. The radial tension is dimensionally amplified, violently replicating the geometric constraint across every spatial dimension simultaneously. The loss of shielding introduces an amplification factor governed by the available spatial dimensions:

(λ / r)^(D(D - 1))

The full geometric attenuation law, accounting for both boundary dilution and the collapse of shielding, is then:

C_D(r) = r^(-(D - 1)) · [1 + (λ / r)^(D(D - 1))]

The total effective geometric response (T_D) generated by the enclosed volume is:

T_D(r) = r^D · C_D(r)

which yields the unified polynomial:

T_D(r) = r + r^(1 - D(D - 1))

For a three-dimensional universe (D = 3), the interaction takes the form:

T_3(r) = r + r^(-5)

By substituting the volumetric mass relation (r ~ m^(1 / 3)), this single continuous equation simultaneously recovers both fundamental regimes of the model:

a_g ~ r ~ m^(1 / 3)

and:

a_e ~ r^(-5) ~ m^(-5 / 3)

The transition scale emerges naturally from the absolute minimum of this combined response function:

dT / dR = 0

which yields:

Rφ = 5^(1 / 6) · λ

Since mass scales with volume (m ~ r^3), evaluating the mass at this equilibrium radius yields the stability factor of √5. This shows that the dynamic stability scale (m_φ) is the point where coherent geometric shielding balances against the dimensional amplification of unshielded spatial tension.

### 5.9. Geometric coherence

One of the guiding principles of the Unified Model of Gravitation and Electrostatics is that observable interactions must preserve geometric coherence across all relational configurations.

The model does not require arbitrary physical triangles to be right triangles in Euclidean space. Instead, it proposes that the independent geometric contributions governing interaction combine orthogonally as components of a unified geometric cost.

Within this framework, the transition masses:

m_z, m_s, m_ϕ

form a geometric relation:

m_ϕ^2 = m_z^2 + m_s^2

where:

m_s = 2m_z

This yields:

m_ϕ = √5 · m_z

The quantity m_ϕ therefore emerges as the geometric resultant generated by the orthogonal composition between volumetric equilibrium and structural displacement.

The relation:

1^2 + 2^2 = (√5)^2

does not describe an arbitrary spatial triangle, but the orthogonal composition of independent geometric contributions within the relational structure of the model.

The structural constant:

w = 2

acts as the transverse geometric component governing the displacement between equilibrium and minimal intrinsic acceleration, while:

δ = √5

corresponds to the invariant resultant generated by this composition:

δ = √(1 + w^2)

The geometric coherence of the model therefore emerges not from arbitrary numerical coincidence, but from the orthogonal composition of volumetric and structural propagation costs.

This interpretation is consistent with the broader role of orthogonal invariants throughout modern physics, where observable quantities frequently emerge as geometric resultants of independent relational components.

### 5.10. Geometric formulation of acceleration

Mass and charge are illusions that emerge from geometry, as both can be reduced to volume (V).

The interaction between objects with equal density can be derived as:

F_u = (U / d^2) · ((V_1 · V_2 / z) + s)

a = (U / d^2) · ((V_2 / z) + (s / V_1))

Where d is, in this case, the distance between objects.

The gravitational term (V_2 / z) depends linearly on the volume of the external source. Crucially, it is independent of V_1. This term recovers the strong equivalence principle, but only in the limit where the second term is negligible. The structural term (s / V_1) depends inversely on V_1.

In terms of the object's radii (V ~ r^3):

a = (U / d^2) · ((r_2^3 / z) + (s / r_1^3))

This introduces a non-linear structural term when s ≠ 0, as acceleration becomes dependent on the physical size of the object. Consequently, the universality of free fall is observed only when mass overshadows structure. At the scale of m_φ, the total geometric trajectory diverges from the classical gravitational prediction because the structural cost is no longer negligible.

#### 5.10.1. Density-corrected geometric scaling

The previously derived asymptotic exponents:

a_g ~ m^(1 / 3)

and:

a_e ~ m^(-5 / 3)

emerge from the geometric volumetric relation:

r ~ m^(1 / 3)

which corresponds to the special case of constant density.

However, the geometric structure of the model does not require universal density invariance. The fundamental volumetric relation is instead:

m ~ ρ · r^3

where ρ represents the effective volumetric density of the excitation.

The effective geometric radius therefore becomes:

r ~ (m / ρ)^(1 / 3)

Substituting this relation into the volumetric acceleration regime yields:

a_g ~ m / r^2

a_g ~ m / (m / ρ)^(2 / 3)

a_g ~ ρ^(2 / 3) · m^(1 / 3)

Likewise, the structural regime becomes:

a_e ~ 1 / (m · r^2)

a_e ~ 1 / (m · (m / ρ)^(2 / 3))

a_e ~ ρ^(2 / 3) · m^(-5 / 3)

The density factor therefore appears as a common geometric scaling coefficient affecting both asymptotic regimes identically, while the topological exponents remain invariant.

The intrinsic acceleration equation consequently generalizes to:

a_i ~ ρ^(2 / 3) · (m^(1 / 3) + m^(-5 / 3))

or equivalently:

a_i = (U · ρ^(2 / 3) / r^2) · ((m / z) + (|n| / m))

The relational acceleration equation becomes:

a_r = (U · ρ^(2 / 3) / d^2) · ((m_2 / z) + (s / m_1))

where:

s = n_1 · n_2

The unified interaction force correspondingly becomes:

F_u = (U · ρ^(2 / 3) / d^2) · ((m_1 · m_2 / z) + s)

or equivalently, in primitive geometric form:

F_u = (ħ · c · ρ^(2 / 3) / (d^2 · m_P^2)) · (m_1 · m_2 + m_z^2 · n_1 · n_2)

The equal-density regime therefore represents the canonical geometric limit in which the density correction becomes constant and the pure topological scaling laws emerge explicitly.

Variations in density do not modify the underlying geometric exponents, but only rescale the effective geometric projection between mass and radius.

The asymptotic interaction structure is therefore governed fundamentally by topology and dimensionality rather than by material density itself.

## 6. Structural action and the topological origin of the fine-structure constant

Within conventional electrodynamics, the fine-structure constant is introduced as

α = e^2 / (4 · π · ε_0 · ħ · c)

and is traditionally interpreted as a fundamental dimensionless coupling governing the strength of the electromagnetic interaction.

However, this formulation obscures the geometric reality of the interaction. It distributes the observed value among several quantities whose separation depends entirely on historical electromagnetic normalization conventions. The elementary charge e and the Coulomb normalization factor 1 / (4 · π · ε_0) never appear independently in measurable physical interactions. Only their product is physically relevant.

Defining the macroscopic action scale as:

U = e^2 / (4 · π · ε_0)

yields the direct equivalence:

U = α · ħ · c

This relation reveals that the physically observable quantity is not the elementary charge itself, nor the vacuum permittivity, but the total structural action scale U. However, because U carries macroscopic physical units, it cannot represent the primitive geometric rule of the spatial substrate; it must be the dimensionful projection of a deeper dimensionless invariant.

### 6.1. Elimination of electromagnetic normalization

The geometric model replaces electric charge with a purely topological quantity:

q → n

where n is an integer-valued topological defect number.

Under this description, the Coulomb interaction ceases to be a primitive law. The conventional decomposition

U = e^2 / (4 · π · ε_0)

is interpreted as a historical factorization of a single physical quantity.

The geometric interaction therefore depends only on U and on the topological integers involved:

F_e = U · n_1 · n_2 / r^2

No independent elementary charge is required. No vacuum permittivity is required. No Coulomb normalization constant is required. The entire electromagnetic normalization structure collapses into a single geometric action scale.

### 6.2. Fundamental nature of α and derivation of U

Because the spatial metric evaluates geometric stability exclusively through pure dimensionless ratios, the fine-structure constant (α) is identified not as a derived coupling, but as a primitive topological invariant of the discrete metric.

Within the geometric model, α represents the structural normalization ratio. It defines the fractional geometric cost required to establish a localized topological connection relative to the absolute causal action limit of the discrete metric (ħ · c).

Instead of α being a derived artifact, it is the underlying boundary condition that deterministically generates the macroscopic structural action:

U = α · ħ · c

Under this interpretation, α is restored to its status as a fundamental dimensionless input. It dictates the intensity of structural connections within the causal graph. 

Consequently, the mesoscopic equilibrium mass is derived directly from this fundamental topological cost:

m_z = m_P · √α

and all subsequent structural interactions, while observationally scaling through U, are fundamentally governed by this single dimensionless geometric invariant.

### 6.3. Structural projection and dimensional consistency

Topological defects cannot concentrate arbitrary structural tension within a single geometric node. The structural projection therefore scales with both topological charge and local Compton geometry.

Using the reduced Compton wavelength

ƛ = ħ / (m · c)

the structural projection length becomes

L_e = α · |n| · ƛ

while the volumetric gravitational projection remains

L_g = w · G · m / c^2

The total geometric projection is therefore

L_t = L_g + L_e

revealing a fundamental duality of the substrate.

Volumetric effects scale proportionally with mass. Structural effects scale inversely with mass.

### 6.4. Unified interaction

The elimination of electromagnetic normalization exposes a direct geometric decomposition of interaction strength.

The volumetric component is

F_g = (ħ · c / r^2) · (m_1 · m_2 / m_P^2)

while the structural component is

F_s = (U / r^2) · n_1 · n_2

The unified interaction becomes

F_u = (ħ · c / r^2) · (m_1 · m_2 / m_P^2) + (U / r^2) · n_1 · n_2

This expression contains no elementary charge, no vacuum permittivity, and no electromagnetic coupling constant. All interactions are transmitted through the same geometric substrate.

The apparent distinction between gravitational and electromagnetic phenomena originates solely from whether the source excitation acts through volumetric redistribution of the substrate or through localized topological saturation.

## 7. Nature of G

The hybrid complexity of the units of G contrasts with the elemental simplicity of the primitive geometric action scale ħ · c. G is revealed not as a fundamental constant, but as a composite artifact that can be expressed in simpler, fundamental geometric terms.

### 7.1. Origin of the empirical dispersion

The large dispersion presented by the empirical measurements of G cannot be attributed to a systematic methodological error. This dispersion is interpreted as the direct manifestation of the anomaly that the model predicts at the m_φ scale.

The model establishes:

G = ħ · c / m_P^2

and:

m_z^2 = α · m_P^2

Given that these constants are defined with great precision, the dispersion of G can only depend on the relationship between m_z and the effective geometric redistribution of the interacting masses. Therefore, any variation in the fundamental conditions of the measurement, including the temporal dimension, can influence the value obtained.

Experiments do not measure the universal static constant G, but the local effective redistribution state of the interacting geometric substrate of the specific test masses involved. The dispersion in the measurements (≈ 22 ppm) is the precise signature of the magnitude of this phenomenon in the terrestrial scenario.

### 7.2. Scale-dependent inertial behavior

The baryonic mass of an object is an invariant constant independent of scale.

However, the observable physical magnitude does not depend solely on the amount of matter, but on the efficiency of its interaction with space.

The factor γ is defined as a function of the relationship between the observable effective mass (m_eff) and the baryonic mass (m_b):

m_eff = m_b · γ

Where m_b is the invariant sum of the masses of the fundamental components and γ is the inertial efficiency coefficient derived from the stability equation.

For a macroscopic neutral body, the volume acts as a geometric shield. Surface constraints are negligible and the interaction is purely volumetric. The acceleration recovers the classical inertial behavior:

γ = 1

For an unshielded mesoscopic object, the effective inertia is interpreted as the inverse of its capacity for intrinsic acceleration (1 / a_i). Because the intrinsic acceleration function a_i(m) possesses a unique global minimum at the dynamic stability scale m_φ, the effective inertia of an unshielded object reaches its absolute maximum at this specific scale. Therefore, a granular sample enriched in non-neutral particles (|n| ≠ 0) close to m_φ does not inherit the classical volumetric inertia.

Instead, the system acts as an aggregate of extremized inertias, maximizing the local structural cost:

γ > 1

Under this interpretation, a granular sample satisfying |n| ≠ 0 and calibrated to the scale m_φ will exhibit an anomalous inertial response compared to a macroscopic solid control sample possessing the same baryonic mass. 

### 7.3. Strong equivalence principle

The model preserves the identity between inertial mass and gravitational mass as an invariant baryonic property:

m_i = m_g = m

No distinction is introduced between gravitational and inertial mass themselves.

However, the model proposes that the observable acceleration of a physical object is not determined exclusively by the volumetric contribution associated with mass, but by the complete intrinsic geometric structure encoded by:

a_i = a_g + a_e

where the structural contribution depends on the existence of discrete topology through |n|.

For perfectly neutral objects:

|n| = 0

the structural contribution vanishes:

a_e = 0

and the intrinsic acceleration reduces to the purely gravitational regime:

a_i = a_g

In this limit, the universality of free fall is fully recovered.

However, for objects with |n| ≠ 0, the total geometric response contains both volumetric and structural contributions simultaneously.

The model therefore predicts that the observable response of an object is not determined by mass alone, but by the complete geometric configuration of the excitation.

The strong equivalence principle consequently emerges as an asymptotic limit of the volumetric regime rather than as an universal property valid for all geometric configurations.

At macroscopic scales, where the volumetric contribution dominates overwhelmingly, the structural contribution becomes effectively negligible and the classical equivalence principle is recovered to extremely high precision.

At mesoscopic scales, however, the model predicts that the structural contribution may become non-negligible, leading to composition-dependent deviations from purely volumetric inertial behavior.

The quantity m_ϕ defines the characteristic scale at which the intrinsic acceleration reaches its minimum geometric configuration through the convex superposition of the volumetric and structural regimes.

The model therefore does not interpret free fall as the manifestation of an isolated gravitational interaction, but as the observable projection of the complete geometric response structure of matter.

### 7.4. Composition dependence and the limits of the strong equivalence principle

The present framework preserves the identity between inertial mass and gravitational mass:

m_i = m_g = m

However, the model rejects the assumption that observable acceleration can be determined exclusively by mass independently of composition.

The relational acceleration is given by:

a_r = (U / d^2) · ((m_2 / z) + (s / m_1))

where:

s = n_1 · n_2

The first term corresponds to the volumetric contribution associated with mass, while the second corresponds to the structural contribution associated with topology.

If acceleration were independent of composition, the structural term would have to vanish identically for all physical configurations.

In that limit, the interaction would reduce exclusively to the volumetric regime:

a_r = (U / d^2) · (m_2 / z)

which reproduces Newtonian gravitation but cannot reproduce the electrostatic regime.

Conversely, the existence of a unified interaction law capable of reproducing both Newtonian gravitation and Coulomb interaction necessarily requires the existence of a structural contribution that depends on composition through topology.

Therefore, strict composition-independent acceleration is mathematically incompatible with unified interaction dynamics.

The strong equivalence principle is consequently recovered only as an asymptotic limit in which the volumetric contribution overwhelmingly dominates the structural contribution. This asymptotic suppression explains why the principle appears experimentally exact at macroscopic scales, while remaining mathematically non-fundamental.

The model preserves the equivalence between inertial and gravitational mass while rejecting the assumption that mass alone completely determines the observable geometric response of matter.

### 7.5. Inertia as geometric response

In classical mechanics, inertia is commonly interpreted as the resistance of matter to acceleration. This interpretation emerges naturally in the macroscopic volumetric regime, where the observable dynamics of matter are overwhelmingly dominated by mass and where the structural contribution becomes asymptotically negligible. However, acceleration is not generated exclusively by volumetric interaction.

At large scales, where the volumetric contribution dominates overwhelmingly, the structural term becomes asymptotically suppressed and the classical notion of inertia emerges as an effective approximation of the observable dynamics.

At small scales, however, the structural contribution introduces an increasingly dominant geometric cost associated with propagation itself. In this regime, the resistance to geometric displacement no longer scales primarily through volume, but through the structural geometry of the excitation.

The model therefore does not interpret inertia as an isolated intrinsic property of passive matter, but as the observable consequence of geometric compatibility under displacement. The apparent resistance to motion emerges from the total geometric cost associated with changing relational configuration in space. This interpretation becomes particularly relevant near the mesoscopic transition region, where neither the volumetric nor the structural contribution can be neglected independently.

The model consequently suggests that the classical concept of inertia is not fundamental, but emergent from the dominance of the volumetric regime at macroscopic scales. Under this interpretation, inertial behavior, gravitational interaction, and electrostatic interaction are not independent mechanisms, but different observable manifestations of the same relational geometric structure.

## 8. Integration of general relativity

### 8.1. Relativity without singularity

General relativity describes gravity as the curvature of space. This curvature is reinterpreted here as the structural response of space in the presence of an object. When an object's density pushes space to its structural limit, the linear or Newtonian behavior transitions to the non-linear or relativistic regime. In this context, the notion and necessity of a mediating particle like the graviton is excluded.

General relativity predicts singularities because it does not include a limit of space curvature. The Schwarzschild solution defines the event horizon of a black hole as:

r_S = 2 · G · m / c^2

The factor 2 is identified with w, and r_S is interpreted as the point where the geometric potential (U · m / z) equals the maximum energy capacity of space (c^2 / w):

r_S = (w · U · m) / (z · c^2)

Space has a geometric saturation limit. This theoretical limit is the Planck force:

F_P = c^4 / G

Given that the universe operates at the structural action scale U rather than at the pure Planck scale, this structural ceiling is established according to the same geometric law as mass:

F_max = F_P · √(U / (ħ · c))

F_max ≈ 1.03 × 10^43 N

This value represents the maximum structural cost that space can sustain.

Here, α is stripped of its historical electromagnetic interpretation and revealed as the primitive dimensionless geometric invariant of the lattice. It deterministically anchors the equilibrium mass transition

α = m_z^2 / m_P^2

and quantifies the fractional boundary between fully volumetric propagation and localized topological saturation.

According to general relativity, mass collapses towards a point of infinite density (r = 0). This singularity is eliminated by imposing a physical limit on the geometric curvature of space (1.03 × 10^43 N). This limit resolves the main mathematical conflict with quantum mechanics.

Gravity has been historically conceived as a continuum, which inevitably leads to mathematical infinities, or singularities. However, physics is the science of measurable quantities, and no measurement can yield infinity. This model operates on a discrete topology where infinity is structurally impossible. The singularity is thus replaced by a state of geometric saturation.

### 8.2. Neutron stars

In main sequence stars, F_e maintains atomic volume against F_g. When a star collapses and F_g overcomes the structural limit of F_e, the fusion of protons and electrons into neutrons results in a macroscopic single domain with |n| = 0.

## 9. Nature of space and time

### 9.1. Pixel of the universe

To define physical existence, an object must present a non-zero effective interaction cross-section. In a three-dimensional universe, a purely one-dimensional structure would have a zero cross-section, making it physically undetectable or incapable of storing information. Therefore, physical existence depends, at a minimum, on a geometric configuration containing two orthogonal dimensions.

Given the linear nature of the structural constant w = 2, the minimum stable area (A) must be the square of this structural length:

A = (w · l_P)^2 = w^2 · l_P^2 = 4 · l_P^2

This minimum area acts as the fundamental unit of information. Therefore, the fundamental linear length of the cosmic pixel (ℓ) is derived as:

ℓ = √(w^2 · l_P^2)

ℓ = w · l_P

ℓ = 2 · l_P

ℓ ≈ 3.232510 × 10^(-35) m

Thus, space has a functional pixelation with a linear dimension equal to 2 · l_P. Below this size, the notion of distance dissolves, since there is not enough extent to satisfy the structural constraint w = 2, necessary to define a physical configuration.

This fundamental length acts as an invariant metric constant. The transition between regimes does not imply a dilation of this pixel, but a change in the topology of space. The geometric cost does not imply the existence of any substance, ether or rigid scaffolding. Instead, the cubic lattice should be understood as the synchronization pattern that arises because every physical interaction must satisfy the structural limit (ℓ).

#### 9.1.1. Dimensional origin of the geometric pixel

The Planck length (l_P) is defined through dimensional analysis as a boundary where the classical description of space-time yields a singularity. This definition relies on the implicit assumption that the underlying metric constitutes a continuous background. Within a discrete geometric framework, l_P is reinterpreted as a fundamental dimensional projection limit rather than an absolute physical resolution boundary. The actual structural pixel (ℓ) is determined by the discrete geometric constraint of three-dimensional space, formalized by the topological constant w = 2. The physical substrate resolution is derived from the linear dimension required to support a stable geometric node, resulting in ℓ = w · l_P = 2 · l_P. This coefficient is not a retrospective correction of the original derivation by Planck, but the identification of the structural dimensionality of space, which remains inaccessible to models that lack a discrete causal lattice. Consequently, the pixel ℓ acts as the invariant metric resolution, while l_P serves as the dimensional scaling coefficient required to map the discrete nodes of the causal graph onto the macroscopic SI coordinate system.

### 9.2. Pixel equation

The equation of intrinsic acceleration can be rewritten exclusively with fundamental constants and geometric parameters.

Given the standard relationship:

l_P = √((ħ · G) / c^3)

the emergent gravitational constant is isolated through the pixel area:

G = (c^3 · ℓ^2) / (w^2 · ħ)

G = (c^3 · (2 · l_P)^2) / (4 · ħ)

This reveals that the intensity of gravity is directly proportional to the area of the fundamental pixel (ℓ^2). In a continuous universe, where ℓ approaches zero, gravity vanishes.

Given the electromagnetic action balance:

α = (k_e · e^2) / (ħ · c)

the structural surface regime is isolated as:

k_e · e^2 = α · ħ · c

Substituting these fundamental definitions into the unified equation of intrinsic acceleration yields the complete expression governed by the square-root metric saturation:

a_i = [((c^3 · ℓ^2) / (w^2 · ħ) · (m / r^2)) + ((ħ · c · m_z^2 · |n|) / (m_P^2 · m · r^2))] / √(1 - L_t / r)

a_i = [G · (m / r^2) + ((ħ · c · m_z^2 · |n|) / (m_P^2 · m · r^2))] / √(1 - L_t / r)

This equation governs all interactions across both the gravitational and electrostatic regimes. The concept of "force" is determined solely by which term dominates within the numerator based on the mass (m) of the object.

G and k_e are not independent parameters of nature, but scaling artifacts arising from the fundamental granularity of space. There is no break between classical and quantum mechanics. F_g is the residual effect of ℓ acting on volumetric aggregates, while F_e is the direct action of localized topological saturation acting on unresolved geometric surfaces.

#### 9.2.1. Recovery of Newton's law

The macroscopic limit is evaluated using terrestrial parameters where mass dominates over discrete topology:

m_⊕ ≈ 5.972 × 10^24 kg

r_⊕ ≈ 6.371 × 10^6 m

Because the physical distance r_⊕ is vastly larger than the projected geometric length L_t, the square-root saturation factor reduces to unity:

√(1 - L_t / r) → 1

Volumetric term:

a_g ≈ 9.8203 m / s^2

Surface term:

a_e ≈ 1.0000 × 10^(-67) m / s^2

#### 9.2.2. Recovery of Coulomb's law

The microscopic limit is evaluated using subatomic parameters where structural surface terms dominate the numerator:

m_p ≈ 1.673 × 10^(-27) kg

r_p ≈ 0.841 × 10^(-15) m

Because the interaction distance remains large relative to the subatomic projection length, the saturation factor reduces to unity:

...

√(1 - L_t / r) → 1

Volumetric term:

a_g ≈ 1.0000 × 10^(-7) m / s^2

Surface term:

a_e ≈ 1.9510 × 10^29 m / s^2

### 9.3. Geometric emergence of ħ

The reduced Planck constant (ħ) is not an independent primitive quantity, but a direct consequence of the discrete metric structure of space.

Given the pixel definition:

ℓ = 2 · l_P

The maximum structural tension that space can sustain is the Planck force:

F_P = c^4 / G

Projecting this structural limit onto the minimum geometric surface (ℓ^2) yields:

F_P · ℓ^2 = (c^4 / G) · ℓ^2

Since w = 2 defines the minimum stable geometric configuration, the primitive action scale satisfies:

ħ · c = (F_P · ℓ^2) / w^2

Therefore, isolating the quantum of action yields:

ħ = (c^3 · ℓ^2) / (w^2 · G)

This identity shows that ħ emerges from the discrete geometry of space. The quantum of action is the geometric consequence of a finite spatial pixel combined with the maximum propagation velocity c and the structural saturation limit of the metric.

### 9.4. Geometric derivation of Bekenstein-Hawking entropy

Within the geometric model, black hole entropy emerges as a consequence of geometric saturation in a discrete spatial metric.

The framework does not interpret entropy as a thermodynamic measure of microscopic disorder, but as the finite geometric occupancy capacity of a causally saturated surface.

As established previously, the discrete substrate possesses a minimum stable geometric interval:

...

ℓ = w · l_P

where the structural constant is fixed by the spatial dimensionality:

w = 2

The minimum stable geometric surface element is defined as:

A_ℓ = ℓ^2

A_ℓ = w^2 · l_P^2

Evaluating the structural factor yields the pixel area:

A_ℓ = 4 · l_P^2

For a saturated geometric boundary of macroscopic area A, the total number of available geometric surface states is:

N = A / A_ℓ

N = A / (4 · l_P^2)

The Bekenstein-Hawking entropy relation is recovered:

S = A / (4 · l_P^2)

This expression emerges as the counting of discrete geometric surface pixels supported by the saturated metric boundary.

The factor 4 is not introduced through semi-classical thermodynamic arguments, but emerges geometrically as the square of the structural scaling constant:

w^2 = 4

Under this interpretation, the event horizon represents the limiting state where volumetric propagation becomes fully saturated under the square-root boundary limit. The metric can no longer sustain coherent volumetric redistribution throughout the interior region. The available geometric degrees of freedom collapse onto the boundary surface itself.

Black hole entropy emerges as another manifestation of dimensional propagation collapse within the discrete metric substrate.

The Bekenstein-Hawking relation is reinterpreted as the geometric occupancy law governing the maximum surface information capacity permitted by the finite causal resolution of space.

This same geometric mechanism reappears in confined Casimir cavities and in the dimensional propagation collapse associated with linear confinement.
### 9.5. Time in three dimensions

The coherence of the model critically depends on the dynamic stability factor δ = √5. This value obeys the general law of inertial displacement for a D-dimensional universe:

δ = √(2 · D - 1)

Applying this law to different topologies, the function of time is revealed as an emergent property.

In a universe with D = 3:

δ = √(2 · 3 - 1) = √5

The static structure of space is composed of two orthogonal axes: the volumetric dimension (base = 1) and the structural dimension (height = w = 2). The vectorial resultant of this static geometry is the hypotenuse:

√(1^2 + 2^2) = √5

The dynamic value (δ = √5) coincides with the geometric resultant.

In a universe with D = 4:

δ = √(2 · 4 - 1) = √7

the static structure (w = 3) would generate a vectorial resultant of:

√(1^2 + 3^2) = √10

There is an unresolvable discrepancy between the static structure (√10) and the dynamic necessity (√7).

This shows that time does not act as a fourth structural dimension, since the unstable dynamics that would emerge simply do not coincide with what is observed.

### 9.6. Geometric definition of time

Time is geometrically defined as the accumulated hypotenuse of the trajectory. In any interaction between a point A and a point B, the base represents the linear spatial distance. However, the structural constraint of three-dimensional space imposes deviations, defined by orthogonal components. An object in motion resolves this constraint by traversing the resulting hypotenuse.

Time as a physical magnitude is the summation of the hypotenuses generated during the path, or the actual distance traveled to resolve its geometric cost. In the absence of a pre-existing temporal dimension, velocity is not defined as distance divided by time:

v = d / t

but in terms of geometric efficiency, through the proportion between the effective distance advanced, corresponding to the base (B), and the total distance traveled, corresponding to the hypotenuse (H):

v = B / H

In a displacement through the pixelated structure of the universe, each step is quantified according to:

ℓ = 2 · l_P

For a photon (m = 0), the movement is rectilinear and has no structural cost. This represents the maximum efficiency in motion:

B = 1

H = √(1^2 + 0^2) = 1

v = 1 / 1 = 1

In normalized geometric units, this corresponds to:

c = 1

For a stable mass (m > 0), the constant w = 2 imposes an orthogonal structural deviation for each unit of displacement, such that each step generates a new hypotenuse:

B = 1

H = √(1^2 + 2^2) = √5

This ratio represents the geometric efficiency factor (η_g) of massive propagation:

η_g = 1 / √5 ≈ 0.447

Unlike photons (v = c), massive objects must resolve the orthogonal structural cost, implying that the effective propagation of the geometric configuration is intrinsically retarded by this factor relative to the geodesic base. The perceived time corresponds to the accumulation of hypotenuses.

This dynamic implies that movement is not the displacement of a substantial body through a passive medium, but the propagation of a topological configuration through the structure of space. The geometric nodes do not spatially displace. Only their structural state is sequentially transferred. Consequently, the model excludes the appearance of phenomena of turbulence or viscous drag, substituting the notion of mechanical friction with the concept of geometric cost. This is consistent with the underlying principle that matter is not a substance, but a configuration of space.

Since velocity is defined as the geometric efficiency ratio between the spatial advance (B) and the total structural path (H), superluminal velocity (v > c) would imply:

B > H

which is not possible in Euclidean geometry. The speed of light is not merely an energetic barrier, but a trigonometric constraint.

Crucially, this definition of time as a geometric resultant rather than a scalar step-counter acts as a continuous normalization mechanism. It compensates for the discrepancies inherent in a discrete lattice, ensuring that the propagation velocity c remains invariant in all directions. The variation in structural steps between different angles is conserved not as a difference in speed, but as a difference in the energy density, or frequency, of the propagating entity.

#### 9.6.1. Recovery of Newton's law

In Newtonian mechanics, the free-fall time (t_N) from a height (h) under acceleration (a) is given by:

t = √((2 · h) / a)

The time (t_u) of a displacement is defined as the total hypotenuse (H_t) traveled at velocity c:

t_u = H_t / c

To calculate H_t, the infinitesimal segments of the path are integrated. Knowing that the instantaneous velocity (v) represents the geometric efficiency at each point:

v = c · d x / d H

the differential of the real path is:

d H = (c · d x) / v

H_t = ∫_0^h (c / v(x)) d x

Since:

v(x) = √(2 · a · x)

H_t = c · ∫_0^h (1 / √(2 · a · x)) d x

The resolution of this integral determines the length of the geometric trajectory:

H_t = c · √((2 · h) / a)

The normalization of the distance by c yields the magnitude of the perceived time:

t_u = (c · √((2 · h) / a)) / c

t_u = √((2 · h) / a)

t_u = t_N

Newton's law is, therefore, the calculation of the arc length of a trajectory. The magnitude of the perceived time is the scalar representation of a much larger physical distance traveled.

This geometric disproportion (c / v) is the measure of dynamic inefficiency of objects in relation to c. Gravity is a slope that allows the geometric efficiency to improve as the object advances by tilting the hypotenuse.

#### 9.6.2. Recovery of Coulomb's law

Just as Newton's law is recovered by analyzing the projection of volume in space, Coulomb's law is recovered by analyzing the projection of the surface.

The three-dimensionality of the universe imposes that the intensity of any geometric interaction diverging from a point must be distributed over the area of a sphere:

A = 4 · π · r^2

In the electrostatic regime, the property that defines the interaction is not the volume, but the surface topology (s). The interaction is geometrically distributed throughout the surrounding space. Given that space is three-dimensional, the influence surface grows according to 1 / r^2:

F_e = (U · s) / r^2

#### 9.6.3. Geometric origin of Newton's third law

The geometric definition of physical propagation inherently resolves the mechanical axiom of action and reaction. Newton's third law postulates that every force exerts an equal and opposite reaction, yet classical mechanics provides no fundamental mechanism explaining why interactions must be perfectly bidirectional.

Within the geometric framework, forces are not independent vectors injected into an empty background, but continuous recalculations of structural cost across the discrete causal graph. When an object A displaces against an object B, the spatial metric must resolve the topological proximity by computing the structural strain across the boundary. This strain corresponds to the generation of the orthogonal geometric hypotenuse:

H = √(B^2 + w^2)

Because the spatial metric is a connected relational graph, this computed geometric tension does not belong individually to object A or object B; it is the physical property of the topological connection linking their adjacent discrete nodes. 

Consequently, any attempt to propagate node A against node B requires the metric to register the exact same structural hypotenuse from the perspective of both configurations simultaneously. It is mathematically impossible for the metric to compute a geometric cost for the advance of A without the adjacent node of B registering the identical spatial tension in the conjugate direction. 

Newton's third law of motion is therefore not a dynamical decree, but a trigonometric tautology of the discrete causal lattice. Action and reaction are identified as the exact same line of geometric code—a single structural hypotenuse—read simultaneously from opposite ends of a connected topological boundary.

### 9.7. Principle of least geometric action

The model has been presented primarily as a derivation of geometric states. However, the dynamics described by the intrinsic acceleration equation (a_i) can be formalized as a consequence of a variational principle, satisfying the requirement for a fundamental action.

In standard physics, the action (S) is defined as the integral of the Lagrangian over time. In the geometric framework, where time is an emergent property of the trajectory, or the hypotenuse, the action is defined as the integral of the structural cost (C_s) over the spatial path.

#### 9.7.1. Geometric action

ħ is conventionally treated as a fundamental quantization of energy. The geometric model identifies it as a derived structural limit.

The fundamental pixel of the universe is defined with a linear dimension:

ℓ = 2 · l_P

This implies an effective rotational radius of:

r = l_P

If m_P represents the mass saturation of this fundamental node, then ħ is the mechanical angular momentum of the space lattice itself:

ħ = m_P · l_P · c

Thus, ħ represents the inevitable rotational limit of a geometric node with mass m_P and radius l_P transmitting information at maximum efficiency (c). It quantifies the granularity of action in a discrete geometry.

The geometric action (S_g) is defined as the accumulation of topological friction along a trajectory (q) in the configuration space:

S_g[q] = ∫ (C_s · d l)

Where d l is the differential of the structural path length, which accounts for the discrete nodal interactions, distinct from the Euclidean displacement d x.

As previously derived, the structural cost scales according to the superposition of the volumetric and superficial terms:

C_s = A · m^(1 / 3) + B · m^(-5 / 3)

This function acts effectively as the scalar potential of the system. Unlike a gravitational potential which is extrinsic, C_s is intrinsic to the mass-space relation.

#### 9.7.2. Derivation of dynamics

The fundamental physical law of the model is the principle of least geometric action: physical systems evolve along the path that minimizes structural cost.

δS_g = 0

Applying the variational method to this functional implies that the gradient (∇) of the cost function determines the motion vector. The resulting Euler-Lagrange equations yield:

a_i = -∇C_s

Intrinsic acceleration equation is not a heuristic postulate, but the solution to the minimization of the geometric action.

#### 9.7.3. Emergence of time

This formulation validates the geometric definition of time. Since the speed of the process is determined by the geometric efficiency:

v = B / H

the temporal parameter (t) emerges naturally from the action integral:

d t ~ d l / v(C_s)

Thus, the model is dynamically complete. It possesses a configuration space, a cost functional, and a variational principle. The apparent absence of a time-dependent Lagrangian is not a deficit, but a consequence of solving the dynamics directly in the spatial metric, rendering time phenomenological.

### 9.8. Geometric derivation of angular momentum and inertia

In classical mechanics, rotational inertia and angular momentum are typically introduced as independent dynamical quantities. Within the geometric model, both emerge as macroscopic consequences of the geometric cost required to maintain the coherent propagation of an extended configuration through a discrete three-dimensional substrate.

The model previously established that the occupation of space carries a geometric cost:

C_s ~ m^(1 / 3) + m^(-2 / 3)

This quantity measures the structural burden associated with maintaining a stable geometric configuration within the metric substrate.

Rotational motion does not introduce a new physical mechanism. Instead, it corresponds to the continuous angular redistribution of an existing geometric cost.

Consider a coherent configuration rotating with angular velocity:

ω

Every differential element of the configuration must remain synchronized in order to preserve structural coherence.

The local tangential propagation velocity satisfies:

v = ω · r

where r denotes the distance from the rotation axis.

Because the geometric cost must be continuously updated during rotation, the local rotational propagation cost scales with the square of the update rate. The differential rotational energy therefore becomes proportional to the differential geometric cost:

dE_rot ~ ω^2 · r^2 · dC_s

The factor r^2 emerges from the geometric exposure of the rotating element relative to the rotation axis.

Integrating over the complete configuration yields:

E_rot ~ ω^2 · ∫ r^2 · dC_s

The geometric rotational inertia is therefore defined as:

I_s = ∫ r^2 · dC_s

Unlike the classical moment of inertia, which is expressed in terms of mass distribution alone, I_s measures the second moment of the geometric cost distribution associated with the configuration.

Using the conventional normalization of rotational energy:

E_rot = (1 / 2) · I_s · ω^2

The classical quadratic structure therefore emerges as the macroscopic limit of geometric cost redistribution.

Angular momentum follows directly from the rotational energy function. Defining the conjugate quantity associated with angular propagation:

L = ∂E_rot / ∂ω

yields:

L = I_s · ω

Angular momentum is therefore interpreted as the accumulated geometric cost associated with coherent rotational propagation.

The persistence of this accumulated cost naturally generates resistance to changes in rotational state and orientation.

Gyroscopic stability consequently emerges as a macroscopic manifestation of the same geometric cost responsible for rotational inertia.

The classical expressions for rotational energy, angular momentum, and gyroscopic rigidity therefore appear as emergent macroscopic manifestations of the same geometric structure previously responsible for inertia and intrinsic acceleration.

Rotational dynamics require no additional primitive postulates beyond the geometric cost already associated with stable occupation of space.

### 9.9. Geometric determinism of exponents

The exponents 1 / 3 and -5 / 3 are not free parameters but consequences of the metric saturation limit:

ℓ = 2 · l_P

The transition mass (m_z), where volumetric and surface terms equilibrate, is geometrically fixed by the pixel scale:

m_z = (ħ · λ_z) / (ℓ · l_P · c)

The saturation ratio (S) at the fundamental boundary (r = ℓ) confirms this structural necessity:

S = F_e(ℓ) / F_max = α / 4

Where:

F_max = 1.03 · 10^43 N

The 1 / 3 exponent is the unique solution for energy dispersion in a three-dimensional (D = 3) Euclidean volume, and the -5 / 3 exponent is the mandatory solution that prevents surface forces from exceeding F_max at the Planck scale.

Any deviation from these exponents would result in a metric singularity or physical instability. Thus, the exponents are topologically determined by the saturated discrete metric.

#### 9.9.1. Mathematical proof of uniqueness

To prove that the topological exponents p = 1 / 3 and q = -5 / 3 are uniquely determined by the discrete metric structure, an arbitrary perturbation scale ε, δ ∈ ℝ is introduced such that the generalized intrinsic acceleration potential takes the form:

V(Ψ) = A · Ψ^(1 / 3 + ε) + B · Ψ^(-5 / 3 + δ)

Where A and B are the coupling scales mapped to U and z.

In the asymptotic limit of large metric occupancy (Ψ ≫ 1), the volumetric term dominates. The acceleration scales as:

a_g ~ Ψ^(1 / 3 + ε)

If ε > 0, the spatial capacity increases faster than the Euclidean volume embedding (D > 3), violating the Birkhoff theorem and making the gravitational constant G distance-dependent at macroscopic ranges. If ε < 0, the metric field fails to satisfy the dimensional boundary conditions of the Einstein-Hilbert action in the weak-field limit. Thus:

ε ≡ 0

is uniquely required to preserve stable D = 3 Euclidean bulk asymptotics.

At the fundamental boundary where the physical interaction distance approaches the metric resolution limit:

r → ℓ = 2 · l_P

the structural term becomes constrained by the maximum allowable cosmic force:

F_max = c^4 / G

Let the structural interaction energy be evaluated at the boundary lattice. If δ > 0, the negative scaling exponent becomes shallower. As m → 0, the local structural acceleration gradient diverges slower than the metric volume collapses, causing a failure in the local confinement mechanism and collapsing the localized topological charge into a metric singularity.

Conversely, if δ < 0, the gradient diverges faster than the metric capacity can dissipate flux. At the discrete pixel scale ℓ, the structural force would yield:

F_s(ℓ) ∝ m · a_s

~ m · m^(-5 / 3 + δ)

⇒ F_s(ℓ) > F_max

This violates the metric saturation limit, injecting non-physical super-Planckian tensions into the local discrete nodes.

Because any non-zero value for ε or δ leads either to a deviation from the empirically verified macroscopic Newtonian limit or to an unphysical stress state exceeding F_max at the pixel boundary, the tuple:

(p, q) = (1 / 3, -5 / 3)

is mathematically unique. They are not parameters of a phenomenological fit, but the only geometrically admissible solutions for a non-singular, saturated discrete universe.

### 9.10. Principle of geometric coherence cost

The unified geometric framework developed throughout this work naturally admits an informational interpretation of physical propagation.

Physical objects are not interpreted as independent entities moving through an inert background, but as coherent topological projections maintained across a discrete spatial metric. Physical displacement therefore requires continuous geometric updating of the object's spatial projection as it propagates through the lattice.

Under this interpretation, mass is not fundamentally understood as a primitive quantity of matter, but as an emergent measure of the geometric coherence cost required to maintain a stable volumetric projection during propagation.

The unified geometric response function:

T_3(r) = r + r^-5

is identified with the geometric coherence cost introduced previously.

Consequently:

C_s ∝ T_3(r)

and, under normalized units:

C_s = T_3(r)

The unified geometric response therefore represents the scale-dependent coherence cost required to maintain a stable propagation state through the discrete metric.

In the macroscopic regime:

T_3(r) ~ r

the object possesses a functional internal volume capable of cooperatively redistributing radial attenuation across the available spatial degrees of freedom. The geometric state remains highly compressible, and coherent propagation requires only weak incremental geometric updating as the object moves through the lattice.

This regime corresponds to gravitation.

In the microscopic regime:

T_3(r) ~ r^(-5)

the volumetric redistribution of radial attenuation collapses near the geometric penetration scale λ. The spatial projection progressively loses its cooperative redistribution capacity, and coherent propagation becomes dimensionally amplified across the exposed geometric boundary.

Under these conditions, the geometric coherence cost increases abruptly as the characteristic scale decreases.

This regime corresponds to electrostatic behavior.

The mesoscopic transition scale m_φ consequently acquires a natural informational interpretation. Rather than representing only the minimum of the intrinsic acceleration curve, it may also be interpreted as the unique point of minimal geometric coherence cost, where volumetric redistribution and dimensional amplification reach equilibrium.
The condition:

dT / dR = 0

therefore defines the point of maximal propagation efficiency across the spatial metric.
Within this interpretation, inertia emerges naturally as the resistance associated with increasing the rate of coherent geometric updating required for propagation through the lattice.

The geometric action:

S_g = ∫ C_s · dl

can consequently be interpreted as the cumulative coherence cost associated with maintaining a propagating geometric state across the spatial metric.

This informational interpretation does not require the universe to behave as a digital computer in the conventional sense. Rather, it suggests that finite geometric propagation inherently possesses an effective informational cost associated with maintaining coherent spatial structure across a discrete metric substrate.

Several quantities traditionally interpreted as fundamental physical constants may instead emerge as effective scaling parameters associated with finite geometric resolution, coherent propagation, and informational saturation within the spatial lattice.

### 9.11. Geometric origin of the uncertainty principle as causal resolution limit

In standard quantum mechanics, Heisenberg's uncertainty principle is often interpreted as a fundamental probabilistic fuzziness of nature or an unavoidable epistemological limit imposed by the act of measurement. Quantum indeterminacy is neither probabilistic nor observer-dependent. It is deterministically derived as the mathematical resolution limit of conjugate variables operating within a background-independent, discrete causal graph.

#### 9.11.1. Conjugate variables on a discrete graph

In a continuous classical space, position (x) and momentum (p) can be defined simultaneously with infinite precision. However, within an emergent causal graph governed by a finite fundamental length (ℓ) and a discrete update cycle, these classical continuous variables are incompatible.

To define the spatial position of a localized topological defect implies identifying its structural locus at a single, frozen instant in the causal sequence. It represents a static snapshot of one geometric node.

Conversely, momentum (or kinetic energy) represents the rate of topological transitions across the causal graph. By definition, a rate of transition cannot be calculated from a single isolated node; its measurement requires observing the defect as it completes at least one minimal causal update across adjacent nodes.

Therefore, absolute geometric localization (zero geometric transition) and absolute momentum definition (continuous geometric transition) are mutually exclusive operations on a discrete graph. 

#### 9.11.2. Microscopic action limit

The minimum structural effort required to complete one fundamental transition across the causal graph is defined by the fundamental quantum of action (ħ). 

Because the localized defect cannot advance through the network without consuming at least this single discrete quantum of action, the product of the spatial resolution (Δx) and the momentum resolution (Δp) is inherently bounded from below by the indivisibility of the update cycle:

Δx · Δp ~ ℓ · m · c

Using the established primitive inputs where the interaction scale restricts the transition:

Δx · Δp ≥ ħ / 2

The uncertainty relation is thus derived not as a mysterious quantum fluctuation, but as the unavoidable geometric truncation error—the pixelation noise—that arises when attempting to map continuous macroscopic variables (position and momentum) onto the indivisible fundamental transitions of a discrete causal network.

#### 9.11.3. Scale-dependent attenuation and the classical limit

The structural state of a propagating object can be characterized through two complementary geometric magnitudes within the graph:

* Local spatial resolution (ΔR): The degree to which the metric can resolve the exposed geometric boundary of the object.

* Coherent propagation cost (ΔC): The structural effort required to maintain topological integrity during propagation.

In the microscopic regime, the object operates directly at the resolution boundary of the graph. The metric is fully exposed to the unresolved causal sequence, amplifying the coherence cost (ΔC → max) and manifesting the fundamental uncertainty limit.

However, as derived previously, the unified geometric response:

T_3(r) = r + r^(-5)

acts as a scale-dependent attenuation law. In the macroscopic regime (r ≫ ℓ), an object consists of a vast, cooperative configuration of topological defects spanning billions of causal nodes. This internal volume cooperatively redistributes the radial attenuation across available spatial degrees of freedom.

This volumetric redistribution acts as a deterministic statistical smoothing mechanism. The discrete pixelation noise of the individual ħ updates is averaged out across the massive composite structure. As local geometric resolution decreases on average, the coherent macroscopic propagation becomes progressively less sensitive to the metric discreteness.

Classical determinism (where Δx and Δp appear infinitely precise) is therefore recovered as the large-scale thermodynamic limit of geometrically attenuated indeterminacy. The uncertainty principle never disappears; its discrete resolution noise becomes statistically imperceptible within massive cooperative structural updates.

### 9.12. Impossibility of perfect geometric equilibrium

If physical space possesses finite resolution, exact geometric equilibrium cannot remain dynamically stable under perturbation.

Let a discrete substrate contain N elementary geometric cells. Each cell possesses finite occupancy:

ρ_i

with:

0 ≤ ρ_i ≤ ρ_max

and conserved total occupancy:

Σρ_i = constant

Perfect equilibrium requires identical occupancy across the substrate for all cells:

ρ_i = ρ_0

Minimum admissible redistribution:

Δρ_min > 0

Because the substrate is discrete, redistribution cannot occur continuously. Any local transition therefore satisfies:

|Δρ_i| ≥ Δρ_min

Conservation requires compensating redistribution:

ΣΔρ_i = 0

Exact restoration of the original uniform state would require compensating variations satisfying:

|Δρ_i| < Δρ_min

Which is forbidden by finite geometric resolution:

Δρ_min > 0

Therefore, exact uniformity cannot be dynamically restored after perturbation, as residual gradients necessarily emerge for some neighboring cells:

ρ_i - ρ_j ≠ 0

In a finite discrete geometry, any admissible perturbation necessarily generates nonlocal redistribution. Because redistribution occurs through finite transitions, exact restoration becomes impossible and residual geometric gradients propagate through the substrate.

Motion therefore emerges as a persistent relaxation process of discrete geometric imbalance.

## 10. Unified dynamics

### 10.1. Geometric intensity

The model reveals that gravitation and electrostatics are not distinct forces, but symmetric projections of the same geometric interaction. The distinction arises solely from how the object scales relative to the equilibrium mass (m_z).

The mass ratio (µ) is defined as the object's mass normalized to the equilibrium pivot:

µ = m / m_z

Geometric intensity (Ψ) is defined as the sum of the volumetric projection and the superficial projection of an object:

Ψ = (m / m_z) + (|n| · m_z / m)

Unlike the acceleration formulation, Ψ is defined as a dimensionless geometric occupancy variable normalized linearly to the equilibrium scale m_z.

This dimensionless magnitude captures the complete geometric nature of the object:

* For macroscopic bodies (µ ≫ 1), the volumetric term dominates:
 
Ψ ~ µ

* For elementary particles (µ ≪ 1), the superficial term dominates:
 
Ψ ~ 1 / µ

### 10.2. Linear saturation limit

Space is not an infinite container; it has a linear structural limit determined by the speed of light (c) and the structural constant (w = 2).

λ_z is defined as the linear saturation length of m_z. It represents the minimum pixel of interaction per unit of geometric intensity:

λ_z = (w · U) / (m_z · c^2)

λ_z = (w · α · ħ · c) / (√α · m_P · c^2)

λ_z = 2 · l_P · √α

λ_z ≈ 2.761357 × 10^(-36) m

### 10.3. Unified equation of intrinsic acceleration

Intrinsic acceleration (a_i) is defined as the flow of the geometric intensity through the available spatial metric.

The baseline is the reference acceleration (a_z) generated by the equilibrium mass:

a_z = U / (r^2 · m_z)

The total geometric length is defined as the linear projection of the object's geometric intensity onto the spatial metric:

L_t = λ_z · Ψ

The object projects its geometric length onto the radius. As this length becomes significant relative to r, the available space for interaction saturates following the geometric square-root constraint.

The unified equation of intrinsic acceleration is defined as:

a_i = (U · Ψ / (m_z · r^2)) / √(1 - L_t / r)

This single equation describes the dynamics of any object in the universe without free parameters.

Unlike standard models where G is an empirical input, the geometric model defines G as a derived hybrid term:

G = U / z

Since U is fixed by definition:

U = α · ħ · c

the strength of the gravitational coupling is constrained by α and c. Any attempt to fit the curve to data is impossible because the interaction intensity is locked by these fundamental constants. The equation does not describe a force plus a correction, but a single geometric projection that yields the Schwarzschild limit and the Coulomb limit as asymptotic extremes of the same saturation curve.

#### 10.3.1. Recovery of Newton's law

When m ≫ m_z, the volumetric term dominates the geometric intensity:

Ψ ~ m / m_z

Since r is much larger than L_t, the saturation factor approaches unity:

1 - L_t / r → 1

√(1 - L_t / r) → 1

The unified equation of intrinsic acceleration simplifies to:

a_i = (U · (m / m_z) / (m_z · r^2)) / 1

a_i = (U / m_z^2) · (m / r^2)

a_i = G · m / r^2

The interaction force (F_g) acting on a test mass is recovered from the inertial relation:

F_g = m · a_i

F_g = G · m^2 / r^2

#### 10.3.2. Coulomb's law

When m ≪ m_z, the surface term dominates the geometric intensity for a minimal non-neutral topology (|n| = 1):

Ψ ~ m_z / m

The radius remains large compared to the projected geometric length:

1 - L_t / r → 1

√(1 - L_t / r) → 1

The unified equation of intrinsic acceleration simplifies to:

a_i = (U · (m_z / m) / (m_z · r^2)) / 1

a_i = U / (m · r^2)

The interaction force (F_e) acting on a test mass is recovered from the inertial relation:

F_e = m · a_i

F_e = U / r^2

#### 10.3.3. General relativity

As the object's density increases, the projected geometric length L_t approaches the available physical distance r. When the available metric space for interaction saturates, the denominator tends to zero, and intrinsic acceleration diverges at the boundary:

1 - L_t / r → 0

√(1 - L_t / r) → 0

Solving for the saturation limit where the denominator cancels out:

r_S = L_t

Since the total geometric projection is constrained by the structural constant w = 2:

L_t = w · G · m / c^2

Evaluating the relation yields the saturation radius:

r_S = 2 · G · m / c^2

This yields the Schwarzschild event horizon as an absolute geometric saturation limit without requiring a point-mass singularity at r = 0.

### 10.4. Ontological collapse of the unified equation

The complex algebraic structure of the unified intrinsic acceleration derived previously is not a fundamental feature, but rather a mechanical expansion. By applying the principle of geometric shielding, the equation collapses into a simple and direct ontological statement.

Dividing both the numerator and the denominator of the unified equation by the normalization factor (m_z · c^2 · r^2) inside the square-root metric operator yields:

a_i = [(U · Ψ) / (m_z · r^2)] / √[((m_z · c^2 · r^2) - (w · U · r · Ψ)) / (m_z · c^2 · r^2)]

The numerator represents the raw, unconstrained acceleration field:

a_raw = (U · Ψ) / (m_z · r^2)

By defining the baseline reference acceleration as a_z = U / (r^2 · m_z), the numerator is expressed as:

a_raw = a_z · Ψ

Applying the normalization division to the internal terms of the denominator square root yields:

1 - (w · U · Ψ) / (m_z · c^2 · r)

The subtracted fraction, (w · U · Ψ) / (m_z · c^2), possesses units of length and defines the projected geometric length L_t, which dictates the total structural projection of the object onto the spatial metric. Thus, the denominator represents the geometric square root of the dimensionless fraction of unsaturated metric space still available for interaction:

√(1 - L_t / r)

By substituting these emergent topological meanings back into the initial ratio, the unified equation of intrinsic acceleration collapses into:

a_i = (a_z · Ψ) / √(1 - L_t / r)

This topological reduction reveals the underlying ontology of the geometric model. The interaction is not interpreted as a force propagating through an inert background, but as the ratio between the unconstrained geometric intensity and the square root of the remaining unsaturated spatial metric available to accommodate its projection.

#### 10.4.1. Geometric saturation function

The unified acceleration equation can be rewritten in terms of a single dimensionless saturation function that measures the metric capacity remaining available for geometric propagation under square-root confinement.

The total geometric length projected onto the metric is:

L_t = λ_z · Ψ

The corresponding saturation function is defined as:

Σ(r, Ψ) = 1 / √(1 - L_t / r)

The quantity Σ represents the non-linear geometric amplification generated by finite metric occupancy.

When the projected geometric length remains much smaller than the available radius:

L_t / r → 0

the saturation function approaches unity:

Σ → 1

and the interaction reduces to the unsaturated geometric regime.

As the projected geometric length increases, the available metric capacity decreases and the geometric response becomes progressively amplified by the metric deformation.

The unified intrinsic acceleration is written in the compact form:

a_i = a_z · Ψ · Σ(r, Ψ)

where:

a_z = U / (r^2 · m_z)

The variable Ψ describes the unconstrained distribution of geometric intensity, while Σ(r, Ψ) describes the finite occupancy state of the metric.

The saturation function generates multiple asymptotic physical regimes without modifying the underlying propagation law.

For weak occupancy states where L_t / r ≪ 1, the geometric amplification function Σ is expanded using a generalized binomial series expansion:

Σ = 1 + (1 / 2) · (L_t / r) + (3 / 8) · (L_t / r)^2 + (5 / 16) · (L_t / r)^3 + ...

The first correction term produces the weak-field relativistic perturbation field. Evaluating this correction for a neutral macroscopic mass where Ψ = m / m_z and L_t = 2 · G · m / c^2 yields the incremental acceleration component:

Δa = a_z · Ψ · (1 / 2) · (L_t / r)

Δa = (U / (r^2 · m_z)) · (m / m_z) · (1 / 2) · (2 · G · m / (c^2 · r))

Δa = (U / m_z^2) · (m / r^2) · (G · m / (c^2 · r))

Since G = U / m_z^2, the first-order metric correction simplifies to:

Δa = (G · m / r^2) · (G · m / (c^2 · r))

Δa = G^2 · m^2 / (c^2 · r^3)

This first-order term modifies the effective potential landscape of the system. Under a standard orbital differential analysis using the radial coordinate u = 1 / r, this precise metric scaling factor generates a non-linear perturbation term proportional to 3 · G^2 · m^2 / (c^2 · r^3) within the orbital differential equations. This reproduces the weak-field relativistic perturbation structure, yielding the anomalous pericenter advance of planetary bodies.

When the projected geometric length approaches the available radius:

L_t → r

the remaining metric capacity tends to zero:

1 - L_t / r → 0

and the geometric amplification diverges asymmetrically:

Σ → ∞

This limit defines the saturation boundary of the metric and naturally generates the Schwarzschild condition previously obtained from the unified equation.

Within this interpretation, Newtonian gravitation, electrostatic interaction, relativistic amplification, and horizon formation correspond to different occupancy states of the same geometric saturation function.

The geometric model reduces the apparent diversity of interaction regimes to a single metric occupancy principle governed by Σ(r, Ψ).

The framework separates physical interaction into two independent geometric mechanisms. The geometric intensity operator Ψ determines how structural density is distributed, while the saturation function Σ(r, Ψ) determines how the finite occupancy of the metric amplifies that response.

### 10.5. Force formulation and strong-field simplification

The unified framework is originally formulated in terms of intrinsic acceleration:

a_i = (U · Ψ / (m_z · r^2)) / √(1 - L_t / r)

This equation describes the geometric interaction generated by a source object of geometric intensity Ψ at distance r. Although the formulation is written in terms of intrinsic acceleration, any interaction may equivalently be expressed through force using Newton's definition:

F = m · a

The force formulation provides a more direct comparison with binary astrophysical systems and allows the strong-field behavior of the model to be analyzed independently of any particular interpretation of intrinsic acceleration.

Multiplying the unified acceleration equation by the mass of the affected object (m_2) yields the complete unified interaction before any weak-field approximation is introduced:

F_u = m_2 · (U · Ψ / (m_z · r^2)) / √(1 - L_t / r)

For a neutral macroscopic source object (m_1), the topological integer is zero (|n| = 0), and the geometric intensity reduces to its volumetric projection:

Ψ = m_1 / m_z

Substituting this relation into the unified acceleration equation gives:

a_i = (U · (m_1 / m_z) / (m_z · r^2)) / √(1 - L_t / r)

a_i = (U / m_z^2) · (m_1 / r^2) / √(1 - L_t / r)

Using the derived macroscopic equivalence G = U / m_z^2 yields:

a_i = (G · m_1 / r^2) / √(1 - L_t / r)

The framework independently establishes the geometric saturation radius as:

r_S = w · G · m_1 / c^2

For a three-dimensional metric space (w = 2), this length corresponds identically to the Schwarzschild radius:

r_S = 2 · G · m_1 / c^2

Substituting r_S into the structural interaction length fixes the identity L_t = r_S. The intrinsic acceleration for neutral macroscopic bodies becomes:

a_i = (G · m_1 / r^2) / √(1 - r_S / r)

The corresponding force formulation therefore collapses into a remarkably simple relational form:

F_u = (G · m_1 · m_2 / r^2) / √(1 - r_S / r)

F_u = (G · m_1 · m_2) / (r^2 · √(1 - r_S / r))

This simplification reveals that the strong-field behavior of the model is governed entirely by the ratio r_S / r.

The interaction is dictated directly by the degree of geometric saturation of the available metric under square-root confinement.

In the weak-field limit, when the physical distance is much larger than the saturation radius (r ≫ r_S), the geometric correction factor approaches unity:

1 - r_S / r → 1

√(1 - r_S / r) → 1

Under this condition, the equation recovers the classical asymptotic limit:

F_u ≈ (G · m_1 · m_2) / r^2

As the physical distance approaches the saturation radius (r → r_S), the remaining metric capacity inside the square root tends to zero, the denominator tends to zero, and the interaction diverges algebraically. This result shows that the event horizon saturation boundary and the Newtonian inverse-square law emerge naturally as the asymptotic extremes of a single continuous geometric function, without introducing additional mathematical assumptions or free parameters.

## 11. Informational ontology of the spatial metric

The unified geometric framework naturally admits an informational interpretation of physical propagation. Within this model, physical objects are not interpreted as independent entities moving through an inert background, but as coherent topological projections maintained across a discrete spatial metric. Physical displacement therefore requires continuous geometric updating of the object's spatial projection as it propagates through the lattice.

### 11.1. Principle of geometric coherence cost

Mass is not fundamentally understood as a primitive quantity of matter, but as an emergent measure of the geometric coherence cost required to maintain a stable volumetric projection during propagation. The unified geometric response function:

T_3(r) = r + r^(-5)

can therefore be reinterpreted as an effective coherence cost function governing spatial propagation through the metric.

1. In the macroscopic regime (r ≫ λ), the object possesses a functional internal volume capable of cooperatively redistributing radial attenuation across the available spatial degrees of freedom. The geometric state remains highly compressible, and coherent propagation requires only weak incremental geometric updating as the object moves through the lattice. This regime corresponds to gravitation.

2. In the microscopic regime (r → λ), the volumetric redistribution of radial attenuation collapses near the geometric penetration scale λ. The spatial projection progressively loses its cooperative redistribution capacity, and coherent propagation becomes dimensionally amplified across the exposed geometric boundary. Under these conditions, the geometric coherence cost increases abruptly as the characteristic scale decreases. This regime corresponds to electrostatic behavior.

The mesoscopic transition scale m_φ consequently acquires a natural informational interpretation. Rather than representing only the minimum of the intrinsic acceleration curve, m_φ is interpreted as the unique point of minimal geometric coherence cost, where volumetric redistribution and dimensional amplification reach equilibrium. The condition:

dT_3 / dR = 0

defines the point of maximal propagation efficiency across the spatial metric. Within this interpretation, inertia emerges naturally as the resistance associated with increasing the rate of coherent geometric updating required for propagation through the lattice. 

The geometric action:

S_g = ∫ C_s · dl

is consequently interpreted as the cumulative coherence cost associated with maintaining a propagating geometric state across the spatial metric.

### 11.2. Geometric attenuation of quantum indeterminacy

The informational interpretation of geometric coherence cost suggests a natural geometric explanation for the phenomenon traditionally described by the uncertainty principle. Within the present framework, quantum indeterminacy is not interpreted as a fundamentally isolated probabilistic postulate, but as an emergent consequence of finite geometric resolution within a discrete spatial metric.

Because the spatial lattice possesses a minimum elementary scale:

ℓ = 2 · l_P

the propagation of any physical structure necessarily occurs over a finite-resolution geometric substrate. Perfectly continuous localization therefore becomes geometrically undefined below the resolution scale of the metric. The structural state of a propagating object may consequently be characterized through two complementary geometric magnitudes:

* Local spatial resolution (Δ_R): The degree to which the spatial metric can resolve the exposed geometric boundary of the object.

* Coherent propagation cost (Δ_C): The geometric coherence cost required to maintain a stable topological projection during propagation through the lattice.

These two quantities are linked by the volumetric redistribution capacity of the object. 

In the microscopic regime (r → λ), volumetric redistribution of radial attenuation collapses. The spatial metric becomes directly exposed to the unresolved geometric boundary, maximizing local geometric resolution (Δ_R reaches its structural minimum) while simultaneously amplifying the coherence cost (Δ_C) required to maintain stable propagation.

In the macroscopic regime (r ≫ λ), the object possesses a functional internal volume capable of cooperatively redistributing radial attenuation across the available spatial degrees of freedom. This redistribution acts as a geometric smoothing mechanism, progressively attenuating the effective influence of metric discreteness on the observable structure. As a consequence, local geometric resolution decreases (Δ_R increases) while coherent propagation becomes increasingly stable and computationally inexpensive.

The unified geometric response, T_3(r) = r + r^(-5), therefore admits an additional interpretation as a scale-dependent attenuation law governing the observable manifestation of geometric indeterminacy. Under this interpretation, microscopic systems remain strongly exposed to the unresolved structure of the spatial lattice, whereas macroscopic systems become progressively insulated from it through cooperative volumetric redistribution.

The framework consequently suggests the existence of a generalized geometric uncertainty relation of the form:

Δ_R · Δ_C ≥ constant

not as an externally imposed quantum postulate, but as a natural consequence of finite geometric resolution and scale-dependent attenuation within a discrete spatial metric. Within this framework, classical determinism emerges as the large-scale limit of geometrically attenuated indeterminacy, rather than as a fundamentally separate dynamical regime.

### 11.3. Casimir scale invariance and geometric shielding collapse

The framework identifies the surface attenuation term not merely as the electrostatic regime of elementary particles, but as the fundamental geometric counterpart of the macroscopic Casimir effect.

When two macroscopic boundaries of area A are brought into close proximity at a distance d, the intervening spatial gap approaches the geometric penetration scale. Within this confined region, the spatial metric lacks the necessary volumetric degrees of freedom to cooperatively redistribute radial tension. The local volumetric shielding mechanism artificially collapses, and the constrained space between the boundaries reverts to the unshielded, dimensionally amplified surface regime.

The spatial lattice is defined by the fundamental structural pixel:

ℓ = 2 · l_P

The minimum stable geometric surface is therefore:

A_l = ℓ^2

A_l = 4 · l_P^2

A macroscopic planar boundary of area A corresponds to a discrete number of nodes:

N_nodes = A / (4 · l_P^2)

Because the unshielded cavity forces the metric to resolve structural tension across the gap, the geometric cost is defined by the finite causal resolution of the lattice.

The causal momentum p required to maintain a topological connection across distance d is:

p = ħ / d

The corresponding geometric energy per topological link is:

E_link = p · c

E_link = ħ · c / d

In a three-dimensional Euclidean cavity, the available density of topological states is geometrically constrained by the ratio between the macroscopic volume and the confinement cube:

N_states = (A · d) / d^3

N_states = A / d^2

The total geometric coherence cost (energy) required to maintain the unshielded cavity is the product of the available states and the energy per link:

E_total = N_states · E_link

E_total = (A / d^2) · (ħ · c / d)

E_total = A · ħ · c / d^3

Because the spatial metric is discrete, the observable geometric tension emerges from the difference between the sum over discrete cavity modes and the continuous integral of unconfined space.

Applying the Euler-Maclaurin summation formula to the discrete spectral modes of the confined lattice yields the residual geometric energy density generated by the mismatch between the discrete cavity spectrum and the continuous unconfined metric:

ΔE / A = -π^2 · ħ · c / (720 · d^3)

ΔE = -π^2 · A · ħ · c / (720 · d^3)

The macroscopic interaction force F_C generated by this structural cost is the negative geometric gradient with respect to distance:

F_C = -∂(ΔE) / ∂d

∂(ΔE) / ∂d = 3 · π^2 · A · ħ · c / (720 · d^4)

∂(ΔE) / ∂d = π^2 · A · ħ · c / (240 · d^4)

F_C = -π^2 · A · ħ · c / (240 · d^4)

The negative sign denotes the geometric attraction. 

This derivation recovers the empirical Casimir force without invoking virtual particles or quantum vacuum fluctuations.

The interaction represents the mechanical consequence of the metric driving the boundaries together to eliminate the high-tension structural constraint and restore cooperative volumetric shielding.

#### 11.3.1. Numerical validation

The exactitude of the geometric derivation may be validated using standard empirical parameters.

For a planar cavity of area A and distance d:

A = 1 × 10^(-4) m^2

d = 1 × 10^(-6) m

c = 299792458 m / s

ħ = 1.0545718 × 10^(-34) J · s

Substituting these values into the derived geometric force magnitude equation:

F_C = (π^2 · 1 × 10^(-4) · 1.0545718 × 10^(-34) · 299792458) / (240 · (1 × 10^(-6))^4)

F_C ≈ 1.30008 × 10^(-7) N

This numerical output matches the experimental measurements of the macroscopic Casimir force.

The structural tension of the discrete metric therefore accounts entirely for the observed phenomenon.

### 11.4. Kinematic geometric rigidification and shear-thickening metamaterials

The informational ontology of the spatial metric provides a fundamental explanation for the macroscopic phenomenon of non-Newtonian shear-thickening fluids. In standard fluid dynamics, the sudden rigidification of these materials under impact is attributed to microscopic particle jamming and mechanical friction. The geometric framework reinterprets this phenomenon as a macroscopic manifestation of causal update latency and the dynamic collapse of volumetric shielding.

The capacity of a macroscopic material to exhibit fluid deformation relies on its ability to cooperatively redistribute geometric strain across its internal volumetric degrees of freedom. As established previously, physical displacement is not a continuous slide through a passive void, but the sequential resolution of topological orthogonal constraints (hypotenuses) across the discrete causal graph.

This continuous geometric updating requires a finite causal transition time. Let τ_v represent the characteristic volumetric relaxation time of the local metric configuration, which defines the maximum rate at which the causal graph can cooperatively compute and redistribute geometric cost across the volume. 

When an external kinetic interaction imposes a geometric displacement at a temporal rate τ_i, the stability of the volumetric shielding depends entirely on the interaction ratio:

R_τ = τ_v / τ_i

If the interaction is slow and continuous:

τ_i ≫ τ_v

the metric possesses sufficient causal cycles to compute the necessary orthogonal hypotenuses required for fluid displacement. The structural cost of the intrusion is successfully redistributed across the volumetric bulk, maintaining the classical volumetric dominance (Ψ_v). The space accommodates the topological projection, and the material flows.

However, if the kinetic interaction is impulsive:

τ_i < τ_v

the external geometric demand exceeds the maximum informational bandwidth of the local causal graph. The spatial metric cannot update the volumetric projection rapidly enough to accommodate the intrusion. Because the required orthogonal hypotenuses cannot be computed and redistributed within the available causal window, the volumetric shielding collapses instantaneously at the interaction boundary.

Unable to transfer the geometric strain into the bulk, the local spatial metric is forced to resolve the applied kinetic tension directly across the unshielded boundary. The interaction transitions abruptly into the structural surface regime:

Ψ_s ≫ Ψ_v

In this dimensionally amplified state, the boundary of the fluid acts topologically as an unshielded two-dimensional surface. It exhibits the rigid topological yield strength characteristic of a solid lattice, arresting the intrusion. The substance acts as a momentary geometric metamaterial, rigidified not by static chemical bonds, but by the kinematic exhaustion of the local metric update rate.

Once the impulsive kinetic energy dissipates and the geometric displacement rate drops below the causal relaxation threshold (τ_i > τ_v), the ability of the graph to compute the volumetric hypotenuses is restored. Volumetric shielding spontaneously recovers, the structural tension dilutes, and fluid behavior resumes.

Apparent mechanical states, such as fluidity and rigidity, are not exclusively intrinsic material properties. They are dynamic, rate-dependent emergent responses governed by the computational latency of the discrete spatial metric reacting to structural geometric demands.

#### 11.5. Topological exclusion and the geometric generalization of solid states

The dynamic response of shear-thickening fluids provides the conceptual foundation for a complete geometric generalization of solid matter. Within the framework, the boundary between fluid and solid states is not an absolute ontological distinction, but a continuous spectrum governed by the volumetric relaxation time (τ_v) of the spatial metric.

A solid object corresponds to a geometric configuration where the topological closure is highly stabilized, resulting in an exceptionally large volumetric relaxation time. When an external object attempts to penetrate a solid boundary at human timescales (τ_i ≪ τ_v), the metric cannot compute the necessary orthogonal hypotenuses to accommodate the overlapping geometric intensities. 

If the metric were to allow instantaneous penetration, multiple topological defects would be forced into the same discrete causal nodes, causing the local structural tension to exceed the absolute saturation boundary (F_max) and creating a causal incoherence. To prevent this topological paradox, the metric instantaneously halts volumetric redistribution and diverges into the structural surface regime (Ψ_s → ∞). The perceived "solidity" of a macroscopic object is therefore the manifestation of the metric enforcing geometric exclusion to prevent super-Planckian structural collapse.

However, because this solidity is a rate-dependent dynamic state (R_τ = τ_v / τ_i) rather than an absolute property, the framework predicts that all solid matter must yield if given sufficient causal time. If the applied geometric pressure is maintained over a timescale exceeding the intrinsic relaxation threshold (τ_i > τ_v), the discrete causal graph acquires sufficient sequential update cycles to compute the orthogonal hypotenuses and redistribute the geometric cost. Under these asymptotic conditions, the structural surface constraint dissolves, volumetric shielding is restored, and the solid matrix plastically flows to accommodate the intrusion.

### 11.6. Geometric latency and the dichotomy of static and kinetic friction

The computational latency of the spatial metric provides a fundamental geometric mechanism for the classical dichotomy between static and kinetic friction. In standard mechanics, this difference is phenomenologically attributed to microscopic surface asperities and electromagnetic cold-welding. The geometric framework reinterprets friction not as a mechanical surface defect, but as the scale-dependent manifestation of topological boundary fusion governed by the causal update rate.

When two macroscopic solid surfaces are brought into static contact, the relative interaction velocity is zero. The displacement timescale (τ_i) becomes effectively infinite relative to the causal update latency of the local metric (τ_c). Given this vast surplus of computational cycles, the spatial metric successfully resolves the structural discontinuities between the two surfaces. The discrete causal graph computes the necessary orthogonal hypotenuses to bridge the boundary, effectively merging the two independent projections into a single, continuous volumetric shield. 

The high value of static friction represents the substantial geometric coherence cost required to violently fracture this newly established topological fusion. To initiate movement, an external interaction must input sufficient energy to overwhelm the combined volumetric stability of the merged boundaries.

Conversely, once relative macroscopic motion is initiated, the dynamic regime shifts. The surfaces slide past one another at a displacement rate (τ_i) that is significantly faster than the metric's capacity to compute and establish stable cross-boundary topological connections (τ_c). Because τ_i < τ_c, the universe lacks the necessary informational bandwidth to fuse the adjacent nodes before they geometrically decouple and shift to the next metric coordinate. 

Consequently, during kinetic sliding, the two objects remain topologically isolated. The spatial metric is never given sufficient time to compute the structural hypotenuses that would anchor them together. Kinetic friction is therefore strictly lower than static friction because the moving system only pays the transient geometric cost of brushing past unlinked topological boundaries, rather than the massive structural cost required to fracture a fully fused volumetric shield.

## 12. Geometric unification

### 12.1. Planck units

F_u can be expressed in Planck units, with normalized constants:

c = ħ = m_P = 1

m_z^2 = α

z = α

F_u = (1 / r^2) · (m_1 · m_2 + m_z^2 · s)

Even in this regime, the term s still appears scaled by α, indicating that Planck units do not achieve full geometrization of the interaction.

### 12.2. Geometric natural units

This system normalizes the physical magnitudes to a geometry-based metric:

* Mass:
 
m_z = 1

This normalization absorbs the mesoscopic structural transition scale into the geometric unit system, implying:

m_z^2 = 1

so that the structural interaction term becomes dimensionless.

* Velocity:
 
c = 1

Primitive geometric action scale:

ħ · c / m_P^2 = 1

Consequently, the scale factor z becomes unity:

z = m_z^2 = 1

and the gravitational constant becomes a dimensionless identity:

G = 1

Therefore, α disappears from the unified equation as it is absorbed into the definition of the geometric units:

F_u = (1 / r^2) · (m_1 · m_2 + m_z^2 · s)

Under this normalization, the primitive interaction equation reduces to:

F_u = (1 / r^2) · (m_1 · m_2 + s)

In terms of intrinsic acceleration:

a_i = (1 / r^2) · (m + |n| / m)

### 12.3. Geometric definitions

The dimensional analysis reveals that all physical interactions can be expressed in terms of length (L). In this framework, physical properties transform into linear projections:

* Gravitational length (L_g) is the linear projection of mass. It corresponds to the Schwarzschild radius (r_S):

L_g = w · G · m / c^2

* Electrostatic length (L_e) is the geometric equivalent of the charge surface. It corresponds to the projection of the linear geometric cost (α) scaled by |n|:

L_e = (m_z^2 / m_P^2) · |n|

which corresponds identically to α · |n| under SI normalization.

* Total interaction length (L_t) is the superposition of both projections:

L_t = L_g + L_e

The effective geometric propagation length (λ) corresponds to the structural radius obtained by de-saturating this total projection over the topological constant w = 2:

λ = L_t / w

* Intrinsic acceleration is redefined as a measure of pure curvature (K) acting over the effective propagation length, modulated by the square-root saturation of the available space:

K = (λ / r^2) / √(1 - L_t / r)

This equation eliminates any dependence on mass, charge, time, or force. It reveals that the event horizon is not a singularity of infinite density, but a topological limit where the radial distance (r) equals the total linear projection of the object (L_t). At this boundary, the denominator vanishes, indicating that the available space for interaction has been fully consumed.

#### 12.3.1. Recovery of Newton's law

For a neutral object, the electrostatic length vanishes:

L_e = 0

In a weak field where r ≫ L_g, the geometric distortion becomes negligible and the saturation factor approaches unity:

1 - L_t / r → 1

√(1 - L_t / r) → 1

The effective propagation length becomes exclusively gravitational:

λ_g = L_g / w = G · m / c^2

The curvature depends exclusively on the gravitational propagation length:

K_g = (λ_g / r^2) / 1

K_g = λ_g / r^2

This recovers Newton's law structure.

#### 12.3.2. Recovery of Coulomb's law

For an elemental object in a weak field, the gravitational length is negligible compared to the structural projection:

L_g ≪ L_e

The geometric distance remains large compared to the projection scale, driving the saturation factor to unity:

1 - L_t / r → 1

√(1 - L_t / r) → 1

The effective propagation length becomes exclusively structural:

λ_e = L_e / w

The curvature depends exclusively on the structural propagation length:

K_e = (λ_e / r^2) / 1

K_e = λ_e / r^2

This recovers Coulomb's law structure.

#### 12.3.3. Recovery of general relativity

For an object in a strong field where r approaches L_t, an asymptotic divergence in the metric curvature occurs:

1 - L_t / r → 0

√(1 - L_t / r) → 0

K → ∞

This recovers the event horizon of general relativity, generalized here as a limit of total linear occupation (L_t) rather than just mass under square-root confinement.

### 12.4. Fundamental scaling symmetry

A geometric symmetry centered on the reduced Compton wavelength (ƛ) is revealed. α acts as the scaling factor between the particle and its orbital dynamics, while w defines the topological boundaries.

The Bohr radius defines the orbital stability limit:

a_0 = ƛ_e / α

The electron radius defines the structural breakdown limit:

r_e = w · ƛ_e · α

The proton radius is independent of α and defined by the geometric constant squared:

r_p = w^2 · ƛ_p

The electron structure and the atomic orbit are inverse manifestations of the geometric imperative, mirrored around ƛ. The proton, conversely, represents a closed stable surface, defined by the dimensional constraint w^2, independent of interaction intensity.

This symmetry derives from the dual nature of geometric action. The orbital radius:

a_0 ~ α^(-1)

represents the solution for kinetic equilibrium, where the electron minimizes action by maximizing distance within the potential well. The structural radius:

r_e ~ α^1

represents the solution for geometric saturation, where the structural cost is optimized by limiting curvature. Thus, the atom and the electron are the dual roots of the same geometric constraint under opposite boundary conditions.

### 12.5. Orbital precession as geometric saturation

General relativity explains the anomalous precession of planetary orbits as a consequence of the curvature of spacetime. The geometric model explains this same phenomenon as a consequence of spatial saturation.

Intrinsic acceleration was previously derived as a measure of pure curvature (K) describing how the effective geometric length propagates through space. To obtain the kinematic acceleration (a) governing orbital motion, this curvature must be projected through the energy density of the metric (c^2):

a = K · c^2

a = ((λ / r^2) / √(1 - L_t / r)) · c^2

This equation represents a non-linear interaction. In the weak-field limit where the total geometric length is small compared to the distance:

L_t ≪ r

The square-root saturation term can be expanded using a generalized binomial series:

1 / √(1 - x) = 1 + (1 / 2) · x + (3 / 8) · x^2 + ...

Substituting this expansion into the acceleration equation:

a = (c^2 · λ / r^2) · (1 + (1 / 2) · (L_t / r) + ...)

a = (c^2 · λ / r^2) + (1 / 2) · (c^2 · λ · L_t / r^3) + ...

The first term represents the classical Newtonian acceleration. Substituting λ = G · m / c^2 yields:

a_N = c^2 · (G · m / c^2) / r^2

a_N = G · m / r^2

The second term represents the extra acceleration required to traverse the saturated space near the central mass:

Δa = (1 / 2) · (c^2 · λ · L_t / r^3)

Substituting the definitions λ = G · m / c^2 and L_t = 2 · G · m / c^2 yields explicitly:

Δa = (1 / 2) · c^2 · (G · m / c^2) · (2 · G · m / c^2) / r^3

Δa = (1 / 2) · c^2 · (2 · G^2 · m^2 / c^4) / r^3

Δa = G^2 · m^2 / (c^2 · r^3)

In standard orbital mechanics, a radial perturbative force scaling with this precise magnitude is known to introduce a non-linear correction factor within the Binet differential equation of motion. This specific scaling factor alters the effective potential geometry, introducing the extra component that generates the full relativistic prediction for the precession of Mercury.

Thus, the anomaly is identified not as independent time dilation, but as the variable saturation of the spatial metric, which forces the planet to climb a steeper geometric gradient, effectively rotating its elliptical path. Just as an optical lens curves a beam of light by increasing the refractive index of the medium, a massive object curves a trajectory by increasing the geometric saturation of the lattice. In both models, the path of least action accounts for the local distortion of the medium.

### 12.6. Scalar weak-field relativistic structure

#### 12.6.1. Numerical validation

Weak-field relativistic corrections are evaluated through the scalar expression:

a_i = (G · m / r^2) / √(1 - r_S / r)

where:

r_S = 2 · G · m / c^2

Using the binomial expansion, this produces the leading-order structural perturbation:

a_i ≈ (G · m / r^2) · (1 + r_S / (2 · r))

a_i ≈ (G · m / r^2) + (G · m · r_S) / (2 · r^3)

Substituting the definition of r_S:

a_i ≈ (G · m / r^2) + (G · m · 2 · G · m) / (2 · c^2 · r^3)

a_i ≈ (G · m / r^2) + G^2 · m^2 / (c^2 · r^3)

This matches the expected weak-field relativistic radial scaling perturbation required to resolve the orbital dynamics of astronomical bodies.

#### 12.6.2. Solar weak-field validation

Using solar parameters:

G = 6.67430 × 10^(-11) m^3 · kg^(-1) · s^(-2)

c = 299792458 m / s

m_☉ = 1.9885 × 10^30 kg

Solar Schwarzschild radius:

r_S = 2 · G · m_☉ / c^2

r_S ≈ 2953.25 m

Mercury semi-major orbital scale:

r ≈ 5.79 × 10^10 m

Dimensionless correction factor:

1 / √(1 - r_S / r) ≈ 1 + r_S / (2 · r)

1 + r_S / (2 · r) ≈ 1 + 2.55 × 10^(-8)

Thus:

a_i ≈ a_N · (1 + 2.55 × 10^(-8))

Where a_N is the Newtonian acceleration. This correction is small, emerges naturally in the weak-field regime, and possesses the correct relativistic scaling order.

#### 12.6.3. Recovery of the relativistic perturbative structure

General relativity weak-field orbital dynamics generate perturbative corrections proportional to G · m / (c^2 · r). The geometric saturation framework generates a matching relational modifier through its square-root occupancy boundary expansion. Both frameworks produce corrections of identical dimensional structure and radial scaling, acting as a computationally efficient geometric approximation layer compatible with relativistic phenomenology in weak-field orbital systems without requiring explicit tensor propagation at runtime.

#### 12.6.4. Numerical magnitude of the correction

Newtonian acceleration at Mercury:

a_N = G · m_☉ / r^2

a_N ≈ 0.039584 m / s^2

Scalar saturation correction:

Δa = a_N · (r_S / (2 · r))

Δa ≈ 1.00947 × 10^(-9) m / s^2

This correction magnitude lies within the expected weak-field relativistic perturbation scale.

#### 12.6.5. Python implementation

To evaluate the dynamic profile of square-root metric saturation without explicit tensor propagation at runtime, the interaction is implemented inside an optimized computational kernel. The input parameters for the physical configuration are defined by the relations:

μ = G · m

r_S = 2 · G · m / c^2

The minimal runtime architecture isolates the leading-order scalar relativistic modification through five explicit floating-point operations (FLOPs), minimizing memory access overhead during systemic execution.

# =============================================================
# THE DWARF OF THE FLOPs
# Minimal runtime weak-field scalar relativistic kernel
# =============================================================

import math

def the_dwarf_of_the_flops(μ, r_S, r):

    # FLOP 1
    r2 = r * r

    # FLOP 2
    rs_over_r = r_S / r

    # FLOP 3
    metric_space = 1.0 - rs_over_r

    # FLOP 4
    denominator = math.sqrt(metric_space)

    # FLOP 5
    acceleration = (μ / r2) / denominator

    return acceleration


# =============================================================
# KERNEL EXECUTION ENVIRONMENT
# =============================================================

if __name__ == "__main__":

    # Solar parameter G · m
    μ_solar = 1.32712440018e20

    # Solar Schwarzschild radius
    rs_solar = 2953.250076

    # Mercury orbital scale
    r_mercury = 5.79e10

    # Execute runtime kernel
    a_scalar = the_dwarf_of_the_flops(μ_solar, rs_solar, r_mercury)

    # Classical baseline calculation
    a_newton = μ_solar / (r_mercury * r_mercury)

    # Isolate relativistic correction
    delta_a = a_scalar - a_newton

    print("--- RUNTIME KERNEL EXECUTION ---")
    print()
    print(f"Newtonian acceleration:    {a_newton:.12e} m/s^2")
    print(f"Scalar corrected value:    {a_scalar:.12e} m/s^2")
    print(f"Relativistic correction:   {delta_a:.12e} m/s^2")
    print()
    print("Weak-field scalar relativistic calculation executed.")

#### 12.6.6. Expected output

--- RUNTIME KERNEL EXECUTION ---

Newtonian acceleration:    3.958717460513e-02 m/s^2

Scalar corrected value:    3.958717561473e-02 m/s^2

Relativistic correction:   1.009592666412e-09 m/s^2

Weak-field scalar relativistic calculation executed.

#### 12.6.7. Final interpretation

The scalar geometric saturation model numerically reproduces:

* The Newtonian limit.

* The weak-field relativistic perturbative order.

* The correct Schwarzschild scaling structure.

* The expected small relativistic correction magnitude.

The model therefore acts as a computationally efficient geometric approximation layer compatible with relativistic phenomenology in weak-field orbital systems.

The framework suggests that weak-field relativistic phenomenology may admit a compressed scalar representation without requiring explicit tensor propagation at runtime.

## 13. Mathematical derivation of energy

### 13.1. Geometric work and metric saturation

Within the geometric framework, physical propagation is not interpreted as the displacement of a material substance through an external background, but as the sequential transfer of geometric configuration across a finite metric substrate. The metric possesses a maximum admissible structural tension, corresponding to the Planck force:

F_P = c^4 / G

This quantity represents the maximum geometric transmission capacity of the metric. Any stable physical configuration requires the propagation of structural information across an effective geometric length λ. The total energetic content associated with the configuration is therefore identified with the total geometric work required to sustain this propagation against the structural tension limit of the metric under square-root confinement.

The geometric work relation is defined as:

E = F_P · λ

This expression establishes energy as an emergent geometric quantity generated by the interaction between metric tension and effective propagation length.

### 13.2. Emergence of the geometric propagation length

The geometric model establishes that relativistic saturation appears when the structural projection of an object approaches the available metric capacity. The relativistic saturation boundary is defined by the square-root Schwarzschild condition:

√(1 - r_S / r) → 0

The saturation limit fixes the boundary at:

r_S = 2 · G · m / c^2

The factor 2 corresponds to the structural constant w = 2, which emerges from the topological relation between volumetric and surface scaling in a three-dimensional space. The effective geometric propagation length (λ) corresponds to the baseline structural radius obtained by de-saturating this projection over the topological constant:

λ = r_S / w

Evaluating the relation yields:

λ = (2 · G · m / c^2) / 2

λ = G · m / c^2

The propagation length therefore emerges directly from the relativistic saturation structure of the metric.

### 13.3. Derivation of relativistic energy

Substituting the geometric propagation length into the geometric work equation yields:

E = F_P · λ

E = (c^4 / G) · (G · m / c^2)

The geometric coupling terms cancel identically across the equation:

E = m · c^2

The relativistic energy identity therefore emerges as a consequence of finite metric tension and geometric propagation length. Mass-energy equivalence is not an independent background postulate, but the necessary energetic cost required to maintain a stable geometric configuration inside a metric substrate possessing finite structural transmissibility. Energy is therefore reinterpreted as accumulated geometric work generated by metric saturation.

### 13.4. Geometric interpretation

The derivation reveals that relativistic energy emerges from the interaction between two fundamental geometric constraints:

* Finite structural tension of the metric substrate.

* Finite propagation length associated with geometric occupancy.

The Planck force defines the maximum transmissible geometric intensity, while the propagation length defines the spatial extent required to maintain coherent structural transfer. Their product generates the energetic content associated with the geometric configuration:

E = m · c^2

Consequently, the relativistic identity represents the equilibrium relation between metric saturation capacity and geometric propagation structure. The energy of a physical system is interpreted as the total geometric work required to sustain coherent propagation inside a finite and discretized spatial metric.

## 14. Formal variational and geometric formulation

### 14.1. Geometric setting

Let (m, g_μν) be a 4-dimensional Lorentzian manifold with signature (-, +, +, +). Spacetime is metrizable but discretized below the fundamental length:

ℓ = 2 · l_P

In addition to the metric g_μν, the real scalar field Ψ(x), defined on m, represents the local geometric structural density. Ψ subsumes both volumetric and superficial contributions. No independent charge or gauge fields exist.

### 14.2. Total action

The dynamics follow from a single variational principle:

δS = 0

with:

S = S_EH + S_g + S_m

#### 14.2.1. Einstein-Hilbert sector

S_EH = (1 / (2 · κ)) · ∫ d^4x · √(-g) · r

where:

κ = (8 · π · G) / c^4

G = U / z

G is emergent, not fundamental.

#### 14.2.2. Geometric structural sector

The geometric structural sector accounts for the non-linear metric occupancy. To implement the square-root boundary saturation condition, the action density incorporates the field-dependent constraint directly into the potential scaling landscape:

S_g = -∫ d^4x · √(-g) · ((1 / 2) · g^μν · (∇_μΨ) · (∇_νΨ) + V(Ψ))

The scalar potential function is constrained by the non-linear metric occupancy function:

V(Ψ) = [A · Ψ^(1 / 3) + B · Ψ^(-5 / 3)] / √(1 - L_t / r)

with A, B > 0 uniquely determined by the primitive geometric prefactor ħ · c / m_P^2 and the mesoscopic transition scale m_z.

#### 14.2.3. Matter sector

S_m = ∫ d^4x · √(-g) · L_m(g_μν, Ψ)

All inertial and electromagnetic effects are mediated through Ψ. There is no independent electromagnetic action.

### 14.3. field equations

#### 14.3.1. Metric variation

Variation with respect to g_μν yields the modified field equations:

r_μν - (1 / 2) · r · g_μν = κ · T_μν^eff

with:

T_μν^eff = T_μν^m + T_μν^Ψ

and:

T_μν^Ψ = (∇_μΨ) · (∇_νΨ) - (1 / 2) · g_μν · g^ab · (∇_aΨ) · (∇_bΨ) - g_μν · V(Ψ)

#### 14.3.2. Scalar field equation

Variation with respect to Ψ yields the non-linear propagation envelope:

□Ψ - ∂V / ∂Ψ = J_m

The spatial variation of the potential function incorporates the geometric feedback term generated by the square-root metric saturation boundary, encoding the intrinsic acceleration profile directly into the metric landscape.

### 14.4. Curvature saturation

The discrete geometry imposes a maximum admissible curvature:

r ≤ r_max

r_max ≈ 1 / ℓ^2 = 1 / (2 · l_P)^2

Configurations exceeding this bound are excluded from the configuration space. Schwarzschild radii correspond to saturation boundaries, not singularities.

### 14.5. Modified geodesic equation

The trajectory x^μ(τ) of a test body satisfies:

d^2x^μ / dτ^2 + Γ^μ_νλ · (d x^ν / dτ) · (d x^λ / dτ) = f_g^μ

where:

f_g^μ = -g^μν · ∇_νΦ_g

Φ_g is the effective geometric potential induced by Ψ, including both volumetric and structural contributions. In the weak-field, static, spherically symmetric limit, the gradient simplifies to:

a_i = -∇Φ_g

a_i = ((ħ · c / (r^2 · m_P^2)) · (m + m_z^2 · |n| / m)) / √(1 - L_t / r)

Thus, Levi-Civita transport alone is insufficient for |n| ≠ 0.

### 14.6. Variational derivation of m_φ

Define the intrinsic acceleration functional:

L(m) = [α_1 · m^(1 / 3) + α_2 · m^(-5 / 3)] / √(1 - L_t / r)

Stationarity condition under weak metric occupancy where the denominator approaches unity yields:

dL / dm = 0

This simplifies to the unconstrained transition equation:

(1 / 3) · α_1 · m^(-2 / 3) = (5 / 3) · α_2 · m^(-8 / 3)

Implying:

m^2 = 5 · (α_2 / α_1)

By definition of equilibrium:

√(α_2 / α_1) = m_z

The dynamic stability factor (δ) remains invariant:

m_φ = √5 · m_z

δ = √5

The mass m_φ corresponds to the unique global minimum of the geometric action density.

### 14.7. Hamiltonian structure

Canonical momentum:

Π_Ψ = δL / δ(∂_0Ψ)

Hamiltonian density:

H = (1 / 2) · Π_Ψ^2 + (1 / 2) · g^ij · (∇_iΨ) · (∇_jΨ) + V(Ψ)

The non-polynomial square-root form of V guarantees convexity, a single global minimum, and the absence of runaway solutions. The minimum-energy configuration corresponds to m = m_φ.

### 14.8. Geometric propagation

The apparent trajectory of an object therefore represents the ordered propagation of geometric state transitions constrained by finite structural resolution and local saturation conditions.

Time is not an independent dimension governing motion. Rather, time emerges as the accumulated geometric cost required to resolve propagation through the metric substrate. The propagation process is therefore fundamentally geometric rather than mechanical.

For a local displacement step B, the total structural propagation path H is defined as:

H = √(B^2 + w^2)

Where B is the projected spatial advance, w is the fundamental structural cost and H is the total geometric propagation path.

The propagation time associated with a trajectory is:

t_u = H_t / c

Where H_t represents the accumulated geometric path along the trajectory.

Thus, physical evolution is determined not by absolute displacement, but by the geometric cost required to transfer structural information through the metric lattice.

### 14.9. Geometric propagation functional

The physical trajectory of a configuration is determined by the extremization of the accumulated geometric propagation cost.

Geometric propagation functional is defined as:

C_γ = ∫ Γ · d s

Where γ is the propagation trajectory, d s is the infinitesimal spatial segment, and Γ is the local geometric propagation cost, which depends on the structural saturation state of the metric and therefore on the geometric intensity Ψ and its spatial variation.

Γ acts as an effective scalar propagation density defined over the local metric state.

The total geometric length projected onto the metric is:

L_t = λ_z · Ψ

As L_t approaches the available radius r, the metric progressively saturates and the geometric propagation cost increases non-linearly under square-root confinement. The unified equation of intrinsic acceleration previously derived can be interpreted as the local geometric response generated by the variation of the propagation cost under finite metric availability.

The denominator represents the square root of the remaining geometric capacity available for propagation. When r tends to L_t, the available metric tends toward zero and the propagation cost diverges asymptotically following the square-root boundary limit.

#### 14.9.1. Extremal geometric trajectories

Physical trajectories are postulated to satisfy the extremal condition:

δC_γ = 0

The realized trajectory is therefore the path that minimizes or extremizes the total accumulated geometric propagation cost compatible with the local saturation state of the metric.

This principle replaces the notion of force-driven motion with geometric admissibility. Objects do not accelerate because they are mechanically pulled through space. Instead, their trajectories emerge from the optimization of structural propagation within a finite geometric substrate.

The geometric trajectory represents the dynamically admissible path of minimum structural cost. In regions of weak saturation, the propagation cost becomes approximately Euclidean and classical Newtonian trajectories emerge naturally. In regions of strong saturation, the propagation cost becomes highly non-linear, generating relativistic orbital corrections and asymptotic causal limits governed by the square-root factor.

#### 14.9.2. Weak-field asymptotic recovery

The intrinsic acceleration equation may be rewritten as:

a_i = (c^2 · λ / r^2) / √(1 - L_t / r)

For weak fields where L_t / r ≪ 1, the denominator is expanded using the generalized binomial series:

1 / √(1 - L_t / r) = 1 + (1 / 2) · (L_t / r) + (3 / 8) · (L_t / r)^2 + ...

Thus, the acceleration field expands into the series:

a_i = (c^2 · λ / r^2) · (1 + (1 / 2) · (L_t / r) + (3 / 8) · (L_t / r)^2 + ...)

a_i = (c^2 · λ / r^2) + (1 / 2) · (c^2 · λ · L_t / r^3) + ...

The first term recovers the classical Newtonian acceleration limit by substituting λ = G · m / c^2:

a_N = G · m / r^2

The second term introduces a perturbative correction scaling as 1 / r^3. Substituting λ = G · m / c^2 and L_t = 2 · G · m / c^2 yields:

Δa = G^2 · m^2 / (c^2 · r^3)

This corresponds to the characteristic weak-field relativistic orbital correction associated with perihelion precession. The geometric framework therefore reproduces relativistic orbital perturbation directly from metric saturation without explicit tensor propagation.

#### 14.9.3. Photon propagation and geometric refraction

For photons (m = 0), the additional structural cost vanishes:

H = 1

and propagation occurs at the maximal admissible velocity v = c. However, although photons possess no intrinsic structural cost, they still propagate through regions of variable geometric saturation.

Spatial gradients of Ψ modify the local geometric propagation conditions of the metric substrate:

∇Ψ ≠ 0

Consequently, photon trajectories are not curved because space mechanically bends them, but because the propagation cost landscape becomes spatially anisotropic under the square-root saturation envelope.

The resulting phenomenon is analogous to geometric refraction. Regions of high saturation generate increased geometric propagation density, modifying the extremal propagation path followed by the photon. The trajectory curves toward regions of increased saturation while preserving the invariant propagation velocity c. Within this interpretation, gravitational lensing emerges as a consequence of geometric propagation optimization inside a non-uniform saturation field.

#### 14.9.4. Geometric interpretation

The geometric model replaces the distinction between force, curvature, and inertial motion with a single propagation principle based on finite metric occupancy.

Newtonian gravitation, relativistic saturation, orbital precession, and photon deflection emerge as asymptotic manifestations of the same geometric propagation constraint. The model suggests that physical motion is fundamentally governed not by forces acting inside spacetime, but by the optimization of structural propagation within a finite and discretized geometric substrate.

## 14.10. Emergent factorization of geometric dynamics

The unified intrinsic acceleration was previously obtained in the compact form:

a_i = (a_z · Ψ) / √(1 - L_t / r)

This expression admits a factorization into two independent geometric components. Define the saturation function under square-root confinement as:

Σ(r, Ψ) = 1 / √(1 - L_t / r)

The unified acceleration becomes:

a_i = a_z · Ψ · Σ(r, Ψ)

The geometric interaction therefore separates into two distinct mechanisms. The first component describes the unconstrained spatial distribution of geometric intensity:

a_raw = a_z · Ψ

The second component Σ(r, Ψ) = 1 / √(1 - L_t / r) describes the occupancy state of the metric. Σ quantifies the non-linear fraction of geometric amplification generated by finite metric availability.

When the projected geometric length remains negligible compared to the available radius:

L_t / r → 0

the saturation function approaches unity:

Σ → 1

and the interaction is governed exclusively by geometric intensity. As the projected geometric length increases, the available metric capacity decreases and the amplification grows under square-root warping:

Σ > 1

When the projected geometric length approaches the available radius r → L_t, the remaining metric capacity vanishes and the amplification diverges asymmetrically:

Σ → ∞

The saturation boundary therefore emerges independently of the fundamental interaction mechanism. This factorization reveals that the geometric framework is governed by two mathematically independent structures. The intensity operator determines how geometric density is projected. The saturation function determines how finite metric occupancy amplifies that response.

Newtonian gravitation, electrostatic interaction, relativistic amplification, and horizon formation are not generated by separate dynamical laws. They emerge from the interaction between geometric intensity projection and metric occupancy. The unified acceleration is interpreted as the product of an intensity operator and an occupancy operator acting on the same geometric substrate. The apparent diversity of interaction regimes is reduced to the combined action of these two geometric mechanisms.

### 14.11. Composition-dependent free fall

Because the structural term depends on geometric occupancy rather than purely baryonic mass, the framework predicts small composition-dependent deviations from the universality of free fall near the mesoscopic transition regime.

The effect should become enhanced for systems with:

* High internal surface-to-volume ratio.

* Granular mesoscopic structure.

* Non-neutral geometric occupancy states.

This should manifest as a deviation from the Strong Equivalence Principle for non-neutral bodies in high-precision torsion balance or optomechanical levitation experiments.

### 14.12. Discrete geometric response

The mesoscopic regime near m_φ provides an experimentally accessible domain where structural geometric effects may become observable beyond purely volumetric scaling.

If the structural term is fundamentally discrete, precision measurements in this regime may reveal non-continuous inertial or electrostatic responses associated with an underlying geometric quantization scale.

## 16. Effective mass and asymptotic consistency of the geometric field

### 16.1. Scale-dependent geometric acceleration

The geometric framework establishes that the ħ · c product constitutes the absolute causal action limit of the discrete metric. Consequently, α is isolated not as a dispensable artifact, but as the fundamental dimensionless topological invariant defining the interaction strength. The scale-dependent properties of physical mass may therefore be reformulated directly in terms of this geometric mesh configuration.

The unified intrinsic acceleration equation expressed in terms of the primitive coupling under square-root metric saturation is:

a_i = ((α · ħ · c · Ψ) / (m_z · r^2)) / √[((m_z · c^2 · r^2) - (w · α · ħ · c · r · Ψ)) / (m_z · c^2 · r^2)]

The fraction inside the square root denominator is simplified by dividing each term by the normalization factor (m_z · c^2 · r^2):

1 - (w · α · ħ · c · Ψ) / (m_z · c^2 · r)

The inverse coefficient appearing within the internal ratio corresponds to the reduced Compton wavelength associated with the mesoscopic transition scale:

ƛ_z = ħ / (m_z · c)

Substituting this geometric scale into the denominator ratio yields:

1 - w · α · Ψ · ƛ_z / r

The complete acceleration equation under square-root confinement is therefore expressed as:

a_i = ((α · ħ · c · Ψ) / (m_z · r^2)) / √(1 - w · α · Ψ · ƛ_z / r)

The geometric response field is defined as:

Ψ = Ψ_v + Ψ_s

The volumetric and structural sectors satisfy the conjugate geometric relation:

Ψ_v · Ψ_s = |n|

For elementary structural excitations satisfying |n| = 1, the volumetric and structural sectors become inverse geometric projections of the same underlying topological state:

Ψ_v · Ψ_s = 1

Macroscopic regimes satisfy Ψ_v ≫ 1 and Ψ_s ≪ 1, while localized structural regimes satisfy Ψ_v ≪ 1 and Ψ_s ≫ 1, where Ψ_v represents coherent volumetric redistribution and Ψ_s represents structural saturation. The apparent separation between gravitational and electrostatic interaction therefore emerges from the asymptotic dominance of conjugate sectors of the same geometric response field rather than from independent physical entities.

An observer interpreting the intrinsic geometric acceleration through Newtonian normalization identifies an effective scale-dependent mass:

(G · m_eff / r^2) / 1 = ((α · ħ · c · Ψ) / (m_z · r^2)) / √(1 - w · α · Ψ · ƛ_z / r)

Using the derived macroscopic equivalence G = α · ħ · c / m_z^2, isolating the effective mass yields:

m_eff = m_z · Ψ / √(1 - w · α · Ψ · ƛ_z / r)

At macroscopic interaction distances where r ≫ ƛ_z, the feedback term inside the square root becomes negligible, and the effective mass stabilizes into a linear invariant regime. At subatomic scales where r approaches the characteristic projection length, the geometric feedback term induces a non-linear rigidification of the spatial mesh. The effective mass formulation does not introduce an independent interaction sector, representing the observational reinterpretation of the intrinsic geometric acceleration field under Newtonian normalization.


### 16.2. Macroscopic asymptotic limit

In the macroscopic regime, the volumetric component of the geometric response field dominates:

Ψ_v = m / m_z

Substituting this volumetric sector into the numerator of the intrinsic acceleration equation yields the standard coupling:

(α · ħ · c · (m / m_z)) / (m_z · r^2) = (α · ħ · c · m) / (m_z^2 · r^2)

Since U = α · ħ · c and z = m_z^2, the relation simplifies to:

(U / z) · (m / r^2) = G · m / r^2

Applying the same volumetric substitution to the internal geometric feedback term of the denominator yields:

w · α · (m / m_z) · ƛ_z / r = w · α · (m / m_z) · (ħ / (m_z · c)) / r

w · (α · ħ · c · m) / (m_z^2 · c^2 · r) = w · U · m / (z · c^2 · r) = w · G · m / (c^2 · r)

The complete acceleration equation for macroscopic bodies under square-root confinement becomes:

a_i = (G · m / r^2) / √(1 - w · G · m / (c^2 · r))

Setting the geometric structural constant w = 2 corresponding to a three-dimensional metric space yields:

a_i = (G · m / r^2) / √(1 - 2 · G · m / (c^2 · r))

The denominator therefore reproduces the exact Schwarzschild metric acceleration divergence structure. In the asymptotic limit where r ≫ 2 · G · m / c^2, the relativistic square-root correction approaches unity and the equation reduces to:

a_i ≈ G · m / r^2

recovering classical Newtonian gravitation.


### 16.3. Subatomic asymptotic limit

In the subatomic regime, the structural component of the geometric response field dominates:

Ψ_s = m_z / m

The macroscopic and subatomic limits correspond to different asymptotic dominance regimes of the same underlying geometric response field. Substituting the structural sector into the intrinsic acceleration equation gives:

a_i = ((α · ħ · c · (m_z / m)) / (m_z · r^2)) / √(1 - w · α · (m_z / m) · ƛ_z / r)

a_i = (α · ħ · c / (m · r^2)) / √(1 - w · α · (m_z / m) · ƛ_z / r)

At interaction distances satisfying r ≫ w · α · Ψ_s · ƛ_z, the geometric feedback term inside the square root becomes negligible, yielding:

a_i ≈ (α · ħ · c / (m · r^2)) / 1

The corresponding interaction force acting on the mass is recovered from the relation F_e = m · a_i:

F_e ≈ α · ħ · c / r^2

recovering the Coulomb interaction magnitude in geometric form. The electrostatic regime therefore emerges as the asymptotic structural limit of the same underlying geometric interaction field.


### 16.4. Geometric interpretation

The asymptotic structure of the intrinsic acceleration equation reveals that gravitation and electrostatic interaction correspond to complementary geometric regimes of the same underlying substrate. In the macroscopic regime, coherent volumetric redistribution dominates the interaction dynamics. Radial attenuation is cooperatively distributed across the available geometric degrees of freedom, producing the weak-field gravitational limit.

In the subatomic regime, volumetric shielding collapses and the interaction becomes dominated by unresolved structural saturation. The resulting inverse scaling behavior produces the electrostatic limit. The transition between both asymptotic sectors is governed by the mesoscopic geometric scale m_z, which acts as the field boundary separating volumetric redistribution from structural amplification. The geometric model therefore interprets gravitation and electrostatic interaction not as independent physical sectors, but as complementary asymptotic responses of a unified discrete metric substrate.

## 17. Topological yield strength and origin of mass

### 17.1. Ontological shift: mass as structural strain

Standard particle physics introduces the electron mass (m_e) as an independent fundamental constant, or relies on a free parameter interacting with a background vacuum expectation value. Within the geometric model, fundamental mass cannot be an arbitrary scalar input. In a discrete causal lattice, a stable elementary particle is not a substance inserted into space, but a localized topological defect sustained by the spatial metric. Consequently, the mass of an elementary fermion must correspond to the mechanical energy required to sustain this geometric distortion. It represents the structural strain limit, defined as the topological yield strength of the discrete metric.

### 17.2. Primitive equilibrium boundary (m_z)

To derive the fundamental mass scale, the framework must first establish the baseline geometric boundary of interaction equilibrium. This scale is defined by the equilibrium mass m_z, where the volumetric and structural interaction regimes acquire equal magnitude:

m_z = m_P · √α

This macroscopic equilibrium corresponds to a specific geometric boundary. Evaluating the Compton radius associated with m_z yields:

r_z = ħ / (m_z · c)

r_z = ħ / (m_P · √α · c)

r_z = l_P / √α

The surface area of this spherical equilibrium boundary is:

A_z = 4 · π · r_z^2

A_z = (4 · π · l_P^2) / α

The causal lattice is quantized by the fundamental structural pixel ℓ = 2 · l_P, which possesses a minimum stable area:

A_ℓ = ℓ^2

A_ℓ = 4 · l_P^2

The number of discrete fundamental pixels (K_z) required to tessellate the interaction equilibrium boundary is the ratio of these areas:

K_z = A_z / A_ℓ

K_z = [(4 · π · l_P^2) / α] / (4 · l_P^2)

K_z = π / α

This shows that the constant π / α is not a phenomenological artifact, but the integer quantization of the equilibrium horizon. Any localized topological defect must distribute its structural tension across this finite discrete boundary.

### 17.3. Geometric intensity and topological saturation

The physical state of a localized defect is quantified by its geometric intensity (Ψ), a dimensionless variable measuring its structural occupancy within the lattice. For a fundamental topological defect where |n| = 1, the volumetric projection is negligible, and the geometric intensity is dominated by the structural term:

Ψ = m_z / m

The lattice, being discrete and finite in its causal capacity, cannot sustain infinite geometric intensity. There exists an absolute upper bound of geometric strain, defined as the topological yield strength Ψ_max, before the discrete metric undergoes structural saturation and permanently locks the defect into a stable state.

### 17.4. Topological origin of the electron

The electron is the lightest stable excitation of the spatial metric, representing the absolute geometric saturation limit of the discrete metric for a single unit of topological charge. When a structural defect is introduced into the lattice, the spatial metric redistributes the strain. Because a smaller mass yields a larger Compton wavelength, the discrete lattice is forced to coordinately stretch the topological tension across a vastly larger volume of geometric pixels. This topological expansion continues until the geometric intensity reaches the absolute breaking point of the lattice capacity:

Customarily, the maximum intensity is defined as:

Ψ_max = m_z / m_e

This threshold is physically equivalent to the square root of the ratio between the primary structural interaction and the volumetric attenuation limit operating on the ground-state defect:

Ψ_max = √(F_e / F_g)

Consequently, m_e is deterministically governed by the structural failure limit of the spatial mesh:

m_e = m_z / Ψ_max

The theoretical derivation of the electron mass is thus reduced to a problem of discrete structural mechanics, determining the maximum number of tensile micro-states that a spherical causal boundary composed of π / α nodes can cooperatively sustain before undergoing topological fracture.

### 17.5. Theorem of dimensional closure

The framework defines the geometric intensity (Ψ) dynamically as the ratio m_z / m_e for an elementary excitation. However, for the model to be purely geometric, this dynamical ratio must correspond to the structural projection of the discrete lattice. The macroscopic interaction area of the electron is defined in terms of discrete lattice nodes as:

A_e = 4 · π · N_e^2

where N_e = m_P / (2 · m_e) is the linear projection radius. As previously derived, the primitive interaction equilibrium boundary (m_z) is tessellated by K_z = π / α nodes. The geometric ratio (R_A) between the macroscopic projected area of the particle and the fundamental equilibrium boundary is:

R_A = A_e / K_z

R_A = (4 · π · (m_P / (2 · m_e))^2) / (π / α)

Algebraic reduction yields the clean identity:

R_A = α · m_P^2 / m_e^2

Since the equilibrium scale is defined as m_z^2 = α · m_P^2, the ratio becomes:

R_A = m_z^2 / m_e^2

R_A = Ψ_max^2

This algebraic identity shows the dimensional closure of the geometric framework. The exponent of the structural acceleration term relative to the volumetric term demands that the structural force dominates by a factor of Ψ^2. The lattice mirrors this dynamical requirement: the surface area of the topological defect dilutes the structural tension by the same factor of Ψ^2 relative to the equilibrium base.

### 17.6. Rejection of the Yukawa parameterization

In the Standard Model of particle physics, the mass of elementary fermions is introduced phenomenologically through the Yukawa coupling, a free parameter representing the interaction strength between the particle and the background Higgs field. This formulation treats mass as an arbitrary property assigned externally to a point particle residing in a continuous vacuum. The geometric model rejects this parameterization. By showing that the electron mass fundamentally corresponds to the topological yield strength (Ψ_max) of the discrete metric, the model eliminates the necessity of an external background field to generate fermion inertia. The electron is interpreted as the fundamental failure limit of the spatial metric itself. Consequently, the mass of the electron cannot be tuned arbitrarily, as it is locked to the structural capacity of the causal graph. The uncertainty principle emerges deterministically as the pixelation noise generated when continuous macroscopic variables are mapped onto the indivisible fundamental transitions of this discrete metric. The framework shows that quantum mechanics acts as an effective macroscopic theory of fluids, capturing the statistical behavior of topological defects while remaining blind to the underlying discrete geometry of the causal lattice.

### 17.7. Requirement for a macroscopic geometric boundary

While the algebraic identity establishes the geometric consistency of the model, calculating Ψ_max through the empirical mass of the electron constitutes a circular definition. For the geometric model to definitively supersede parameterized models, the topological yield strength of the metric (Ψ_max) must be derived ab initio. However, this combinatorial boundary condition cannot be resolved by analyzing the micro-scale in isolation. If the electron represents the absolute structural saturation of the discrete metric, its maximum admissible intensity must be constrained by the total available capacity of the space it occupies. The ultimate geometric bound of a topological defect is not determined by local physics, but by the macroscopic limits of the causal graph in which it is embedded. Therefore, the deterministic calculation of the fundamental mass requires extending the discrete geometric formulation to its ultimate boundary, defined as the cosmological limit of the entire spatial metric.

### 17.8. Geometric shrapnel

The Standard Model catalogs a vast array of subatomic particles, classifying them as fundamental building blocks of nature. The geometric framework reinterprets this particle zoo not as an inventory of fundamental entities, but as the transient geometric shrapnel generated by the fracturing of stable topological closures.

Within a discrete three-dimensional metric, stable mass requires absolute topological closure. The fundamental states, corresponding to the macroscopic volumetric closure (the proton) and the microscopic surface saturation limit (the electron), represent the unique geometric configurations capable of infinite stability.

High-energy collider experiments do not reveal deeper fundamental particles existing passively inside these stable states. Instead, extreme energetic collisions forcefully fracture the stable volumetric closure of the causal graph. The immense interaction energy is temporarily absorbed by the spatial metric, forcing the lattice to sustain incomplete topological defects that lack stable three-dimensional closure. Because these geometric fragments cannot satisfy the topological boundary conditions required for stable mass, they appear observationally as highly unstable transient resonances. The phenomenon of particle decay is therefore reinterpreted as the deterministic geometric relaxation of the spatial metric.

The lattice rapidly dissipates the unresolved structural tension, cascading through discrete harmonic states until topological closure is restored in the form of stable ground states. Consequently, the discrete higher generations of matter and the massive intermediate bosons do not correspond to independent fundamental fields. They represent the quantized energetic cost associated with topological transformations and the step-wise dissipation of structural strain across the discrete metric.

The contemporary particle zoo is therefore an archaeological record of shattered geometric structures, mathematically patched together through parameterized couplings rather than derived from the underlying topology of space.

## 18. Cosmological limit: conformal scaling and the relational metric

The fundamental constraint of the discrete metric graph is the conservation of its total informational capacity:

N = constant

The total number of causal nodes (N) within the spatial metric is fixed as a topological invariant. Consequently, the expansion of the universe is not interpreted as the creation of new space, but as the continuous dilution of the global node density over a larger effective volume. Since mass, length, and time are not fundamental background entities but emergent properties of the causal graph, local systems do not decouple from this global expansion. As the metric density dilutes, the geometric projection of all localized topological defects recalibrates proportionally. Fundamental constants are therefore dynamic expressions of the global geometric state, adjusting continuously with the metric dilution.

Despite this universal recalibration, local physics appears static to an internal observer. Because the measuring apparatus and the observed system scale by the exact same conformal factor, local geometric ratios remain strictly invariant. Within any given cosmological epoch, empirical measurements yield stable constants and stable local orbits, effectively shielding the expansion from local mechanical detection. Cosmològical redshift is no longer interpreted as the continuous kinematic stretching of a photon propagating through an expanding empty space. A photon carries the quantized geometric intensity of the causal graph fixed at the exact epoch of its emission. Redshift emerges relationally when a photon emitted in a past, higher-density metric epoch is absorbed and measured by an apparatus existing in a present, lower-density metric epoch. The observed frequency shift is the direct measurement of the metric recalibration that occurred between the time of emission and the time of observation.

### 18.1. Topo-cosmological derivation of the fundamental mass

The mass of the fundamental stable topological defect emerges as a dynamic boundary condition constrained by the macroscopic limits of the causal graph. Since standard gravitational parameters are derived geometric relations within this framework where G = U / z, the spatial metric resolution is defined by the fundamental quantum constants and the structural equilibrium mass constant (z). Substituting the derived geometric equivalent of the Newtonian constant into the Planck length definition yields the direct topological representation of the fundamental spatial pixel (ℓ):

ℓ = 2 · √((ħ · ((α · ħ · c) / z)) / c^3)

ℓ = 2 · √((α · ħ^2 · c) / (z · c^3))

ℓ = (2 · ħ · √α) / (c · √z)

This defines the minimum resolution limit of the spatial metric as the modified Compton wavelength of the equilibrium state. The electron (m_e) represents the minimal stable topological defect where |n| = 1, saturating the discrete local metric at the pixel scale. The global capacity of the causal graph is dictated by its total radius (r_u). Because the graph expands volumetrically while the fundamental defect scales as a surface projection, the maximum geometric intensity the defect can sustain is constrained by the volumetric expansion ratio:

√z / m_e = (r_u / ℓ)^(1 / 3)

Solving for the fundamental mass:

m_e = √z · (ℓ / r_u)^(1 / 3)

Substituting the explicit definition of the spatial pixel (ℓ) into the boundary condition yields the unified equation for the fundamental mass:

m_e^3 = z^(3 / 2) · (ℓ / r_u)

m_e^3 = z^(3 / 2) · (((2 · ħ · √α) / (c · √z)) / r_u)

m_e^3 = (2 · z · ħ · √α) / (c · r_u)

m_e = ((2 · z · ħ · √α) / (c · r_u))^(1 / 3)

### 18.2. Dimensional determinism and uniqueness of the fundamental mass

#### 18.2.1. Absence of algebraic fine-tuning

The fundamental resolution limit of the spatial metric (ℓ) is constructed exclusively from the primitive inputs: the quantum of action (ħ), the propagation velocity (c), the structural equilibrium mass (√z), and the dimensionless topological invariant (α). According to the Buckingham π theorem, dimensional homogeneity restricts the possible algebraic combinations of these variables. To yield a physical length (L), the variables must satisfy:

[L] = [ħ]^a · [c]^b · [√z]^d

The fundamental dimensions balance according to the system:

M: a + d = 0

T: -a - b = 0

L: 2a + b = 1

Solving this system yields a unique, mathematically unavoidable solution: a = 1, b = -1, d = -1. Therefore, the only dimensionally admissible algebraic core for the metric resolution limit is the modified Compton wavelength:

ℓ ∝ ħ / (c · √z)

#### 18.2.2. Topological lock of the dimensionless modifier

While dimensional analysis fixes the algebraic core, a phenomenological model might still introduce arbitrary dimensionless modifiers to artificially align predictions with experimental values. However, the dimensionless modifier is axiomatically locked by the topological constraints of the three-dimensional metric established prior to any cosmological considerations. As defined by the fundamental spatial pixel relation, the boundary condition for stable three-dimensional geometric capacity requires:

ℓ = w · l_P

where the geometric constant w = 2 acts as the structural scaling limit between volumetric and surface topologies. By substituting the non-circular geometric equivalent of the Planck length, the exact coefficient emerges deterministically:

ℓ = 2 · √α · (ħ / (c · √z))

The framework contains zero algebraic degrees of freedom. The fundamental mass equation cannot be manipulated or fine-tuned:

m_e = ((2 · z · ħ · √α) / (c · r_u))^(1 / 3)

The exponent (1 / 3) is locked by the volumetric scaling prerequisite for Newtonian gravitation, and the coefficient is locked by the fundamental structural limit (w = 2).

#### 18.2.3. Conclusion on the cosmological derivation

Because the equation is dimensionally unique and topologically locked, the emergence of the exact order of magnitude for the electron mass (10^(-31) kg) from the required cosmological inflation radius (10^29 m) cannot be attributed to combinatorial numerology. It constitutes a deterministic, parameter-free geometric prediction, showing that the mass of elementary topological defects is fundamentally dictated by the total metric capacity of the causal graph.

### 18.3. Derivation of the gravitational constant

Standard physical models treat the gravitational constant (G) as an empirically determined primitive parameter. Within the geometric framework, gravitation was previously shown to emerge from the relation G = U / z. However, relying exclusively on the definition z = α · m_P^2 introduces a circular dependency, as m_P itself is classically derived from the empirical measurement of G.

The topo-cosmological derivation of the fundamental mass breaks this circularity. The boundary condition establishing the electron mass from the macroscopic radius of the causal graph yields:

m_e = ((2 · z · ħ · √α) / (c · r_u))^(1 / 3)

By isolating the structural equilibrium scale (z), the equation becomes:

m_e^3 = (2 · z · ħ · √α) / (c · r_u)

z = (m_e^3 · c · r_u) / (2 · ħ · √α)

Substituting this purely cosmological definition of z into the unified macroscopic gravitational coupling G = U / z, where U = α · ħ · c, yields:

G = (α · ħ · c) / ((m_e^3 · c · r_u) / (2 · ħ · √α))

The propagation velocity (c) cancels out algebraically, reducing the expression to a fundamental topological identity:

G = (2 · α^(3 / 2) · ħ^2) / (m_e^3 · r_u)

This equation represents a closed derivation of the gravitational constant. m_P is eliminated from the mechanical foundation. The macroscopic intensity of gravity (G) is deterministically generated by the dimensionless topological invariant (α), the discrete quantum of action (ħ), the structural yield strength of the metric (m_e), and the total geometric capacity of the causal graph (r_u).

This algebraic closure formally mathematicalizes Mach's principle within a discrete metric. Local gravitational coupling is not an independent constant of nature, but an emergent relational property directly dictated by the global cosmological volume and the fundamental particle boundary limit. Substituting the previously derived causal radius r_u = 2.748305 × 10^29 m along with the fundamental values for m_e, α, and ħ returns the exact empirical value of G:

G = 6.67430 × 10^(-11) m^3 · kg^(-1) · s^(-2)

This confirms the absolute dimensional and numerical consistency of the geometric framework.

### 18.4. Emergence of Planck units

The Planck length (l_P) is conventionally treated as a fundamental physical constant derived from the gravitational constant (G). Within the geometric model, this interpretation is inverted. The Planck scale is not a primitive input, but an emergent projection of the global causal graph capacity. By substituting the derived relation G = (2 · α^(3 / 2) · ħ^2) / (m_e^3 · r_u) into the classical definition of the Planck length l_P = √(ħ · G / c^3), the fundamental length scale is reformulated as:

l_P = √(ħ / c^3) · √((2 · α^(3 / 2) · ħ^2) / (m_e^3 · r_u))

l_P = ħ · α^(3 / 4) / √(c · m_e^3 · r_u / 2)

This derivation shows that l_P is fundamentally constrained by the cosmological expansion of the universe (r_u) and the fundamental structural yield strength (m_e). Consequently, Planck units are not independent constants of nature, but relational snapshots of the metric state at a specific epoch of cosmological dilution. The geometric pixel ℓ = 2 · l_P acts as the resolution threshold of the metric, while the Planck length serves as the dimensional projection required to map the discrete causal graph onto the macroscopic SI coordinate system.

### 18.5. Cosmological implications and the inflationary horizon

This derivation eliminates m_e as a free parameter, establishing it as an active geometric consequence of the total causal graph size. Evaluating the equation using the CODATA recommended value for the electron mass (m_e = 9.1093837139 × 10^(-31) kg) predicts a precise total causal radius of the universe:

r_u ≈ 2.748305 × 10^29 m

This distance corresponds to approximately 29049 Gly, indicating that the complete causal graph is dynamically balanced at a radial scale roughly 624 times larger than the current observable universe horizon. This theoretical prediction aligns with standard cosmological requirements and resolves specific unconstrained parameters in contemporary astrophysics:

* Precision measurements of the cosmic microwave background indicate an extremely flat spatial curvature. For the observable universe to present such a negligible degree of curvature, the total causal volume must be orders of magnitude larger than the observable horizon.

* The thermodynamic equilibrium observed across causally disconnected regions of the cosmic microwave background requires an initial inflationary phase. While standard inflationary models necessitate this vast unobservable volume, they provide no fundamental upper bound for the final extent of the universe. The geometric model resolves this by establishing the topological boundary of the inflationary horizon, deterministically locked by the fundamental mass constraint.

* The direct detection of gravitational waves confirms that dynamic metric perturbations physically deform the spatial projection of macroscopic bodies. This provides empirical evidence that local physical dimensions are not absolute background entities, but relational properties coupled to the continuous state of the spatial metric.

The fundamental mass (m_e) acts as a topological boundary condition that restricts the maximum causal capacity of the spatial metric. This algebraic dependency requires m_e to scale over cosmological time inversely with the expansion of the universe metric, confirming a purely relational framework where no local quantity exists independently of the global geometric state. The fractional rate of mass decay is locked to the Hubble expansion parameter (H_0), scaling volumetrically:

(1 / m_e) · (d m_e / d t) = -(1 / 3) · H_0

### 18.6. Empirical phenomenology of relational mass decay

If the fundamental geometric mass scales inversely with the volumetric expansion of the causal graph, local systems cannot be perfectly decoupled from cosmological dynamics. This relational recalibration provides three mathematical pathways for empirical falsifiability.

#### 18.6.1. Secular orbital expansion anomaly

Standard gravitational mechanics predicts that isolated planetary orbits remain statically invariant under cosmological expansion. However, within the geometric framework, macroscopic orbital dynamics are governed by the conservation of total geometric action (angular momentum). For a test mass (m) orbiting a central mass (M), the classical magnitude is:

L_J = m · √(G · M · r)

Squaring the relation to isolate the physical orbital radius yields:

r = L_J^2 / (G · m^2 · M)

Assuming absolute geometric conservation of angular momentum and acknowledging that the primitive coupling G = ħ · c / m_P^2 is a topological invariant independent of metric dilution, the scaling of the orbit depends on the fundamental mass components. Since all massive bodies undergo the identical relative metric decay dictated by the fundamental mass equation, the product m^2 · M scales as m^3.

Applying the logarithmic derivative yields the absolute expansion rate of the orbital radius:

(1 / r) · (d r / d t) = -3 · ((1 / m) · (d m / d t))

Substituting the cosmological volumetric mass decay rate previously derived:

(1 / r) · (d r / d t) = -3 · (-(1 / 3) · H_0)

(1 / r) · (d r / d t) = H_0

This shows that local orbital radii undergo a physical expansion exactly matching the Hubble rate. However, to an internal observer, physical distances are evaluated relationally against local atomic measuring devices. The fundamental scale of atomic structures is determined by the Bohr radius:

a_0 = ħ / (m_e · c · α)

Since ħ, c, and α are invariant topological limits, the ruler itself expands as fundamental mass decays:

a_0 ~ m_e^(-1)

The logarithmic derivative yields the expansion rate of the atomic measuring standard:

(1 / a_0) · (d a_0 / d t) = -(1 / m_e) · (d m_e / d t) = (1 / 3) · H_0

The observable expansion (r_obs) is the ratio between the absolute orbital expansion and the expanding atomic ruler:

(1 / r_obs) · (d r_obs / d t) = H_0 - (1 / 3) · H_0

(1 / r_obs) · (d r_obs / d t) = (2 / 3) · H_0

The geometric model consequently predicts a non-zero secular expansion of local orbits equivalent to two-thirds of the Hubble rate. This differential relational expansion offers a mathematical explanation for contemporary high-precision astrometric anomalies, such as the unexplained secular increase of the Astronomical Unit (AU), without requiring unobserved mass loss from the Sun or modifications to the Newtonian limit.

#### 18.6.2. Resolution of the Hubble tension

Contemporary cosmology faces a severe crisis known as the Hubble tension, characterized by a persistent statistical discrepancy between the local measurement of H_0 using supernovae Ia (standard candles) and the early-universe derivation from the Cosmic Microwave Background.

Standard models interpret the luminosity of a supernova Ia as an absolute invariant baseline because it is triggered by the Chandrasekhar mass limit. However, the geometric model establishes that during earlier cosmological epochs, when the causal graph radius (r_u) was smaller, the fundamental topological mass m_e was proportionally larger.

Since all critical stability thresholds in degenerate matter scale with the underlying fundamental mass limits of the spatial metric, a supernova event occurring at high redshift necessarily involved a different absolute energy yield than an identical event occurring locally today. By assuming invariant mass, standard cosmological distance ladders systematically miscalculate the luminosity distances at high redshifts. When the time-varying intrinsic luminosity is properly recalibrated under the geometric relation m ~ r_u^(-1/3), the non-linear deviation is naturally resolved. The geometric model thereby provides a mechanical explanation for the Hubble tension without invoking dark energy or arbitrary modifications to general relativity.

#### 18.6.3. Quasar spectra and the invariance of α

The relational recalibration of the metric imposes a falsifiability test regarding the fine-structure constant α. Within the framework, α is explicitly defined not as a composite dynamical parameter, but as the primitive dimensionless topological invariant of the causal graph. It represents the structural fraction of the causal limit, completely independent of the volumetric expansion ratio.

Therefore, the geometric model mandates:

Δα / α = 0

When analyzing atomic absorption lines in the spectra of distant quasars originating billions of years ago, the absolute masses and radii of the emitting atoms were different due to the historical metric density. However, because atomic spectral transitions represent dimensionless ratios governed by α, the observable fine-structure spacing must remain invariant across cosmological time. This stringent topological constraint matches current high-precision empirical astrophysical surveys, supporting the relational architecture of the spatial metric.

#### 18.6.4. Ephemeris data absorption and the residual measurement discrepancy

Evaluating the relational expansion rate at the Earth-Sun semi-major scale yields a theoretical observable distance increase:

dr_obs / dt = (2 / 3) · H_0 · AU

Using a standard baseline Hubble parameter where H_0 ≈ 70 km / s / Mpc, the relative expansion factor translates to approximately 7.13 meters per year. However, high-precision empirical astrometric analyses report a significantly smaller unmodeled residual expansion of approximately 0.15 meters per year. This apparent numerical discrepancy does not invalidate the relational mechanics, but exposes a systemic data absorption effect inherent to contemporary orbital measurement frameworks.

Astronomical distance determinations do not rely on direct static measurements, but on the processing of raw radar tracking intervals and spacecraft propagation times through automated orbital simulation software. These numerical models are fundamentally hardcoded under the axiomatic assumption of invariant physical masses, static local metric parameters, and a strict unexpanding Newtonian baseline.

When the physical system undergoes the true relational expansion of 7.13 meters per year, the least-squares optimization algorithms within the ephemeris software systematically absorb the majority of this dynamic signal. The algorithm achieves numerical convergence by artificially distorting other tightly coupled orbital variables, such as initialization state vectors, orbital eccentricities, and secular planetary velocities. The reported 15 centimeters per year anomaly therefore does not represent the absolute physical expansion of the system, but rather the irreproducible geometric residual that classical static software cannot mathematically digest or eliminate through parameter tuning.

### 18.7. Geometric origin of cosmic expansion

The derivation of the differential observable expansion rate exposes an ontological inversion regarding cosmological dynamics. Standard models postulate that the universe expands due to an external dark energy acting as a negative pressure on the vacuum. The geometric framework rejects this exogenous parameterization, proposing instead that cosmological expansion is the inherent mechanical relaxation rate of the discrete causal graph.

Within the discrete spatial metric, physical stability requires the simultaneous coexistence of two conjugate topological projections:

* The volumetric (gravitational) regime, which scales with mass through the exponent 1 / 3.

* The structural (electrostatic) regime, which scales with mass through the exponent -5 / 3.

Because the fundamental spatial pixel ℓ = 2 · l_P is a rigid dimensional invariant, the discrete metric cannot absorb the differential scaling of these two regimes continuously. The geometric shear gradient (τ) generated between the volumetric bulk and the unshielded structural surface is exactly equivalent to the difference between their projection exponents:

τ = |1 / 3 - (-5 / 3)|

τ = 6 / 3

τ = 2

This mathematical identity reveals that the topological friction generated between the atomic scale and the macroscopic scale corresponds identically to the structural constant of the three-dimensional metric (w = 2). 

As topological defects interact and propagate, the mismatch between the expanding atomic ruler and the massive orbital bulk generates an ongoing topological shear pressure at the node level. If the spatial metric were completely static, this continuous geometric friction would accumulate, eventually causing the local tension of the nodes to exceed the absolute saturation boundary (F_max), leading to a collapse of the causal graph.

To maintain dynamic stability and dissipate this topological shear, the causal graph must continuously inject new volumetric capacity into the spatial lattice. The cosmological expansion of the universe is therefore interpreted as the continuous macroscopic relaxation of the microscopic topological tension. The Hubble parameter (H_0) does not represent an arbitrary velocity of space, but the precise geometric update frequency required to alleviate the structural friction w = 2 generated by the coexistence of matter and quantum geometry.

Under this relational ontology, dark energy is eliminated from the cosmological inventory. The universe does not expand because it is filled with an unknown repulsive fluid; it expands mechanically to resolve the fundamental topological conflict between volume and surface within a finite, discrete metric substrate.

### 18.8. Relational ontology of absolute scale

The derivation of the fundamental mass from the cosmological radius reveals a profound epistemological feature of the geometric framework. While the model deterministically dictates the structural ratios, scaling exponents, and geometric shape of the causal graph through dimensionless topological invariants (α and w), it remains mathematically impossible to derive the absolute dimensionful scale of the universe (r_u) without empirical observation.

The mutual dependence between r_u and m_e demonstrates that the model cannot be algebraically closed using solely dimensionless parameters. This mathematical impossibility is not a theoretical deficit, but the ultimate requirement of a background-independent ontology.

If the absolute dimensionful scale of the causal graph could be derived independently from any empirical mass, it would imply that space possesses a pre-existing, absolute metric grid that dictates physical sizes from the outside. By establishing that r_u and m_e are inextricably linked, the framework proves that absolute scale does not exist as a fundamental background property.

Dimensionful scale is entirely emergent and dynamic. The macroscopic volume of the universe represents the spatial capacity required to accommodate the structural strain of its fundamental topological defects. Consequently, anchoring the geometric equations to a single empirical measurement, such as the mass of the electron, is the necessary symmetry-breaking operation that links the invariant topological structure to the specific expansion epoch of the observer.

This mutual dependence formally mathematicalizes Mach's principle within a discrete metric. It confirms that local physical quantities have no absolute meaning independent of the global geometric state, and that the spatial lattice is not a pre-existing container, but the dynamic consequence of topological relation itself.

## 19. Directed acyclic graph of the geometric model

The geometric model operates with zero free parameters. Every physical interaction and characteristic scale emerges deterministically from a primitive topological core. The following directed acyclic graph (DAG) maps the explicit causal flow of the derivations contained within this work.

```text

[ PRIMITIVE AXIOMS ]
  |
  +-- Fundamental background scales: c, ħ, m_e, r_u
  +-- Dimensionless topological invariant (structural cost): α
  +-- Spatial dimensionality (D = 3): w = D - 1 = 2
        |
        V
[ GEOMETRIC BASE AND PIXEL RESOLUTION ]
  |
  +-- Planck length emergent: l_P = ħ · α^(3 / 4) · √(2 / (c^3 · m_e^3 · r_u))
  +-- Cosmic pixel linear scale: ℓ = w · l_P = 2 · l_P
  +-- Static crossover equilibrium mass: m_z = m_P · √α
  +-- Macroscopic primitive action scale: U = α · ħ · c
        |
        V
[ EMERGENT CONSTANTS AND PROPAGATION SCALES ]
  |
  +-- Derived gravitational coupling: G = (2 · α^(3 / 2) · ħ^2) / (m_e^3 · r_u)
  +-- Dynamic stability scaling factor: δ = √(w^2 + 1^2) = √5
  +-- Optimal mass of dynamic stability: m_φ = √5 · m_z
  +-- Effective geometric propagation length: λ = L_t / w
        |
        V
[ UNIFIED GEOMETRIC DYNAMICS ]
  |
  +-- Dimensionless geometric intensity: Ψ = (m / m_z) + (|n| · m_z / m)
  +-- Projected geometric length: L_t = λ_z · Ψ
  +-- Metric confinement saturation function: Σ = 1 / √(1 - L_t / r)
  +-- Pure metric curvature operator: K = (λ / r^2) · Σ
        |
        V
[ UNIFIED EQUATION OF INTRINSEC ACCELERATION ]
  |
  +-- a_i = K · c^2 = (a_z · Ψ) / √(1 - L_t / r)
        |
        +---> [ VOLUMETRIC BULK REGIME (m ≫ m_z, r ≫ L_t) ]
        |       +-- Classical Newtonian gravitation: a_N = G · m / r^2
        |
        +---> [ STRUCTURAL SURFACE REGIME (m ≪ m_z, r ≫ L_t) ]
        |       +-- Classical electrostatic Coulomb law: a_e = α · ħ · c / (m · r^2)
        |
        +---> [ STRONG-FIELD METRIC SATURATION REGIME ]
                +-- Horizon formation (r → L_t): Schwarzschild radius (r_S = 2 · G · m / c^2)
                +-- First-order binomial expansion: relativistic precession (Δa = G^2 · m^2 / (c^2 · r^3))
                        |
                        V
[ MACROSCOPICAL, QUANTUM, AND TOPOLOGICAL BOUNDARY CLOSURES ]
  |
  +-- Global cosmological capacity boundary (radius of the Universe: r_u)
  |     +-- Deterministic electron mass: m_e = ((2 · z · ħ · √α) / (c · r_u))^(1 / 3)
  |
  +-- Metric surface satiation counting (available node ratio: A / A_ℓ)
  |     +-- Bekenstein-Hawking black hole entropy: S = A / (4 · l_P^2)
  |
  +-- Volumetric shielding collapse under planar spatial confinement
  |     +-- Macroscopic Casimir force density: F_C = -π^2 · A · ħ · c / (240 · d^4)
  |
  +-- Finite causal resolution of conjugate graph updates (pixel noise)
  |     +-- Deterministic Heisenberg uncertainty principle: Δx · Δp ≥ ħ / 2
  |
  +-- De-saturation metric work envelope (E = F_P · λ)
        +-- Universal mass-energy equivalence: E = m · c^2
```
        
### 20. Minimal logical complexity and algorithmic information audit

```python
# =============================================================
# HUCKLEBERRY SCRIPT
# Minimal logical complexity and algorithmic information audit
# =============================================================

import math
import ast
import sys

"""
===============================================================================
ALGEBRAIC RECOVERY PROOF
===============================================================================

0. FUNDAMENTAL DEFINITIONS
   U = α * ħ * c
   m_z = √α * m_P
   s = n_1 · n_2
   n = n_p - n_e

1. COULOMB'S LAW
   a_e = (U / r**2) * (1 / m)
   F_e = m * a_e
   F_e = U / r**2
   U = k_e * e**2

2. NEWTON'S LAW
   a_g = (U / r**2) * (m / m_z**2)
   G = U / m_z**2
   a_g = G * m / r**2

3. GENERAL RELATIVITY (SCHWARZSCHILD HORIZON & WEAK-FIELD PRECESSION)
   Horizon limit: 1 - L_t / r = 0
                  r = L_t
                  L_t = 2 * (U / z) * m / c**2
                  r = r_S

4. GEOMETRIC SATURATION (SINGULARITY RESOLUTION)
   F_P = c**4 / G
   F_max = F_P * √(U / (ħ * c)) = F_P * √α
   F_max ≈ 1.03e43 N
   The classical mathematical singularity (r -> 0) is replaced
   by this maximum structural capacity in the geometric model.
===============================================================================
"""


# =============================================================================
# DYNAMIC AUDIT TOOLING
# =============================================================================

class FLOPTracker:
    """
    [note on FLOPs]: Evaluates the theoretical algorithmic density.
    Weights approximate typical CPU clock cycle costs for IEEE 754 operations:
    Add/Sub/Mul = 1, Div = 4, Sqrt = 8, Pow = 10.
    """
    flops = 0

    @classmethod
    def reset(cls):
        cls.flops = 0

    def __init__(self, value):
        self.value = float(value.value if isinstance(value, FLOPTracker) else value)

    def _op(self, other, func, weight=1):
        FLOPTracker.flops += weight
        other_val = other.value if isinstance(other, FLOPTracker) else float(other)
        return FLOPTracker(func(self.value, other_val))

    def __add__(self, other): return self._op(other, lambda a, b: a + b, weight=1)

    def __radd__(self, other): return self._op(other, lambda a, b: b + a, weight=1)

    def __sub__(self, other): return self._op(other, lambda a, b: a - b, weight=1)

    def __rsub__(self, other): return self._op(other, lambda a, b: b - a, weight=1)

    def __mul__(self, other): return self._op(other, lambda a, b: a * b, weight=1)

    def __rmul__(self, other): return self._op(other, lambda a, b: b * a, weight=1)

    def __truediv__(self, other): return self._op(other, lambda a, b: a / b, weight=4)

    def __rtruediv__(self, other): return self._op(other, lambda a, b: b / a, weight=4)

    def __pow__(self, other):
        FLOPTracker.flops += 10
        other_val = other.value if isinstance(other, FLOPTracker) else float(other)
        return FLOPTracker(pow(self.value, other_val))

    def __abs__(self):
        FLOPTracker.flops += 1
        return FLOPTracker(abs(self.value))


def tracked_sqrt(x):
    FLOPTracker.flops += 8
    val = x.value if isinstance(x, FLOPTracker) else float(x)
    return FLOPTracker(math.sqrt(val))


def tracked_max(a, b):
    FLOPTracker.flops += 1
    val_a = a.value if isinstance(a, FLOPTracker) else float(a)
    val_b = b.value if isinstance(b, FLOPTracker) else float(b)
    return FLOPTracker(max(val_a, val_b))


def tracked_min(a, b):
    FLOPTracker.flops += 1
    val_a = a.value if isinstance(a, FLOPTracker) else float(a)
    val_b = b.value if isinstance(b, FLOPTracker) else float(b)
    return FLOPTracker(min(val_a, val_b))


def calculate_cyclomatic_complexity(func_source):
    """
    Calculates strict cyclomatic complexity (CC) using Python's native AST parser.
    """
    try:
        tree = ast.parse(func_source)
    except SyntaxError:
        return 1

    cc = 1
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler, getattr(ast, 'Match', type(None)))):
            cc += 1
        elif isinstance(node, ast.BoolOp):
            cc += len(node.values) - 1

    return cc


# =============================================================================
# KERNEL SOURCES (FOR AST PARSING)
# =============================================================================

CLASSICAL_KERNEL_SRC_A = """
def classical_routing_kernel_A(self, r, mass=0, target_mass=1, q_source=0, q_target=0):
    r2 = r**2
    F_g_n = (self.G * mass * target_mass) / r2
    x = (2.0 * self.G * mass) / (self.c2 * r)
    F_g = F_g_n * (1.0 + 0.5 * x + 0.375 * x**2 + 0.3125 * x**3)
    F_e = (self.k_e * abs(q_source * q_target * self.e_charge**2)) / r2

    # CODATA threshold: The negligibility threshold is set at 45454.0.
    # This corresponds to the inverse of the relative uncertainty 
    # of the gravitational constant G established by CODATA (delta_G = 2.2e-5).
    # If a force does not exceed the other by this factor, the difference 
    # submerges within the empirical error margin.
    CODATA_THRESHOLD = 45454.0

    # Heuristic Logic: Calculate both fields blindly, discard if possible.
    if F_g > F_e * CODATA_THRESHOLD:
        return F_g / target_mass
    elif F_e > F_g * CODATA_THRESHOLD:
        return F_e / target_mass
    else:
        return (F_g + F_e) / target_mass
"""

CLASSICAL_KERNEL_SRC_B = """
def classical_routing_kernel_B(self, r, mass=0, target_mass=1, q_source=0, q_target=0):
    r2 = r**2
    F_g_n = (self.G * mass * target_mass) / r2
    x = (2.0 * self.G * mass) / (self.c2 * r)
    F_g = F_g_n * (1.0 + 0.5 * x + 0.375 * x**2 + 0.3125 * x**3)
    F_e = self.k_e * abs(q_source * q_target * self.e_charge**2) / r2
    return (F_e + F_g) / target_mass
"""

GEOMETRIC_KERNEL_SRC = """
def geometric_unified_kernel(self, r, m_source, n_source, m_target, n_target):
    r2 = r**2
    volumetric = (m_source * m_target) / self.z
    s = n_source * n_target
    F_raw = abs((self.U / r2) * (volumetric + s))
    L_t = (2.0 * (self.U / self.z) * m_source) / self.c2

    # Branchless geometric saturation (Continuous mathematical bounds)
    # Prevents horizon inversion & enforces the structural capacity of the lattice
    metric_space = tracked_max(abs(1.0 - (L_t / r)), sys.float_info.min)
    F_net = F_raw / tracked_sqrt(metric_space)

    return tracked_min(F_net, self.F_max) / m_target
"""


# =============================================================================
# ALGORITHMIC COMPRESSION AUDIT
# =============================================================================

class AlgorithmicCompressionAudit:
    def __init__(self):
        self.delta_G = 2.2e-5
        self.delta_alpha = 1.5e-10
        self.c = 299792458.0
        self.c2 = self.c ** 2
        self.k_e = 8.9875517923e9
        self.e_charge = 1.602176634e-19
        self.m_e = 9.1093837139e-31
        self.m_p = 1.67262192595e-27

        self.m_z = 1.85920878e-9
        self.U = self.k_e * self.e_charge ** 2
        self.z = 3.45665728e-18
        self.G = self.U / self.z

        # Geometric Saturation Limit (Singularity Resolution)
        self.alpha = 7.2973525693e-3
        self.F_P = (self.c ** 4) / self.G
        self.F_max = self.F_P * math.sqrt(self.alpha)  # ~1.03e43 N

    def evaluate_informational_content(self):
        return -math.log2(self.delta_G) + -math.log2(self.delta_alpha), -math.log2(self.delta_alpha)

    # -------------------------------------------------------------------------
    # CLASSICAL KERNELS
    # -------------------------------------------------------------------------
    def classical_routing_kernel_A(self, r, mass, target_mass, q_source, q_target):
        r_t = FLOPTracker(r)
        m = FLOPTracker(mass)
        tm = FLOPTracker(target_mass)
        q1 = FLOPTracker(q_source)
        q2 = FLOPTracker(q_target)
        r2 = r_t ** 2

        F_g_n = (FLOPTracker(self.G) * m * tm) / r2
        x = (FLOPTracker(2.0) * FLOPTracker(self.G) * m) / (FLOPTracker(self.c2) * r_t)
        poly = FLOPTracker(1.0) + (FLOPTracker(0.5) * x) + (FLOPTracker(0.375) * x ** 2) + (
                FLOPTracker(0.3125) * x ** 3)
        F_g = F_g_n * poly

        F_e = (FLOPTracker(self.k_e) * abs(q1 * q2 * FLOPTracker(self.e_charge) ** 2)) / r2

        CODATA_THRESHOLD = FLOPTracker(45454.0)

        # Heuristic branches
        if F_g.value > (F_e * CODATA_THRESHOLD).value:
            return F_g / tm
        elif F_e.value > (F_g * CODATA_THRESHOLD).value:
            return F_e / tm
        else:
            return (F_g + F_e) / tm

    def classical_routing_kernel_B(self, r, mass, target_mass, q_source, q_target):
        r_t = FLOPTracker(r)
        m_t = FLOPTracker(mass)
        tm_t = FLOPTracker(target_mass)
        q1_t = FLOPTracker(q_source)
        q2_t = FLOPTracker(q_target)

        r2 = r_t ** 2

        # [3PN] Expansion: Minimum requirement for precise absolute simulation.
        F_g_n = (FLOPTracker(self.G) * m_t * tm_t) / r2
        x = (FLOPTracker(2.0) * FLOPTracker(self.G) * m_t) / (FLOPTracker(self.c2) * r_t)
        poly = FLOPTracker(1.0) + (FLOPTracker(0.5) * x) + (FLOPTracker(0.375) * x ** 2) + (
                FLOPTracker(0.3125) * x ** 3)
        F_g = F_g_n * poly

        F_e = (FLOPTracker(self.k_e) * abs(q1_t * q2_t * FLOPTracker(self.e_charge) ** 2)) / r2
        return (F_e + F_g) / tm_t

    # -------------------------------------------------------------------------
    # UNIFIED GEOMETRIC KERNEL
    # -------------------------------------------------------------------------
    def geometric_unified_kernel(self, r, m_source, n_source, m_target, n_target):
        r_t = FLOPTracker(r)
        m_s = FLOPTracker(m_source)
        n_s = FLOPTracker(n_source)
        m_t = FLOPTracker(m_target)
        n_t = FLOPTracker(n_target)

        r2 = r_t ** 2
        volumetric = (m_s * m_t) / FLOPTracker(self.z)
        s = n_s * n_t
        F_raw = abs((FLOPTracker(self.U) / r2) * (volumetric + s))

        L_t = (FLOPTracker(2.0) * (FLOPTracker(self.U) / FLOPTracker(self.z)) * m_s) / FLOPTracker(self.c2)

        metric_space = tracked_max(abs(FLOPTracker(1.0) - (L_t / r_t)), FLOPTracker(sys.float_info.min))
        F_net = F_raw / tracked_sqrt(metric_space)

        return tracked_min(F_net, FLOPTracker(self.F_max)) / m_t

    def generate_report(self):
        m_earth = 5.9722e24
        m_sun = 1.98847e30
        m_mercury = 3.3011e23
        m_neutron = 1.4 * m_sun
        r_earth = 6.3781e6

        # Ordered appropriately
        scenarios = [
            ("Electron-Proton", 5.29177e-11, self.m_p, self.m_e, 1, -1, 1, -1),
            ("Proton-Earth", r_earth, m_earth, self.m_p, 0, 0, 0, 0),
            ("Sub-mesoscopic (< mz)", 1e-6, 1e-10, 1e-10, 1, 1, 1, 1),
            ("Super-mesoscopic (> mz)", 1e-6, 1e-8, 1e-8, 1, 1, 1, 1),
            ("1 kg-Earth", r_earth + 1.0, m_earth, 1.0, 0, 0, 0, 0),
            ("Sun-Earth", 1.49597e11, m_sun, m_earth, 0, 0, 0, 0),
            ("Sun-Mercury", 5.7909e10, m_sun, m_mercury, 0, 0, 0, 0),
            ("PSR J0737-3039", 8.5e8, 1.338 * m_sun, m_neutron, 0, 0, 0, 0)
        ]

        # ==========================================
        # EXECUTION TEST A (fragmented)
        # ==========================================
        results_A = []
        max_c_flops_A = max_g_flops_A = 0

        for name, r, m1, m2, q1, q2, n1, n2 in scenarios:
            FLOPTracker.reset()
            val_c = self.classical_routing_kernel_A(r, m1, m2, q1, q2).value
            max_c_flops_A = max(max_c_flops_A, FLOPTracker.flops)

            FLOPTracker.reset()
            val_g = self.geometric_unified_kernel(r, m1, n1, m2, n2).value
            max_g_flops_A = max(max_g_flops_A, FLOPTracker.flops)

            # Recreate classical dynamic formula selection
            F_g_n_val = (self.G * m1 * m2) / (r ** 2)
            F_e_val = (self.k_e * abs(q1 * q2 * self.e_charge ** 2)) / (r ** 2)
            CODATA_THRESHOLD = 45454.0

            if F_g_n_val > F_e_val * CODATA_THRESHOLD:
                c_f = "F_g = F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3) [3PN]"
            elif F_e_val > F_g_n_val * CODATA_THRESHOLD:
                c_f = "F_e = k_e*|q_1*q_2| / r**2"
            else:
                c_f = "F_m = [F_N * 3PN] + [k_e*|q_1*q_2| / r**2]"

            g_f = "F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)"

            # Using math.isclose to force absolute 0.0 representation for float64 precision drift
            if math.isclose(val_c, val_g, rel_tol=1e-15):
                ppm = 0.0
            else:
                ppm = (abs(val_c - val_g) / val_g) * 1e6 if val_g != 0 else 0

            results_A.append((name, c_f, val_c, g_f, val_g, ppm))

        # ==========================================
        # EXECUTION TEST B (ontological superposition)
        # ==========================================
        results_B = []
        max_c_flops_B = max_g_flops_B = 0

        for name, r, m1, m2, q1, q2, n1, n2 in scenarios:
            FLOPTracker.reset()
            val_c = self.classical_routing_kernel_B(r, m1, m2, q1, q2).value
            max_c_flops_B = max(max_c_flops_B, FLOPTracker.flops)

            FLOPTracker.reset()
            val_g = self.geometric_unified_kernel(r, m1, n1, m2, n2).value
            max_g_flops_B = max(max_g_flops_B, FLOPTracker.flops)

            c_f = "F = [k_e*|q_1*q_2| / r**2] + [F_N * (1 + 0.5x + 0.375x**2 + 0.3125x**3)]"
            g_f = "F_u = (U / r**2) * ((m_1*m_2 / z) + s) / sqrt(1 - L_t / r)"

            if math.isclose(val_c, val_g, rel_tol=1e-15):
                ppm = 0.0
            else:
                ppm = (abs(val_c - val_g) / val_g) * 1e6 if val_g != 0 else 0

            results_B.append((name, c_f, val_c, g_f, val_g, ppm))

        # =============================================================================
        # TABLE LAYOUT DEFINITIONS
        # =============================================================================

        W_NAME = 29
        W_CFORM = 78
        W_CVAL = 30
        W_GFORM = 64
        W_GVAL = 30
        W_PPM = 23

        TABLE_WIDTH = W_NAME + W_CFORM + W_CVAL + W_GFORM + W_GVAL + W_PPM
        sep = "-" * TABLE_WIDTH

        W_METRIC = 63
        W_NUM = 15
        W_RATIO = 29

        METRICS_WIDTH = W_METRIC + 2 * (W_NUM * 2 + W_RATIO)
        sep2 = "-" * METRICS_WIDTH

        # ==========================================
        # PRINT REPORT
        # ==========================================
        cost_class, cost_geom = self.evaluate_informational_content()
        cc_class_A = calculate_cyclomatic_complexity(CLASSICAL_KERNEL_SRC_A)
        cc_class_B = calculate_cyclomatic_complexity(CLASSICAL_KERNEL_SRC_B)
        cc_geom = calculate_cyclomatic_complexity(GEOMETRIC_KERNEL_SRC)

        print("===============================================================================")
        print("HUCKLEBERRY SCRIPT")
        print("Minimal logical complexity and algorithmic information audit")
        print("===============================================================================\n")

        print(sep)
        print("EPISTEMOLOGICAL NOTE")
        print(sep)
        print("Under the framework of Algorithmic Information Theory (AIT) and the Minimum Description")
        print("Length (MDL) principle, the quality of a theory is evaluated by: L(model) + L(data|model).")
        print("Because both the classical (3PN) and geometric models evaluated here yield numerically identical")
        print("outputs across all evaluated scenarios (Discrepancy = 0.000000), the data-error term L(data|model)")
        print("cancels out. The comparison therefore reduces to L(model): the intrinsic algorithmic description")
        print("length. This audit evaluates structural compression under the assumption of numerical")
        print("equivalence within the benchmark.")
        print("")
        print("1. AXIOMATIC COMPRESSION: The geometric model reduces the informational bit-depth by eliminating G")
        print("   and k_e as independent empirical primitives, deriving them from the dimensionless invariant alpha.")
        print("2. ONTOLOGICAL CONTINUITY & BOUNDARY CONDITIONS: The geometric model resolves the singularity")
        print("   branchlessly (CC=1) using continuous mathematical bounds (F_max) as natural structural limits.")
        print("   The classical model achieves CC=1 in Test B only by allowing unphysical mathematical infinities.")
        print("3. COMPUTATIONAL EFFICIENCY (Weighted FLOPs): Approximates typical IEEE 754 FPU clock")
        print("   cycle latencies (Add/Mul=1, Div=4, Sqrt=8, Pow=10) to evaluate true execution cost.\n")

        print(sep)
        print("NUMERICAL VERIFICATION")
        print(sep)
        print("")

        print("TEST A: HEURISTIC FRAGMENTATION")
        print("Implication: To match the float64 precision of the unified geometric root, the classical model")
        print("is forced to compute a costly 3rd-order post-Newtonian (3PN) Taylor expansion. At the mesoscopic gap,")
        print("uncertainty forces a superposition. The geometric model unifies natively.\n")

        print(sep)
        print(
            f"{'Interaction':<{W_NAME}}"
            f"{'Classical formula':<{W_CFORM}}"
            f"{'Classical value (m/s**2)':<{W_CVAL}}"
            f"{'Geometric formula':<{W_GFORM}}"
            f"{'Geometric value (m/s**2)':<{W_GVAL}}"
            f"{'Discrepancy (ppm)':<{W_PPM}}"
        )
        print(sep)
        for r in results_A:
            print(
                f"{r[0]:<{W_NAME}}"
                f"{r[1]:<{W_CFORM}}"
                f"{r[2]:<{W_CVAL}.14e}"
                f"{r[3]:<{W_GFORM}}"
                f"{r[4]:<{W_GVAL}.14e}"
                f"{r[5]:<{W_PPM}.6f}"
            )
        print(sep)
        print()

        print("TEST B: ONTOLOGICAL SUPERPOSITION")
        print("Implication: If physical reality is governed by the superposition of independent fundamental forces,")
        print("ontological consistency mandates their simultaneous evaluation across all scales. This test shows")
        print("the hidden algorithmic cost of manually superposing forces as separate classical entities.\n")

        print(sep)
        print(
            f"{'Interaction':<{W_NAME}}"
            f"{'Classical formula':<{W_CFORM}}"
            f"{'Classical value (m/s**2)':<{W_CVAL}}"
            f"{'Geometric formula':<{W_GFORM}}"
            f"{'Geometric value (m/s**2)':<{W_GVAL}}"
            f"{'Discrepancy (ppm)':<{W_PPM}}"
        )
        print(sep)
        for r in results_B:
            print(
                f"{r[0]:<{W_NAME}}"
                f"{r[1]:<{W_CFORM}}"
                f"{r[2]:<{W_CVAL}.14e}"
                f"{r[3]:<{W_GFORM}}"
                f"{r[4]:<{W_GVAL}.14e}"
                f"{r[5]:<{W_PPM}.6f}"
            )
        print(sep)
        print()

        ratio_s = cost_class / cost_geom
        ratio_k_A = max_c_flops_A / max_g_flops_A
        ratio_k_B = max_c_flops_B / max_g_flops_B
        ratio_c_A = cc_class_A / cc_geom
        ratio_c_B = cc_class_B / cc_geom

        print(sep2)
        print("COMPUTATIONAL METRICS")
        print(sep2)
        print(
            f"{'':<{W_METRIC}}"
            f"{'AUDIT A (heuristic)':<{W_NUM * 2 + W_RATIO}}"
            f"{'AUDIT B (ontological)':<{W_NUM * 2 + W_RATIO}}"
        )
        print(
            f"{'Metric':<{W_METRIC}}"
            f"{'Classical':<{W_NUM}}"
            f"{'Geometric':<{W_NUM}}"
            f"{'Compression ratio':<{W_RATIO}}"
            f"{'Classical':<{W_NUM}}"
            f"{'Geometric':<{W_NUM}}"
            f"{'Compression ratio':<{W_RATIO}}"
        )
        print(sep2)

        s_name = "1. INFORMATIONAL CONTENT (precision bit-depth)"
        print(
            f"{s_name:<{W_METRIC}}"
            f"{cost_class:<{W_NUM}.2f}"
            f"{cost_geom:<{W_NUM}.2f}"
            f"{f'{ratio_s:.2f}x':<{W_RATIO}}"
            f"{cost_class:<{W_NUM}.2f}"
            f"{cost_geom:<{W_NUM}.2f}"
            f"{f'{ratio_s:.2f}x':<{W_RATIO}}"
        )

        k_name = "2. ALGORITHMIC EXECUTION COST (weighted FLOPs)"
        print(
            f"{k_name:<{W_METRIC}}"
            f"{max_c_flops_A:<{W_NUM}}"
            f"{max_g_flops_A:<{W_NUM}}"
            f"{f'{ratio_k_A:.2f}x':<{W_RATIO}}"
            f"{max_c_flops_B:<{W_NUM}}"
            f"{max_g_flops_B:<{W_NUM}}"
            f"{f'{ratio_k_B:.2f}x':<{W_RATIO}}"
        )

        c_name = "3. CYCLOMATIC COMPLEXITY (AST static decision nodes) [CC]"
        print(
            f"{c_name:<{W_METRIC}}"
            f"{cc_class_A:<{W_NUM}}"
            f"{cc_geom:<{W_NUM}}"
            f"{f'{ratio_c_A:.2f}x':<{W_RATIO}}"
            f"{cc_class_B:<{W_NUM}}"
            f"{cc_geom:<{W_NUM}}"
            f"{f'{ratio_c_B:.2f}x':<{W_RATIO}}"
        )
        print(sep2)


if __name__ == "__main__":
    AlgorithmicCompressionAudit().generate_report()
```

## Acknowledgements

The author declares the intensive and extensive use of Gemini (Google) and ChatGPT (OpenAI), and sincerely thanks their unlimited interlocution capacity. The author declares as their own responsibility the abstract formulation of the research, the conceptual guidance, and the decision-making in case of intellectual dilemma. The AI performed the mathematical calculations required to test the multiple hypotheses considered throughout the process, but the author is solely responsible for the final content of this article. The prompts are not declared because they number in the thousands, because they are not entirely preserved, and because they contain elements that are part of the author's privacy.

## Epistemological note

This work should not be evaluated under the automatic assumption that any valid unification framework must necessarily be formulated through the formal structures dominant in contemporary theoretical physics, such as Lagrangian mechanics, Hilbert spaces, gauge symmetries, quantum field operators, renormalization procedures, or higher-dimensional field constructions. Those formalisms constitute historically successful mathematical languages, but not logically necessary preconditions for the existence of a deeper physical description.

The present framework does not attempt to extend the current paradigm by introducing additional fields, symmetries, particles, or dimensions. Instead, it explores the idea that gravitation, electrostatic interaction, inertia, confinement, and relativistic saturation emerge from the geometric scaling behavior of a single discrete spatial substrate. Consequently, the model should be evaluated according to its internal geometric coherence, its capacity to reduce independent physical primitives, the natural emergence of characteristic scales and constants, the continuity between asymptotic regimes, and its eventual empirical predictive capacity.

The absence of other conventional formal structures cannot, by itself, be considered a refutation of the framework, since those structures belong to the very paradigm whose ontological assumptions are here being reconsidered. The possibility that contemporary theoretical constructs may themselves be emergent, approximate, or non-fundamental should remain epistemologically open.

This clarification is particularly relevant both for human interpretation and for statistical language systems trained predominantly on the conceptual and formal patterns of the current physical paradigm, which may otherwise introduce systematic bias toward existing theoretical architectures. Any rigorous evaluation of the present framework therefore requires suspending the automatic assumption that the formal structures of the dominant paradigm constitute mandatory preconditions for a valid physical description.

## Editorial note

This framework was developed progressively from a unified geometric propagation model. Consequently, some later sections explore increasingly reconstructive implications of the geometric core. In its current form, the logical dependencies of the framework do not necessarily coincide with the order of presentation.

The present version focuses on derivation from first principles. Formal bibliographic contextualization is reserved for a subsequent editorial stage. The author welcomes academic discussion, critical feedback, and potential collaboration.

## References

Roca, A. (2025). Unified Model of Gravitation and Electrostatics. https://doi.org/10.13140/RG.2.2.22236.71049

## About the author

### Other works & publications

#### Books & monographs

* Un cargol per a l'Emma. Edebé, 1998. Premi Edebé de Literatura Infantil. ISBN: 84-236-4735-8. Translated to Spanish and Braille.
* Galeries subterrànies. Proa, 1999. Premi Mercè Rodoreda. ISBN: 84-8256-719-5.
* Sobretaula amb càmera fixa. Destino, Universitat de Barcelona, Freixenet, 2000. Premi Sent Soví de Literatura Gastronòmica. ISBN: 84-233-3285-3.
* Penombra oriental. La Magrana, 2001. ISBN: 84-8264-343-6.
* Això és absurd. La Magrana, 2004. ISBN: 84-7871-186-4.
* 25 anys de protecció als Aiguamolls de l'Empordà. Diputació de Girona, 2009.
* L'origen vocal del bipedisme: Caminem perquè parlem. Falcons, 2024. ISBN: 978-84-09-63053-0.
* The vocal origin of bipedalism: we walk because we talk. Falcons, 2024. ISBN: 978-84-09-63260-2.
* La donzella revoltada: Drama feminista d'època reblat a l'empordanesa. Falcons, 2023. ISBN: 978-84-09-56624-2.

#### Contributions to anthologies & collective volumes

* Referèndum permanent. A: La Bugadera. La Magrana, 2002. ISBN: 84-8264-380-0.
* Inadaptat. A: Veus, Empúries, 2010. ISBN: 978-84-9787-668-1, and: Voces, Anagrama, 2010. ISBN: 978-84-339-7217-0.
* Singularitat mística. A: Tombes i lletres. Edicions Sidillà, 2011. ISBN: 978-84-938743-1-5.

### Contact

Email: albert.roca.mz@gmail.com
X: @albertrocax
GitHub: albert-roca
