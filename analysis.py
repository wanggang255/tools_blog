import ast
import os
from radon.visitors import ComplexityVisitor

# Define custom visitor class to extract imported libraries
class ImportVisitor(ast.NodeVisitor):
    def __init__(self):
        self.imported_libraries = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imported_libraries.append(alias.name)

    def visit_ImportFrom(self, node):
        if node.module:
            for alias in node.names:
                self.imported_libraries.append(node.module + '.' + alias.name)
        else:
            for alias in node.names:
                self.imported_libraries.append(alias.name)

# Project root directory
project_root = '.'

# Walk through project directory and analyze Python files
for root, dirs, files in os.walk(project_root):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r',encoding='utf-8') as file:
                source_code = file.read()
            # Parse the code and extract imported libraries
            parsed_ast = ast.parse(source_code)
            import_visitor = ImportVisitor()
            import_visitor.visit(parsed_ast)
            imported_libraries = import_visitor.imported_libraries

            # Print the imported library list for the current file
            print(f'File: {file_path}')
            for library in imported_libraries:
                print(library)
            print('---')