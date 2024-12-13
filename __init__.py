from exts import LanguageExpertAssistant
from exts import ProductDesignerAssistant
from exts import PyArchitectAssistant
from exts import PyCoderAssistant
from exts import PythonDeveloperAssistant
from exts import SoftwareArchitectAssistant
from exts import SoftwareEngineerAssistant
from exts import WebDeveloperAssistant
from core import PromptAssistant
from core import PromptTemplateModel

# prompt_assistant/__init__.py
__version__ = '1.0.0'

def get_version():
    return __version__

__all__ = [
    "LanguageExpertAssistant",
    "ProductDesignerAssistant",
    "PyArchitectAssistant",
    "PyCoderAssistant",
    "PythonDeveloperAssistant",
    "SoftwareArchitectAssistant",
    "SoftwareEngineerAssistant",
    "WebDeveloperAssistant",
    "PromptAssistant",
    "PromptTemplateModel",
    "get_version"
]