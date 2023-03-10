import matplotlib.pyplot as plt

# Define chromosome sizes and centromere positions
chromosome_sizes = {'A1': 37718439, 'A2': 31611734, 'A3': 40564783, 'A4': 26049113,
                    'A5': 45217253, 'A6': 54099293, 'A7': 22766400, 'A8': 29265719,
                    'A9': 62871001, 'A10': 15338199, 'C1': 63869038, 'C2': 70998313,
                    'C3': 85909631, 'C4': 53947295, 'C5': 65818846, 'C6': 52992254,
                    'C7': 40522094, 'C8': 52342584, 'C9': 70496361}

centromere_positions = {'A1': 16153434, 'A2': 15326171, 'A3': 20504854, 'A4': 13660117,
                        'A5': 22405641, 'A6': 22830166, 'A7': 11054331, 'A8': 15838887,
                        'A9': 47367679, 'A10': 7925493, 'C1': 51644205, 'C2': 34856694,
                        'C3': 16000000, 'C4': 16000000, 'C5': 17000000, 'C6': 35335801,
                        'C7': 22263006, 'C8': 15460898, 'C9': 26400000}

# Create karyotype plot
fig, ax = plt.subplots(figsize=(15, 10))

y_positions = []
labels = []

for chr_name, chr_size in chromosome_sizes.items():
    centromere_pos = centromere_positions.get(chr_name, None)
    y_pos = len(y_positions) + 0.5
    y_positions.append(y_pos)
    labels.append(chr_name)

    # Add chromosome band rectangles
    ax.add_patch(plt.Rectangle((0, y_pos - 0.25), chr_size, 0.5, facecolor='pink'))

    # Add centromere line
    if centromere_pos is not None:
        ax.plot([centromere_pos, centromere_pos], [y_pos - 0.20, y_pos + 0.20], color='red')

    # Add chromosome size label
    ax.text(chr_size + 5000000, y_pos, '{:,}'.format(chr_size), va='center')

# Set axis properties
ax.set_ylim(0, len(y_positions))
ax.set_xlim(0, max(chromosome_sizes.values()) + 10000000)
ax.set_yticks(y_positions)
ax.set_yticklabels(labels)
ax.set_xlabel('Chromosome Size (bp)')

plt.show()
