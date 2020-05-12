import os, re
import subprocess as sub

# see list of projects
def see_project_list():
  print("=> Existing projects")
  # see a list of projects?
  see_projects = input("Do you want to see a list of projects? Y/N ").lower().strip()
  # list folders
  if see_projects == "y":
    # only want folder names not other files
    project_list = os.listdir(os.getcwd())
    pattern = re.compile(r'(\.\w+$)')
    filtered_projects = list(filter(lambda item: not pattern.search(item), project_list))
    if len(filtered_projects) != 0:
      for index, project in enumerate(filtered_projects, start=1):
        print(f"{index}: {project}")
    else:
      print("No projects found in this folder")

def get_project_name():
  print("=> Set project name")
  # ask the user
  user_input = input("What's the name of the project? (use spaces to separate words): ").strip()
  # ask user to confirm
  confirm = input(f"Please confirm project name is {user_input.lower()} Y/N ")
  answers = ["y", "n"]
  # repeat ask for confirmation
  while confirm == "n" or confirm not in answers:
    user_input = input("What's the name of the project? (use spaces to separate words): ").strip()
    confirm = input(f"Please confirm project name is {user_input.lower()} Y/N ")
  else:
    project_name = user_input.title().replace(" ", "-")
    return project_name

def select_language():
  print("=> Select language")
  languages = ["Python", "Ruby", "Javascript", "None"]
  for index, language in enumerate(languages, start=1):
    print(f'{index}: {language}')
  user_input = int(input("What language will you be scripting in? Select index ").strip())
  if user_input <= len(languages):
    language = languages[user_input - 1]
    print(f"You selected {language}")
    return language
  else:
    print(f"Your list doesn\'t contain as many languages max = {len(languages)}")
    select_language()

def initialize_project():
  # create project folder and add README.md with
  # project_name as h1
  project_name = get_project_name()
  os.mkdir(project_name)
  os.chdir(os.path.join(os.getcwd(), project_name))
  with open('README.md', "w") as readme:
    readme.write(f"# {project_name}")
  # initialize repo and do first commit
  sub.run(['git', 'init'])
  sub.run(['git', 'add', '.'])
  sub.run(['git', 'commit', '-m', '"initial commit"'])


# see_project_list()
# select_language()
# initialize_project()