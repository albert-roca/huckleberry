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
