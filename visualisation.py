import matplotlib.pyplot as plt
import numpy as np


def draw_charts(predictions: dict, functions: dict) -> None:
    prediction_v = predictions["v"]
    prediction_square_v = predictions["square_v"]

    function_v = functions["v"]
    function_square_v = functions["square_v"]

    abscissa_v = np.linspace(min(prediction_v["abscissa"]), max(prediction_v["abscissa"]),
                             len(prediction_v['abscissa']))
    abscissa_square_v = np.linspace(min(prediction_square_v["abscissa"]), max(prediction_square_v["abscissa"]),
                                    len(prediction_square_v['abscissa']))

    ordinate_v = function_v(abscissa_v)
    ordinate_square_v = function_square_v(abscissa_square_v)

    total_time_v = prediction_v["total_time"]
    total_time_square_v = prediction_square_v["total_time"]

    color_simulate_v, color_theory_v, color_simulate_vv, color_theory_vv = 'orange', 'lime', 'red', 'green'

    _, ax = plt.subplots(figsize=(16, 9))
    ax.plot(
        prediction_v['abscissa'], prediction_v['ordinate'], c=color_simulate_v,
        label='simulation_v'
    )
    ax.plot(
        prediction_square_v['abscissa'], prediction_square_v['ordinate'], c=color_simulate_vv,
        label='simulation_square_v'
    )
    ax.set_xlim(0, max(max(ordinate_square_v), max(ordinate_v), max(abscissa_v), max(abscissa_square_v)) * 1.5)

    ax.plot(
        abscissa_v, ordinate_v, c=color_theory_v,
        label='theory_v'
    )
    ax.plot(
        abscissa_square_v, ordinate_square_v, c=color_theory_vv,
        label='theory_square_v'
    )

    ax.text(0.75, 0.6, 'Total flight time for v^1: ' + str(round(total_time_v, 3)) + 's',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes, fontsize=12)
    ax.text(0.75, 0.5, 'Point of falling for v^1: ' + str(round(abscissa_v[-1], 3)) + 'm',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes, fontsize=12)
    ax.text(0.75, 0.4, 'Total flight time for v^2: ' + str(round(total_time_square_v, 3)) + 's',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes, fontsize=12)
    ax.text(0.75, 0.3, 'Point of falling for v^2: ' + str(round(abscissa_square_v[-1], 3)) + 'm',
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes, fontsize=12)

    ax.set_xlabel('x', fontsize=15)
    ax.set_ylabel('y', fontsize=15)

    ax.legend()
    ax.grid(True)

    plt.title('M1 Task', fontsize=25)
    plt.show()
