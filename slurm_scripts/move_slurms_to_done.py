import os
import shutil

# define the directories
output_dir = 'outputs'
first_runs_dir = 'first_runs'
done_dir = 'done'

# get list of filenames in the output_dir
filenames = os.listdir(output_dir)

for filename in filenames:
    if filename.endswith(".out"):
        # remove the .out suffix
        filename = filename[:-4]
        # extract the parameters from the filename
        parts = filename.split('__')
        print(parts)
        param_dict = {part.split('-')[0]: '-'.join(part.split('-')[1:]) for part in parts[1:]}
        print(param_dict)
        # format the corresponding filename in first_runs
        corresponding_filename = f"{param_dict['n']}_{param_dict['d']}_{param_dict['mu']}_{param_dict['dist']}_{param_dict['a']}.sh"
        # check if the corresponding file exists in first_runs_dir
        if corresponding_filename in os.listdir(first_runs_dir):
            # move the file from first_runs to done
            shutil.move(os.path.join(first_runs_dir, corresponding_filename), os.path.join(done_dir, corresponding_filename))
