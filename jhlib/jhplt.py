#!/usr/bin/env python
# coding: utf-8

# **输出特征重要度的图**

# In[ ]:


def plt_feat_import(model_name, max_cols=9999, max_print=10):
    from pyecharts.globals import CurrentConfig, NotebookType
    CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
    from pyecharts import options as opts
    from pyecharts.charts import Bar
    
    # 处理数据并排序
    x_name = model_name.feature_name()
    y_val = [int(x) for x in model_name.feature_importance()]
    val_pairs = [x for x in zip(x_name, y_val)]
    val_pairs.sort(key=lambda x:x[1])
    
    # 设置图像属性
    bar = Bar()
    bar.add_xaxis([x[0] for x in val_pairs][-max_cols:])
    bar.add_yaxis("特征重要度", [x[1] for x in val_pairs][-max_cols:])
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='right'))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="特征重要度"),datazoom_opts=opts.DataZoomOpts(),)
    bar.reversal_axis()
    print(val_pairs[-max_print:][::-1])
    return bar

