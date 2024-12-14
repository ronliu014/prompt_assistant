# 项目结构

MagicSeeds/prompt_assistant/
├── core/                       # 核心功能模块
│   ├── __init__.py
│   ├── prompt_assistant.py     # 基础助手类
│   └── prompt_template_model.py # 提示模板模型
├── exts/                       # 扩展助手模块
│   ├── __init__.py
│   ├── python_developer_assistant.py    # Python开发助手
│   ├── web_developer_assistant.py       # Web开发助手
│   ├── software_engineer_assistant.py   # 软件工程师助手
│   ├── software_architect_assistant.py  # 软件架构师助手
│   ├── python_architect_assistant.py    # Python架构师助手
│   ├── python_coder_assistant.py        # Python编码助手
│   ├── language_expert_assistant.py     # 语言专家助手
│   └── product_designer_assistant.py    # 产品设计师助手
├── tests/                      # 测试用例
│   ├── __init__.py
│   ├── test_python_developer_assistant.py
│   ├── test_web_developer_assistant.py
│   ├── test_software_engineer_assistant.py
│   └─�� test_software_architect_assistant.py
└── docs/                       # 文档目录
    ├── structure.md            # 项目结构文档
    ├── core.md                 # 核心模块文档
    ├── extensions.md           # 扩展模块文档
    ├── testing.md              # 测试文档
    └── usage.md                # 使用指南 