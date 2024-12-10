# prompt_assistant
[![PyPI version](https://img.shields.io/pypi/v/prompt_assistant.svg)](https://pypi.org/project/prompt_assistant/)
[![Build Status](https://travis-ci.org/ronliu014/prompt_assistant.svg?branch=master)](https://travis-ci.org/ronliu014/prompt_assistant)
prompt_assistant is a Python library designed to assist in creating structured prompts for various tasks. It provides a framework for defining prompts in a consistent and structured manner, making it easier to generate content such as product descriptions, code snippets, and JSON data.

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

## Usage
The prompt_assistant library can be used to create and manage structured prompts. Here's an example of how to use it:
```python
from prompt_assistant import PromptTemplateModel, PromptAssistant, CustomAssistant
# Create a custom assistant
assistant = CustomAssistant()
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
output = assistant.generate_output(prompt)
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
- **Your Name** - *Initial work* - [Your GitHub Profile](https://github.com/ronliu014)
See also the list of [contributors](https://github.com/ronliu014/prompt_assistant/graphs/contributors) who participated in this project.

## Acknowledgments
- [List of acknowledgments](https://github.com/ronliu014/prompt_assistant/blob/master/AUTHORS.md)

## Sponsors
Thank you to all our backers! [[Become a backer](https://opencollective.com/prompt_assistant#backer)]

## Support
If you are having issues, please let us know by filing an issue on GitHub.

## Stay in Touch
Join the discussion group or follow the project on Twitter to stay up to date with the latest announcements.
- [Discussion Group](https://example.com/discussion)
- [Twitter](https://twitter.com/prompt_assistant)

## Further Reading
For more information, see the following resources:
- [Python Documentation](https://docs.python.org/3/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
---

# prompt_assistant
[![PyPI version](https://img.shields.io/pypi/v/prompt_assistant.svg)](https://pypi.org/project/prompt_assistant/)
[![Build Status](https://travis-ci.org/ronliu014/prompt_assistant.svg?branch=master)](https://travis-ci.org/ronliu014/prompt_assistant)
prompt_assistant 是一个用于创建结构化提示的 Python 库。它提供了一个框架，用于以一致和结构化的方式定义提示，从而更容易生成内容，如产品描述、代码段和 JSON 数据。

## 特性
- **结构化提示框架**：库遵循一个结构化提示框架，为每个提示定义任务、上下文、输入、输出、约束和风格。
- **模块化设计**：提示框架中的每个字段都是独立的且定义清晰，便于解析和扩展。
- **灵活性**：`context` 和 `constraints` 字段允许灵活调整任务范围。
- **可扩展性**：支持向提示框架添加自定义字段，如 `metadata` 和 `references`。
- **程序友好**：JSON 格式易于解析和编程，使其适合自动化和与其他系统的集成。

## 安装
要安装 prompt_assistant，请运行以下命令：
```bash
pip install prompt_assistant
```

## 使用
prompt_assistant 库可用于创建和管理结构化提示。以下是如何使用它的示例：
```python
from prompt_assistant import PromptTemplateModel, PromptAssistant, CustomAssistant
# 创建一个自定义助手
assistant = CustomAssistant()
# 定义一个提示
prompt = PromptTemplateModel(
    task="生成产品描述",
    context="电商网站产品描述",
    input={
        "type": "text",
        "data": "一款轻便的笔记本电脑，品牌是ABC，重量为1.2kg，支持触屏，适合学生和商务人士。"
    },
    output={
        "type": "text",
        "format": "段落",
        "examples": [
            "这款轻便的ABC笔记本电脑重量仅为1.2kg，支持触屏功能，非常适合学生和商务人士使用。"
        ]
    },
    constraints={
        "length_limit": "100字以内",
        "rules": ["不得使用负面描述", "不得偏离商品特点"]
    },
    style={
        "tone": "专业",
        "language": "中文"
    }
)
# 生成输出
output = assistant.generate_output(prompt)
print(output)
```

## 示例
库中包含几个示例，演示了如何为不同任务使用结构化提示：
- **生成产品描述**：为电商网站创建一个生成产品描述的提示。
- **生成 Python 代码**：定义一个生成 Python 函数的提示，该函数计算两个数字的和。
- **生成 JSON 数据**：设计一个 JSON 数据模板，用于展示用户基本信息卡。

## 贡献
欢迎贡献！请阅读 [CONTRIBUTING.md](https://github.com/ronliu014/prompt_assistant/blob/master/CONTRIBUTING.md) 了解我们的行为准则以及提交拉取请求的过程。

## 许可证
此项目采用 MIT 许可证 - 请参阅 [LICENSE.md](https://github.com/ronliu014/prompt_assistant/blob/master/LICENSE.md) 文件了解详情。

## 作者
- **您的姓名** - *初始工作* - [您的 GitHub 个人资料](https://github.com/ronliu014)
请参阅 [贡献者列表](https://github.com/ronliu014/prompt_assistant/graphs/contributors)，了解参与此项目的贡献者。

## 致谢
- [致谢列表](https://github.com/ronliu014/prompt_assistant/blob/master/AUTHORS.md)

## 赞助商
感谢所有支持者！[[成为支持者](https://opencollective.com/prompt_assistant#backer)]

## 支持
如果您遇到问题，请在 GitHub 上提交问题以告知我们。

## 保持联系
加入讨论组或关注 Twitter 上的项目，以获取最新公告。
- [讨论组](https://example.com/discussion)
- [Twitter](https://twitter.com/prompt_assistant)

## 进一步阅读
有关更多信息，请参阅以下资源：
- [Python 文档](https://docs.python.org/3/)
- [Pydantic 文档](https://pydantic-docs.helpmanual.io/)
