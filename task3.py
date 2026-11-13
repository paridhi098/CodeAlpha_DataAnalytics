import matplotlib.pyplot as plt
import seaborn as sns


def create_visualizations():
  df = sns.load_dataset("titanic")
  sns.set_theme(style="whitegrid")

  # 1. Survival Rate by Passenger Class and Gender
  plt.figure(figsize=(8, 6))
  sns.barplot(x="class", y="survived", hue="sex", data=df, palette="muted")
  plt.title("Survival Rate by Passenger Class and Gender", fontsize=14)
  plt.xlabel("Passenger Class", fontsize=12)
  plt.ylabel("Survival Rate", fontsize=12)
  plt.savefig("survival_by_class.png")
  plt.close()

  # 2. Age Distribution of Passengers
  plt.figure(figsize=(8, 6))
  sns.histplot(
      df["age"].dropna(), bins=30, kde=True, color="skyblue", edgecolor="black"
  )
  plt.title("Age Distribution of Passengers", fontsize=14)
  plt.xlabel("Age", fontsize=12)
  plt.ylabel("Count", fontsize=12)
  plt.savefig("age_distribution.png")
  plt.close()

  print(
      "Visualizations successfully created and saved as"
      " 'survival_by_class.png' and 'age_distribution.png'."
  )


if __name__ == "__main__":
  create_visualizations()