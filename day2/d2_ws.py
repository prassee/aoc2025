# %%
x = 82
max = 100
direction = 1

# %%
print(f"{x} {max} {direction}")
# %%
direction = -1
print(f"{x} {max} {direction}")
# if +ve diff of 100 - curr_pos
# if -ve curr_pos
rotation = 280
# %%
# -ve
int(rotation / x)
# %% +ve
int(rotation / (100 - x))
