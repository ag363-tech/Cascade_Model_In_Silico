def three_node_system(t, y, params):
    A, B, C = y

    k_prod_A = params["k_prod_A"]
    k_deg_A_base = params["k_deg_A"]
    k_deg_A_fast = params["k_deg_A_fast"]
    t_switch = params["t_switch"]

    k1 = params["k1"]
    k2 = params["k2"]

    k_deg_B = params["k_deg_B"]
    k_deg_C = params["k_deg_C"]

    if t < t_switch:
        k_deg_A = k_deg_A_base
    else:
        k_deg_A = k_deg_A_fast

    dA_dt = k_prod_A - k_deg_A * A
    dB_dt = k1 * A - k_deg_B * B
    dC_dt = k2 * B - k_deg_C * C

    return [dA_dt, dB_dt, dC_dt]
