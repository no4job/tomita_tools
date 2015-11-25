#coding windows-1251
__author__ = 'mdu'
class Replacement():
    def __init__(self, **kwargs):
        self.text = kwargs.get('TEXT','')
        self.position = kwargs.get('POSITION',0)
        self.length = kwargs.get('LENGTH',0)
        self.marupStyleName = kwargs.get('MARKUP_STYLE_NAME','')
        self.markupCSSClassName = kwargs.get('MARKUP_CSS_CLASS_NAME','')
        self.pathToElementWithCSSMarkup = kwargs.get('PATH_TO_ELEMENT_WITH_CSS_MARKUP','')

