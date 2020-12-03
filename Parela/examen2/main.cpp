#include "threadpool.hpp"

int main () {

    ThreadPool TP(2); // 2 threads are sufficient

    // initialize tuples with random values
    init_tuples(tuples, num_items);

    // traverse left and right branch
    TP.spawn(traverse<index_t, tuple_t, bmask_t>,
        0, tuple_t(0, 0), 0);
    TP.spawn(traverse<index_t, tuple_t, bmask_t>,
        0, tuple_t(0, 0), 1);

    // wait for all tasks to be finished
    TP.wait_and_stop();

    // report the final solution
    auto g_state = global_state.load();
    std::cout << "value " << g_state.value << std::endl;

    auto bmask = g_state.bmask;
    for (index_t i = 0; i < num_items; i++) {
        std::cout << bmask % 2 << " ";
        bmask >>= 1;
    }
    std::cout << std::endl;
}