#coding windows-1251
__author__ = 'mdu'
class ManualReplacement():
    def __init__(self, **kwargs):
        self.text = kwargs.get('TEXT','')
        self.position = kwargs.get('POSITION',0)
        self.length = kwargs.get('LENGTH',0)
        self.markupStyleName = kwargs.get('MARKUP_STYLE_NAME','')
        self.markupStyleID = kwargs.get('MARKUP_STYLE_ID','')
        self.markupCSSClassName = kwargs.get('MARKUP_CSS_CLASS_NAME','')
        self.pathToElementWithCSSMarkup = kwargs.get('PATH_TO_ELEMENT_WITH_CSS_MARKUP','')


