import re


def convert_format(input_file, output_file):

    with open(input_file, 'r') as f:
        content = f.read()

    # Find all entries
    entries = re.findall(r'\*\*(\w+)\*\*\:(.*?)</details>', content, re.DOTALL)
    with_details = True
    if len(entries) == 0:
        entries = re.findall(r'\*\*(\w+)\*\*\:(.*?)\)\]', content, re.DOTALL)
        with_details = False

    output = ''
    for entry in entries:
        abbr = entry[0]
        if with_details:
            entry = entry[1] + '</details>'
        else:
            entry = entry[1] + ')]'
        print(entry)

        # Extract components
        match = re.search(r' (.+)\.\n   - (.+)(\.|\?) \[\[(.+)\'([0-9]+)\]\((.+?)\)\]', entry)
        authors, title, _, conf, year, link = match.groups()
        
        # Reformat
        output += f'* **{title}**<br>\n'
        output += f'*{authors}*<br>\n'
        output += f'{conf}\'{year} [[Paper]({link})]\n'

        # Extract code
        match = re.search(r'\[\[code\]\((.+)\)\]', entry)
        if match is not None:
            code = match.group(1)
            output += f'[[Code]({code})]\n'
        
        # Extract framework 
        match = re.search(r'<details close>\n  (.+?)</details>', entry, re.DOTALL)
        if match is not None:
            framework = match.group(1)
            framework = framework.replace('<summary>Framework</summary>', f'<summary>{abbr} Framework</summary>')
            output += r'   <details close>' + '\n  ' + framework + r'</details>' + '\n\n'
        else:
            output += '\n'

    with open(output_file, 'w') as f:
        f.write(output)


convert_format('input.txt', 'output.md')
