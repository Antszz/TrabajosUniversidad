template <
    typename tuple_t,
    typename bmask_t>
void atomic_update(
    tuple_t tuple,
    bmask_t bmask) {

    typedef typename tuple_t::value_t value_t;

    auto g_state = global_state.load();
    auto l_value = tuple.value;
    state_t<bmask_t, value_t> target;

    do {

        // exit if solution is not optimal
        if (g_state.value > l_value)
        return;

        // construct the desired target
        target.value = l_value;
        target.bmask = bmask;
    } while (!global_state.compare_exchange_weak(g_state, target));
}