# prompt_assistant

[English](#english) | [中文](#chinese)

<h2 id="english">English</h2>

`prompt_assistant` is a Python library that helps create structured prompts for AI interactions. It provides a systematic framework for generating high-quality prompts across various domains like software development, product design, and language tasks.

## Key Features

- **Structured Prompt Framework**: Define prompts with clear task, context, input/output specifications
- **Multiple Assistant Types**: Pre-built assistants for different domains:
  - Language Expert Assistant
  - Product Designer Assistant  
  - Python Architect Assistant
  - Python Coder Assistant
  - Software Architect Assistant
  - Software Engineer Assistant
- **Flexible & Extensible**: Easy to customize and add new assistant types
- **JSON Compatible**: All prompts can be serialized to/from JSON

## Installation

```bash
pip install prompt_assistant
```

Requires Python 3.10+

## Quick Start

```python
from prompt_assistant import PyCoderAssistant

# Create a Python coding assistant
assistant = PyCoderAssistant()

# Generate a prompt for writing a function
prompt = assistant.create_prompt(
    "Write a function to calculate fibonacci numbers"
)

# Get the structured prompt as JSON
prompt_json = prompt.to_json()
```

## Documentation

Each assistant type provides specialized prompting capabilities:

- **Language Expert**: Translation and language-related tasks
- **Product Designer**: UI/UX and product design specifications
- **Python Architect**: High-level Python architecture design
- **Python Coder**: Python implementation details
- **Software Architect**: System architecture design
- **Software Engineer**: General software engineering tasks

## Examples

```python
# Using Language Expert Assistant
from prompt_assistant import LanguageExpertAssistant

expert = LanguageExpertAssistant()
prompt = expert.create_prompt("Translate: Hello World")
print(prompt.to_json())

# Using Product Designer Assistant 
from prompt_assistant import ProductDesignerAssistant

designer = ProductDesignerAssistant()
prompt = designer.create_prompt("Design a user-friendly login interface")
print(prompt.to_json())
```

## License

MIT License

## Author

- **Ron Liu** - *Initial work* - [GitHub](https://github.com/ronliu014)
- Email: 66141975@qq.com

For questions or suggestions, please feel free to:
1. Open an issue on GitHub
2. Contact author directly via email
3. Submit a pull request

---

<h2 id="chinese">中文</h2>

`prompt_assistant` 是一个用于创建结构化AI提示词的Python库。它为不同领域(如软件开发、产品设计和语言任务)提供了系统化的提示词生成框架。

## 主要特性

- **结构化提示框架**: 通过明确的任务、上下文、输入/输出规范来定义提示词
- **多种助手类型**: 预置多种专业领域助手:
  - 语言专家助手
  - 产品设计师助手
  - Python架构师助手
  - Python开发助手
  - 软件架构师助手
  - 软件工程师助手
- **灵活且可扩展**: 易于自定义和添加新的助手类型
- **JSON兼容**: 所有提示词可以与JSON格式互转

## 安装

```bash
pip install prompt_assistant
```

需要Python 3.10+版本

## 快速开始

```python
from prompt_assistant import PyCoderAssistant

# 创建Python编程助手
assistant = PyCoderAssistant()

# 生成编写函数的提示词
prompt = assistant.create_prompt(
    "编写一个计算斐波那契数列的函数"
)

# 获取JSON格式的结构化提示词
prompt_json = prompt.to_json()
```

## 文档说明

每种助手类型提供专门的提示词能力:

- **语言专家**: 翻译和语言相关任务
- **产品设计师**: UI/UX和产品设计规范
- **Python架构师**: Python高层架构设计
- **Python开发者**: Python实现细节
- **软件架构师**: 系统架构设计
- **软件工程师**: 通用软件工程任务

## 使用示例

```python
# 使用语言专家助手
from prompt_assistant import LanguageExpertAssistant

expert = LanguageExpertAssistant()
prompt = expert.create_prompt("翻译: Hello World")
print(prompt.to_json())

# 使用产品设计师助手
from prompt_assistant import ProductDesignerAssistant

designer = ProductDesignerAssistant()
prompt = designer.create_prompt("设计一个用户友好的登录界面")
print(prompt.to_json())
```

## 开源协议

MIT License

## 作者

- **Ron Liu** - *Initial work* - [GitHub](https://github.com/ronliu014)
- Email: 66141975@qq.com

如有问题或建议，欢迎:
1. 在GitHub上提Issue
2. 通过邮件直接联系作者
3. 提交Pull Request
