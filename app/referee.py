def compare_ec2_vs_lambda(inputs):
    ec2_score = 0
    lambda_score = 0
    explanation = []

    if inputs["traffic"] == "spiky":
        lambda_score += 2
        explanation.append("Lambda handles spiky traffic better due to auto-scaling.")
    else:
        ec2_score += 2
        explanation.append("EC2 is cost-effective for steady traffic.")

    if inputs["budget"] == "low":
        lambda_score += 1
        explanation.append("Lambda avoids always-on server costs.")
    else:
        ec2_score += 1
        explanation.append("EC2 provides predictable pricing at scale.")

    if inputs["execution_time"] == "long":
        ec2_score += 2
        explanation.append("EC2 supports long-running workloads.")
    else:
        lambda_score += 2
        explanation.append("Lambda is ideal for short-lived tasks.")

    return {
        "EC2": ec2_score,
        "Lambda": lambda_score,
        "Tradeoffs": explanation
    }

