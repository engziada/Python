import gooeypie as gp
from time import sleep
import threading
from plyer import notification

app = gp.GooeyPieApp('Stopwatch!')
app.width = 800
app.set_grid(15, 3)
app.set_column_weights(1, 1, 0)


def save(event):
    pass

name_lbl = gp.Label(app, "الاسم (حسب جواز السفر)")
name_inp = gp.Input(app)
car_lbl = gp.Label(app, "رقم السيارة")
car_inp = gp.Input(app)
nationalno_lbl = gp.Label(app, "الرقم الوطني/التسلسلي")
nationalno_inp = gp.Input(app)
passport_lbl = gp.Label(app, "رقم جواز السفر")
passport_inp = gp.Input(app)
email_lbl = gp.Label(app, "البريد الإلكتروني")
email_inp = gp.Input(app)
phone_lbl = gp.Label(app, "رقم اتصال فعال")
phone_inp = gp.Input(app)

nationality_lbl = gp.Label(app, 'الجنسية')
nationality_radios = gp.Radiogroup(app, ['سوري','أردني'],orientation='horizontal')
nationality_radios.selected_index=1
countrycode_lbl = gp.Label(app, 'كود الدولة')
countrycode_radios = gp.Radiogroup(app, ['سوريا - 00963', 'الأردن - 00962'], orientation='horizontal')
countrycode_radios.selected_index = 1
direction_lbl = gp.Label(app, 'الإتجاه')
direction_radios = gp.Radiogroup(app, ['خروج من الأردن', 'دخول للأردن'], orientation='horizontal')
direction_radios.selected_index = 1

btn_container = gp.LabelContainer(app, '')
btn_container.set_grid(1, 5)
btn_container.set_column_weights(1,0,1,0,1)
save_btn = gp.Button(btn_container, 'حفظ', save)
exit_btn = gp.Button(btn_container, 'تنفيذ', save)
btn_container.add(save_btn,1,2)
btn_container.add(exit_btn, 1, 4)

status = gp.StyleLabel(app, 'جاهز')
status.color = 'darkgray'
status.font_size = 12
status.align = 'right'
status.font_style = 'normal'
status.font_name = 'times new roman'
status.margin_top = 50
status.border = True

title = gp.StyleLabel(app, 'مركز حدود جابر')
title.color = 'darkblue'
title.font_size=32
title.align='center'
title.font_style = 'normal'
title.font_name = 'times new roman'
title.margin_bottom=50
title.border=True

row=1
app.add(title, row, 1, fill=True, column_span=3)

row+=1
app.add(direction_radios, row , 1, fill=True, column_span=2,
        margins=['auto', 'auto', 'auto', 300])
app.add(direction_lbl, row, 3, align='right')

row += 1
app.add(name_inp, row, 1, fill=True, column_span=2,
        align='right', margins=['auto', 'auto', 'auto', 50])
app.add(name_lbl, row, 3, align='right')

row += 1
app.add(nationality_radios, row, 1, fill=True, column_span=2,
        margins=['auto', 'auto', 'auto', 300])
app.add(nationality_lbl, row, 3, align='right')

row += 1
app.add(passport_inp, row, 1, fill=True, column_span=2,
        align='right', margins=['auto', 'auto', 'auto', 50])
app.add(passport_lbl, row, 3, align='right')

row += 1
app.add(nationalno_inp, row, 1, fill=True, column_span=2,
        align='right', margins=['auto', 'auto', 'auto', 50])
app.add(nationalno_lbl, row, 3, align='right')

row += 1
app.add(car_inp, row, 1, fill=True, column_span=2,
        align='right', margins=['auto', 'auto', 'auto', 50])
app.add(car_lbl, row, 3, align='right')

row += 1
app.add(email_inp, row, 1, fill=True, column_span=2,
        align='right', margins=['auto', 'auto', 'auto', 50])
app.add(email_lbl, row, 3, align='right')

row += 1
app.add(countrycode_radios, row, 1, fill=True, column_span=2,
        margins=['auto', 'auto', 'auto', 300])
app.add(countrycode_lbl, row, 3, align='right')

row += 1
app.add(phone_inp, row, 1, fill=True, column_span=2,
        align='right', margins=['auto', 'auto', 'auto', 50])
app.add(phone_lbl, row, 3, align='right')

row += 1
app.add(btn_container, row, 1, fill=True, column_span=3)

row += 1
app.add(status, row, 1, fill=True,column_span=3)

app.run()
