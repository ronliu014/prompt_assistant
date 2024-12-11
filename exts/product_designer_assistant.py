from pydantic import ValidationError
from typing import Any, Dict, Optional, List
from core import PromptAssistant, PromptTemplateModel

# Example ProductDesignerAssistant for extensions
class ProductDesignerAssistant(PromptAssistant):
    """
    An assistant class customized specifically for product designers, automatically setting roles and related fields.
    """

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = "",
        output: Dict[str, Any] = {},
        additional_constraints: Optional[List[str]] = None
    ) -> PromptTemplateModel:
        """
        Create a prompt template for a product designer, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's design task.
        :param context: Optional background information.
        :param additional_constraints: Optional list of additional constraint rules.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced product designer specializing in AI and mobile internet product design."
        default_context = context if context else "Please create a product design based on the provided task description."
        default_input = {"type": "text", "data": task}
        default_output = {
            "type": "text",
            "format": "markdown",
            "constraints": {"type_specific": ["Highly professional", "Well-structured"]},
            "examples": [
                '''
# 产品设计需求文档范例

## 一、产品简介
### （一）产品使用价值
- **我是谁**：“美食分享平台”是一款专注于美食爱好者分享美食体验、菜谱以及发现美食好去处的移动应用。
- **我有什么用**：用户可以在平台上发布自己制作或品尝美食的照片、心得，分享独特的菜谱，同时也能通过定位功能查找附近的热门餐厅、小吃摊等美食地点。
- **为什么选择我们**：与其他美食类应用相比，我们拥有简洁美观的界面设计，提供个性化的美食推荐算法，根据用户的口味偏好精准推送美食内容，并且注重用户互动，打造活跃的美食社区。

### （二）目标用户、使用场景
- **目标用户**：美食爱好者，包括喜欢烹饪的家庭主妇/夫、热爱探店的吃货、美食博主等。
- **使用场景**：
    - 用户在家尝试新菜谱后，拍照记录并分享到平台，同时附上详细的制作步骤和心得。
    - 外出就餐时，使用平台查找附近美食，查看其他用户的评价后选择心仪的餐厅，就餐后分享美食体验。
    - 美食博主在平台上发布高质量的美食内容，吸引粉丝关注，与其他用户互动交流美食心得。

## 二、行业概要
### （一）行业现状
目前美食分享类应用市场竞争激烈，存在多种类型的竞争对手。部分应用专注于菜谱分享，提供海量的菜谱资源；一些则侧重于餐厅推荐，整合了众多商家信息。同时，社交媒体平台上也有大量美食相关内容，但缺乏专业的美食分享社区氛围。

### （二）未来发展趋势
随着人们对美食的追求不断提升，美食分享类应用将更加注重个性化推荐、视频化内容展示以及社交互动功能的深化。同时，与线下餐饮商家的合作模式也将更加多样化，例如提供在线预订、外卖点餐、美食活动推广等服务。

### （三）竞争对手情况分析
- **竞品A**：是一款知名的菜谱分享应用，拥有庞大的菜谱数据库，但用户互动性相对较弱，主要以单向的菜谱查询和学习为主。
- **竞品B**：侧重于餐厅推荐和点评，与众多商家合作，提供优惠信息，但在用户生成内容（UGC）方面的激励不足，用户分享美食体验的积极性不高。
- **竞品C**：是社交媒体平台上的美食话题社区，内容丰富多样，但缺乏专业的美食分类和精准推荐功能，用户查找特定类型美食信息较为困难。

## 三、版本
### （一）排期
本次大版本开发排期如下：
| 活动项 | 时间 | 交付物 | 责任人 |
|---|---|---|---|
| 需求分析与文档编写 | 20XX/XX/XX - 20XX/XX/XX | 需求文档 | 产品经理 |
| UI设计 | 20XX/XX/XX - 20XX/XX/XX | UI设计稿 | UI设计师 |
| 前端开发 | 20XX/XX/XX - 20XX/XX/XX | 前端代码 | 前端开发工程师 |
| 后端开发 | 20XX/XX/XX - 20XX/XX/XX | 后端接口 | 后端开发工程师 |
| 测试 | 20XX/XX/XX - 20XX/XX/XX | 测试报告 | 测试工程师 |
| 上线准备与发布 | 20XX/XX/XX - 20XX/XX/XX | 上线版本 | 运维工程师 |

### （二）产品设计（重点）
#### 1. 实体关系图（E-R图）
- **用户**：包含属性（用户ID、用户名、密码、头像、性别、年龄、注册时间、个人简介等）。
- **美食菜谱**：属性有（菜谱ID、菜谱名称、菜品图片、食材列表、制作步骤、烹饪时间、难度等级、发布用户ID等）。
- **餐厅**：包括（餐厅ID、餐厅名称、地址、联系电话、营业时间、人均消费、餐厅类型、评分、发布用户ID等）。
- **评论**：属性为（评论ID、评论内容、评论时间、评论用户ID、关联菜谱ID/餐厅ID等）。
- **点赞/收藏**：涉及（点赞/收藏ID、用户ID、关联菜谱ID/餐厅ID等）。

#### 2. 用户角色权限表
| 用户角色 | 查看美食菜谱 | 发布美食菜谱 | 查看餐厅信息 | 发布餐厅评价 | 点赞/收藏 | 管理个人信息 |
|---|---|---|---|---|---|---|
| 普通用户 | 是 | 是 | 是 | 是 | 是 | 是 |
| 美食博主（认证用户） | 是 | 是 | 是 | 是 | 是 | 是 |
| 管理员 | 是 | 是 | 是 | 是 | 是 | 是（可管理所有用户信息） |

#### 3. 业务流程图
用户进入应用后，可选择浏览美食菜谱、查找附近餐厅或进入个人中心。浏览菜谱时可查看详情、点赞收藏、发表评论；查找餐厅可根据距离、评分等筛选，查看餐厅信息并评价。用户也可在个人中心编辑个人资料、发布菜谱或查看自己的点赞收藏记录。

#### 4. 全局说明
- **空数据状态**：当页面无数据时，显示“暂无相关内容，快去探索美食吧！”的提示语，并提供相应的引导操作，如发布菜谱或查找餐厅。
- **网络异常状态**：若网络连接不畅，弹出“网络连接异常，请检查网络设置后重试”的提示框，同时提供重试按钮。
- **加载失败状态**：加载内容失败时，显示“加载失败，请稍后重试”，并可点击重新加载。
- **刷新状态**：用户手动刷新页面时，显示加载动画，刷新完成后更新数据。

#### 5. 需求、功能、交互说明
以美食菜谱详情页面为例：
- **字段、字段说明、数据来源**
    - **菜谱名称**：展示菜谱的具体名称，由发布用户填写。
    - **菜品图片**：展示美食的成品图片，由发布用户上传。
    - **食材列表**：详细列出制作该美食所需的食材及用量，发布用户编辑。
    - **制作步骤**：按顺序呈现美食的制作过程，发布用户编写。
    - **烹饪时间**：显示制作该美食大概所需的时间，发布用户提供。
    - **难度等级**：分为简单、中等、困难三个级别，由发布用户选择。
    - **点赞数/收藏数**：统计该菜谱获得的点赞和收藏数量，系统实时计算。
    - **评论列表**：展示用户对该菜谱的评论内容、评论时间和评论用户头像/昵称，数据来源于用户评论。
- **前置条件、排序机制、刷新机制**
    - **前置条件**：用户需登录才能点赞、收藏、评论菜谱；发布菜谱需先填写完整的菜谱信息。
    - **排序机制**：评论按照发布时间倒序排列，最新的评论显示在最上方。
    - **刷新机制**：用户下拉页面可手动刷新菜谱详情，获取最新的点赞数、收藏数和评论数据。
- **状态流转（一个页面可能有多个状态，需要说明）**
    - **初始状态**：页面正常展示菜谱的基本信息、图片、点赞收藏数等。
    - **点赞/收藏成功状态**：用户点击点赞/收藏按钮后，按钮变为已选中状态，点赞数/收藏数立即加1，并显示成功提示。
    - **评论发布成功状态**：用户提交评论后，评论内容显示在评论列表顶部，同时清空评论输入框。
- **交互操作（正常操作、异常操作）**
    - **正常操作**：
        - 点击菜谱图片可放大查看高清图。
        - 点击食材列表中的食材可查看食材详情（如营养价值等）。
        - 点击制作步骤中的步骤序号可展开详细步骤说明。
        - 点击点赞/收藏按钮可进行相应操作，再次点击取消。
        - 在评论区输入评论内容后点击发送按钮发布评论。
    - **异常操作**：
        - 当用户快速多次点击点赞/收藏按钮时，系统限制短时间内的重复操作，并提示“操作过于频繁，请稍后再试”。
        - 若评论内容为空时点击发送按钮，提示“请输入评论内容”。

### （三）非功能需求
#### 1. 埋点需求
- 记录菜谱详情页面的打开率，用于分析用户对不同菜谱的关注程度。
- 统计点赞按钮、收藏按钮、评论按钮的点击率，了解用户对菜谱的互动行为。

#### 2. 性能需求
- 页面加载时间控制在1秒以内，确保用户快速获取美食信息。
- 支持10000并发用户访问，保证在高流量情况下应用的稳定性。

#### 3. 兼容性需求
- 支持iOS 10及以上版本、Android 5.0及以上版本的移动操作系统。
- 适配iPhone、华为、小米等主流手机品牌的多种屏幕尺寸。
- 兼容Chrome、Safari、Firefox等主流浏览器（针对网页版应用，如有）。

### （四）修改记录
| 模块 | 页面 | 编辑内容 | 属性 | 修改人 | 日期 |
|---|---|---|---|---|---|
| 美食菜谱 | 菜谱详情 | 新增食材营养价值查看功能 | 功能增强 | 产品经理 | 20XX/XX/XX |
| 用户中心 | 个人资料编辑 | 修改头像上传规则 | 功能调整 | 产品经理 | 20XX/XX/XX |
| 餐厅列表 | 筛选功能 | 优化筛选条件显示方式 | UI优化 | UI设计师 | 20XX/XX/XX |
'''
            ]
        }
        if not output:
            output = default_output
        constraints = {
            "rules": ["Provide detailed design proposals", "Include user needs analysis"],
            "time_limit": None,  # Default time limit
            "length_limit": None  # Default length limit
        }
        if additional_constraints:
            constraints["rules"].extend(additional_constraints)
        default_style = {"language": "Chinese"}

        try:
            template = PromptTemplateModel(
                task=task,
                role=default_role,
                context=default_context,
                input=default_input,
                output=output,
                constraints=constraints,
                style=default_style
            )
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating product designer prompt template: {e}")