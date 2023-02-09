from flet import *
import math

rg_direction = Ref[RadioGroup]()
tf_name = Ref[TextField]()
dd_nationality = Ref[Dropdown]()
tf_passportno = Ref[TextField]()
tf_carnumber = Ref[TextField]()
tf_nationalid = Ref[TextField]()
tf_email = Ref[TextField]()
tf_phoneno = Ref[TextField]()
dd_countrycode = Ref[Dropdown]()
selected_files = Ref[TextField]()


def Save(e):
    direction=rg_direction.current.value
    name=tf_name.current.value
    passportno = tf_passportno.current.value
    carnumber = tf_carnumber.current.value
    nationalid = tf_nationalid.current.value
    email=tf_email.current.value
    phoneno = tf_phoneno.current.value
    nationality=dd_nationality.current.value
    countrycode=dd_countrycode.current.value
    status=-1
    log='success'
    image=selected_files.current.data
    
    data = {'name': name, 'direction': direction, 'image': image, 'phoneno': phoneno, 'nationality': nationality,
            'cc': countrycode, 'passportno': passportno, 'nationalid': nationalid, 'carnumber': carnumber, 'email': email, 'status': status, 'log': log}

    print(data)
    bs = BottomSheet(
            Container(
                Row(
                    [
                        Text("من فضلك أدخل كل البيانات المطلوبة",size=16),
                    ],
                    tight=True,alignment='end'
                ),
                padding=20, gradient=LinearGradient([colors.BLACK12, colors.RED_900], rotation=math.pi/2),
        ),
        open=True,
        # on_dismiss=bs_dismissed,
    )
    if not direction or not name or not passportno or not nationalid or not nationality or not carnumber or not email or not countrycode or not phoneno:
        e.page.overlay.append(bs)
        e.page.update()



def CreateForm(page):
    
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.current.value = e.files[0].name
        selected_files.current.data = e.files[0].path
        selected_files.current.update()
    pick_files_dialog = FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    
    
    titlebox = Container(padding=Padding(0, 10, 0, 0), content=Column(horizontal_alignment='center',
    controls=[
    Text("مركز حدود جابر", size=64,
                color=colors.BLUE_900, font_family='arial'),
    Text("المملكة الأردنية الهاشمية", size=28,
                    color=colors.RED_900, font_family='arial'),
    Divider()
    ]))

    form=Container(
        bgcolor=colors.BLACK12,
        padding=20,
        expand=True,
        border_radius=20,
        content=Column(expand=True, controls=[
            RadioGroup(ref=rg_direction, content=Row(controls=[
                Radio(value="in", label="دخول إلى الأردن"),
                Radio(value="out", label="خروج من الأردن")])),
            TextField(ref=tf_name , label="الاسم (حسب جواز السفر)",
                      border_radius=10, text_size=16, icon=icons.PERSON),
            Dropdown(ref=dd_nationality,label='الجنسية', content_padding=Padding(10, 0, 10, 0), border_radius=10,icon=icons.FLAG,
                     options=[
                dropdown.Option(key='192',text='سوري'),
                dropdown.Option(key='99',text='أردني'),
            ]),
            TextField(ref=tf_carnumber,label="رقم السيارة", border_radius=10,
                      text_size=16, icon=icons.CAR_CRASH),
            TextField(ref=tf_nationalid,label="الرقم الوطني/التسلسلي", border_radius=10,
                      text_size=16, icon=icons.PERM_IDENTITY),
            TextField(ref=tf_passportno,label="رقم جواز السفر", border_radius=10,
                      text_size=16, icon=icons.BOOK),
            TextField(ref=tf_email,label="البريد الإلكتروني", border_radius=10,
                      text_size=16, icon=icons.EMAIL),
            TextField(ref=tf_phoneno,label="رقم اتصال فعال", border_radius=10, content_padding=Padding(10, 10, 10, 10), keyboard_type=KeyboardType.NUMBER,
                      text_size=16, icon=icons.PHONE, prefix=Dropdown(ref=dd_countrycode,hint_text='كود الدولة', content_padding=Padding(10, 0, 10, 0), width=120, text_size=12, border_radius=10,
                                                                      options=[
                                                                          dropdown.Option(key='00963',text='سوريا'),
                                                                          dropdown.Option(key='00962',text='الأردن'),
                                                                      ]),
                      ),
            TextField(ref=selected_files, label="صورة جواز السفر", border_radius=10, content_padding=Padding(10, 10, 10, 10),
                      text_size=16, icon=icons.IMAGE,read_only=True ,  prefix=IconButton(
                        icon=icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False),
                      )),
            
            Divider(),
            ElevatedButton('حفظ و إرسال',width=200,on_click=Save)
        ]),
    )
    page.controls.append(titlebox)
    page.controls.append(form)



def main(page:Page):
    page.window_width = 480
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.rtl = True

    CreateForm(page)
    page.update()

    
    
    
app(target=main,name='Test App')
