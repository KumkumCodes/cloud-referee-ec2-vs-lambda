from referee import compare_ec2_vs_lambda

user_input = {
    "traffic": "spiky",
    "budget": "low",
    "execution_time": "short"
}

result = compare_ec2_vs_lambda(user_input)

print("=== AWS EC2 vs AWS Lambda ===")
print("Scores:", result["EC2"], "vs", result["Lambda"])
print("\nTrade-offs:")
for point in result["Tradeoffs"]:
    print("-", point)

