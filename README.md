# prompt_assistant
[![PyPI version](https://img.shields.io/pypi/v/prompt_assistant.svg)](https://pypi.org/project/prompt_assistant/)
[![Build Status](https://travis-ci.org/ronliu014/prompt_assistant.svg?branch=main)](https://travis-ci.org/ronliu014/prompt_assistant)
`prompt_assistant` 是一个用于创建结构化提示的 Python 库。它提供了一个框架，用于以一致和结构化的方式定义提示，从而更容易生成内容，如产品描述、代码段和 JSON 数据。该库还包含了一系列预定义的助手类，如语言专家助手、产品设计师助手、Python 架构师助手、Python 编码助手、软件架构师助手和软件工程师助手等，以帮助用户更高效地完成日常工作。
## 目录结构
```
prompt_assistant/
|-- core/
|   |-- __init__.py
|   |-- prompt_assistant.py   # 提示词助手基类
|   |-- prompt_template_model.py  # 提示词模板类
|-- exts/                     # 提示词助手类目录
|   |-- __init__.py
|   |-- language_expert_assistant.py
|   |-- product_designer_assistant.py
|   |-- python_architect_assistant.py
|   |-- python_coder_assistant.py
|   |-- software_architect_assistant.py
|   |-- software_engineer_assistant.py
|-- tests/                    # 单元测试目录
|   |-- __init__.py
|   |-- test_language_expert_assistant.py
|   |-- test_product_designer_assistant.py
|   |-- test_prompt_assistant.py
|   |-- test_python_architect_assistant.py
|   |-- test_python_coder_assistant.py
|   |-- test_software_architect_assistant.py
|   |-- test_software_engineer_assistant.py
|-- __init__.py
|-- README.md
|-- setup.py
|-- LICENSE
```
## 安装
使用以下命令安装 `prompt_assistant`：
```bash
pip install prompt_assistant
```
确保你的 Python 环境为 3.x 版本。
## 使用
### 导入模块
```python
from prompt_assistant import LanguageExpertAssistant
from prompt_assistant import ProductDesignerAssistant
from prompt_assistant import PyArchitectAssistant
from prompt_assistant import PyCoderAssistant
from prompt_assistant import SoftwareArchitectAssistant
from prompt_assistant import SoftwareEngineerAssistant
```
### 示例
以下是一个使用 `LanguageExpertAssistant` 的简单示例：
```python
# 创建语言专家助手实例
language_expert = LanguageExpertAssistant()
# 使用助手提供提示词
prompt = language_expert.create_prompt("翻译以下句子：Hello World")
print(prompt)
```
以下是一个使用 `ProductDesignerAssistant` 的简单示例：
```python
# 创建产品设计师助手实例
product_designer = ProductDesignerAssistant()
# 使用助手提供提示词
prompt = product_designer.create_prompt("设计一个用户友好的登录界面")
print(prompt)
```
更多示例请参考各助手类的文档。
## 单元测试
运行以下命令以执行单元测试：
```bash
python -m unittest discover -s tests
```
这将验证库的功能是否按预期工作。
## 许可证
本项目使用 [MIT License](LICENSE)。
## 贡献
欢迎贡献者提交 PR 或提出问题。请遵循以下准则：
- 确保代码风格与现有代码保持一致。
- 添加适当的单元测试。
- 更新文档以反映任何更改。
## 联系方式
如有任何问题，请通过邮箱 [66141975@qq.com](mailto:66141975@qq.com) 联系我们。
## Features
- **Structured Prompt Framework**: The library follows a structured prompt framework that defines the task, context, input, output, constraints, and style for each prompt.
- **Modular Design**: Each field in the prompt framework is independent and clearly defined, allowing for easy parsing and extension.
- **Flexibility**: The `context` and `constraints` fields allow for flexible adjustment of task scope.
- **Extensibility**: Supports adding custom fields to the prompt framework, such as `metadata` and `references`.
- **Programmatic Support**: The JSON format is easy to parse and program, making it suitable for automation and integration with other systems.
## Installation
To install prompt_assistant, run the following command:
```bash
pip install prompt_assistant
```
Ensure your Python environment is version 3.x.
## Usage
The prompt_assistant library can be used to create and manage structured prompts. Here's an example of how to use it:
```python
from prompt_assistant import PromptTemplateModel, PromptAssistant
# Define a prompt
prompt = PromptTemplateModel(
    task="Generate a product description",
    context="E-commerce website product description",
    input={
        "type": "text",
        "data": "A lightweight laptop with a touch screen, brand ABC, weight 1.2kg, suitable for students and business people."
    },
    output={
        "type": "text",
        "format": "paragraph",
        "examples": [
            "This lightweight ABC laptop weighs only 1.2kg and features a touch screen, making it perfect for students and business people."
        ]
    },
    constraints={
        "length_limit": "100 characters",
        "rules": ["No negative descriptions", "Do not deviate from product features"]
    },
    style={
        "tone": "professional",
        "language": "Chinese"
    }
)
# Generate output
output = prompt.to_json()
print(output)
```
## Examples
The library includes several examples to demonstrate how to use structured prompts for different tasks:
- **Generate a product description**: Create a prompt for generating a product description for an e-commerce website.
- **Generate Python code**: Define a prompt for generating a Python function that calculates the sum of two numbers.
- **Generate JSON data**: Design a JSON data template for a user information card to display basic user information.
## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](https://github.com/ronliu014/prompt_assistant/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ronliu014/prompt_assistant/blob/master/LICENSE.md) file for details.
## Authors
- **Ron Liu** - *Initial work* - [Ron Liu's GitHub Profile](https://github.com/ronliu014)
See also the list of [contributors](https://github.com/ronliu014/prompt_assistant/graphs/contributors) who participated in this project.
## Acknowledgments
## Sponsors
## Support
If you are having issues, please let us know by filing an issue on GitHub.
## Stay in Touch
- [Discussion Group](https://example.com/discussion)
- [Twitter](https://twitter.com/prompt_assistant)
## Further Reading
For more information, see the following resources:
- [Python Documentation](https://docs.python.org/3/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
