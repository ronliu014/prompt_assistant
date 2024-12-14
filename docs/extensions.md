# 扩展模块文档

## 通用扩展结构

所有扩展助手类都继承自 PromptAssistant 基类，并实现了特定领域的提示模板创建逻辑。

### 共同特征:

1. 默认角色描述
2. 默认上下文设置
3. 可配置的输入/输出格式
4. 可自定义的约束条件
5. 支持思维链输出

## Python开发者助手 (PythonDeveloperAssistant)

位置: `exts/python_developer_assistant.py`

专门面向Python后端开发的助手类。

### 特点:
- 提供Python相关的专业角色描述
- 支持Python代码生成
- 包含Python最佳实践约束

## Web开发者助手 (WebDeveloperAssistant)

位置: `exts/web_developer_assistant.py`

专门面向Web前端开发的助手类。

### 特点:
- 提供Web开发相关的专业角色描述
- 支持前端代码生成
- 包含响应式设计和性能优化约束

## 其他扩展助手

- SoftwareEngineerAssistant: 软件工程师助手
- SoftwareArchitectAssistant: 软件架构师助手
- PythonArchitectAssistant: Python架构师助手
- PythonCoderAssistant: Python编码助手
- LanguageExpertAssistant: 语言专家助手
- ProductDesignerAssistant: 产品设计师助手 