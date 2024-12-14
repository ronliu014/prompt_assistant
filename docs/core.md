# 核心模块文档

## PromptTemplateModel

位置: `core/prompt_template_model.py`

这是一个基础的提示模板模型类，用于定义和验证提示模板的结构。

### 主要属性:

- task: str - 任务描述
- role: str - 角色描述
- context: str - 上下文信息
- input: Dict - 输入配置
- output: Dict - 输出配置
- constraints: Dict - 约束条件
- style: Dict - 风格设置
- chain_of_thought: Dict - 思维链配置

### 主要方法:

- to_json(): 将模板转换为JSON格式
- to_compact_json(): 将模板转换为紧凑的JSON格式

## PromptAssistant

位置: `core/prompt_assistant.py`

这是所有助手类的基类，提供了基础的提示模板创建功能。

### 主要属性:

- templates: List[PromptTemplateModel] - 存储创建的模板

### 主要方法:

- create_prompt(): 创建提示模板的抽象方法 