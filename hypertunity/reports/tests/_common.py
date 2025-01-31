from hypertunity.domain import Domain
from hypertunity.optimisation.base import EvaluationScore, HistoryPoint


def generate_history(n_samples):
    domain = Domain({"x": [-5., 6.], "y": {"sin", "sqr"}, "z": set(range(4))}, seed=7)
    history = [HistoryPoint(sample=domain.sample(),
                            metrics={"metric_1": EvaluationScore(float(i)),
                                     "metric_2": EvaluationScore(i * 2.)})
               for i in range(n_samples)]
    if len(history) == 1:
        history = history[0]
    return history, domain
