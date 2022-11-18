from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Elder, Dispenser, ElderDisease, ElderPhysical, TakeCare
from django.contrib.auth.models import User, auth
from django.contrib import messages
import face_recognition
# from httpx import options

# Create your views here.

elder_info = {
    "name": '', 
    "surname": '', 
    "birthday": '', 
    "HN": '', 
    "hospital_name": '', 
    "hospital_phone": '', 
    "care_name": '', 
    "care_surname": '', 
    "relation": '', 
    "care_phone": '', 
}
disease_info = {
    "disease_else": '',
    "disease_name": [],
}
physical_info = {
    "physical_name": [],
}
mem = {
    "options" : '',
}
img_data = {
    "crop_arr" : [],
}
logging_in = {
    "username": '', 
    "password": '', 
}
test = {
    "face" : [],
}

# index test
def home(request):
    #return HttpResponse("<h2>hello world</h2>")
    elder_info["name"] =''
    elder_info["surname"] =''
    elder_info["birthday"] =''
    elder_info["HN"] = ''
    elder_info["hospital_name"] = ''
    elder_info["hospital_phone"] = ''
    elder_info["care_name"] = ''
    elder_info["care_surname"] = ''
    elder_info["relation"] = ''
    elder_info["care_phone"] = ''
    disease_info["disease_else"] = ''
    disease_info["disease_name"] = []
    physical_info["physical_name"] = []
    # user = auth.authenticate(username=logging_in['username'], password=logging_in['password'])
    if logging_in['username'] == '' or logging_in['password'] == '':
        logging_in['username'] = ''
        logging_in['password'] = ''
        return redirect('/login_form')
    elif request.user.is_authenticated:
        # print(logging_in['username'])
        # print(logging_in['password'])
        care_taker = request.user.id
        elder_for_show = []
        print("Care Taker ID: ", str(care_taker))
        all_elder = TakeCare.objects.filter(careTaker_id_id=care_taker)
        print(all_elder)
        for i in all_elder:
            e_id = i.elder_id_id
            e_info = Elder.objects.filter(id=e_id)[0]
            elder_for_show.append(e_info)
            # elder_firstname = Elder.objects.filter(id=e_id)[0].first_name
            # elder_surname = Elder.objects.filter(id=e_id)[0].sure_name
            # elder_for_show.append(str(elder_firstname)+" "+str(elder_surname))
            # print(elder_firstname, elder_surname)
        print(elder_for_show)
        return render(request, 'dashboard.html', {'elders': elder_for_show})

def view_elder_info(request):
    if request.method == 'POST':
        # print(request.POST['elder_id'])
        e_id = request.POST['elder_id']
        elder = Elder.objects.filter(id=e_id)[0]
        disease = ElderDisease.objects.filter(elder_id_id=e_id)[0]
        physical = ElderPhysical.objects.filter(elder_id_id=e_id)[0]
        # print(physical.physical['physical_name'])
        # print(type(physical.physical['physical_name']))
        if physical.physical['physical_name'] == []:
            # print('ไม่มีความผิดปกติ')
            phy_result = ['ไม่มีความผิดปกติ']
        else:
            phy_result = physical.physical['physical_name']
        # print(disease.disease['disease_name'])
        # print(elder.memory['options'])
        # print(elder.first_name, elder.sure_name)
    return render(request, 
                    'read_elder_info.html', 
                    {'elder_info': elder, 
                        'elder_disease': disease.disease['disease_name'], 
                        'elder_physical': phy_result, 
                        'elder_memory': elder.memory['options']})

def add_new(request):
    elder_info["name"] =''
    elder_info["surname"] =''
    elder_info["birthday"] =''
    elder_info["HN"] = ''
    elder_info["hospital_name"] = ''
    elder_info["hospital_phone"] = ''
    elder_info["care_name"] = ''
    elder_info["care_surname"] = ''
    elder_info["relation"] = ''
    elder_info["care_phone"] = ''
    disease_info["disease_else"] = ''
    disease_info["disease_name"] = []
    physical_info["physical_name"] = []
    return render(request, 'elder_regis.html', elder_info)

def elder_register(request):
    return render(request, 'elder_regis.html', elder_info)

def elder_register2(request):
    if "next" in request.POST :
        elder_info["name"] = request.POST['elder_name']
        elder_info["surname"] = request.POST['elder_surname']
        elder_info["birthday"] = request.POST['birthday']
        elder_info["HN"] = request.POST['elder_hNumber']
        elder_info["hospital_name"] = request.POST['elder_hName']
        elder_info["hospital_phone"] = request.POST['elder_hPhone']
        elder_info["care_name"] = request.POST['care_name']
        elder_info["care_surname"] = request.POST['care_surname']
        elder_info["relation"] = request.POST['relation']
        elder_info["care_phone"] = request.POST['care_phone']
        return render(request, 'elder_regis2.html',disease_info)
    elif "cancel" in request.POST :
        elder_info["name"] =''
        elder_info["surname"] =''
        elder_info["birthday"] =''
        elder_info["HN"] = ''
        elder_info["hospital_name"] = ''
        elder_info["hospital_phone"] = ''
        elder_info["care_name"] = ''
        elder_info["care_surname"] = ''
        elder_info["relation"] = ''
        elder_info["care_phone"] = ''
        # return render(request, 'layout.html')
        return redirect('/')
    else:
        return render(request, 'elder_regis2.html',disease_info)

def elder_register3(request):
    if "back2" in request.POST :
        return render(request, 'elder_regis2.html',disease_info)
    elif "next2" in request.POST :
        disease_info["disease_else"] = request.POST['disease_else']
        disease_info["disease_name"] = []
        # list_box = ['disease1','disease2','disease3','disease4','disease5','disease_else']
        list_box = ['disease1','disease2','disease3','disease4','disease5']
        for name in list_box :
            di = request.POST.get(name)
            if di :
                disease_info["disease_name"].append(request.POST[name])
        disease_else = request.POST['disease_else'].replace(" ", "").split(",")
        # print(disease_else)
        disease_info['disease_name'].extend(disease_else)
        print(disease_info['disease_name'])
        return render(request, 'elder_regis3.html',physical_info)
    elif "cancel2" in request.POST :
        disease_info["disease_else"] = ''
        disease_info["disease_name"] = []
        # return render(request, 'layout.html')
        return redirect('/')
    else:
        return render(request, 'elder_regis3.html',physical_info)
    

def elder_register4(request):
    if "back3" in request.POST :
        return render(request, 'elder_regis3.html',physical_info)
    elif "next3" in request.POST :
        physical_info["physical_name"] = []
        list_box1 = ['physical1','physical2','physical3','physical4']
        for phy in list_box1 :
            physic_di = request.POST.get(phy)
            if physic_di :
                physical_info["physical_name"].append(request.POST[phy])
        return render(request, 'elder_regis4.html',mem)
    elif "cancel3" in request.POST :
        physical_info["physical_name"] = []
        # return render(request, 'layout.html')
        return redirect('/')
    else:
        return render(request, 'elder_regis4.html',mem)


def elder_register5(request):
    if "back4" in request.POST :
        return render(request, 'elder_regis4.html',mem)
    elif "next4" in request.POST :
        mem['options'] = request.POST['options']
        return render(request, 'elder_regis5.html')
    elif "cancel4" in request.POST :
        mem["options"] = ''
        # return render(request, 'layout.html')
        return redirect('/')
    else:
        return render(request, 'elder_regis5.html')

def save_elder_info(request):
    if "back5" in request.POST :
        return render(request, 'elder_regis4.html', mem)
    elif "next5" in request.POST :
        care_taker = request.user.id
        # img_data['crop_arr'] = request.POST['dataurl']
        # print(len(img_data['crop_arr']))
        if request.method == 'POST' and request.FILES['picture']:
            new_elder = Elder()
            elder_phy = ElderPhysical()
            elder_disease = ElderDisease()
            take_care = TakeCare()
            new_elder.first_name = elder_info['name']
            new_elder.sure_name = elder_info['surname']
            new_elder.birthday = elder_info['birthday']
            new_elder.hospital_number = elder_info['HN']
            new_elder.hospital_name = elder_info['hospital_name']
            new_elder.hospital_phone = elder_info['hospital_phone']
            new_elder.relative_firstname = elder_info['care_name']
            new_elder.relative_surename = elder_info['care_surname']
            new_elder.relative_relation = elder_info['relation']
            new_elder.relative_phone = elder_info['care_phone']
            # new_elder.disease = disease_info['disease_name']
            new_elder.memory = mem
            # new_elder.face = img_data['crop_arr']
            new_elder.image = request.FILES['picture']
            image = face_recognition.load_image_file(request.FILES['picture'])
            image_location = face_recognition.face_locations(image)
            image_encoding = face_recognition.face_encodings(image,image_location)[0]
            changetype = str(image_encoding.tolist())
            test["face"] = changetype
            new_elder.face = test["face"]
            new_elder.save()
            # elder's disease
            elder_disease.elder_id_id = new_elder.id
            elder_disease.disease = disease_info
            elder_disease.save()
            # elder's physical
            elder_phy.elder_id_id = new_elder.id
            elder_phy.physical = physical_info
            elder_phy.save()
            # matching elder and care taker
            take_care.careTaker_id_id = care_taker
            take_care.time_spend = None
            take_care.elder_id_id = new_elder.id
            take_care.save()
            # return render(request, 'layout.html')\
        return redirect('/')
    elif "cancel5" in request.POST :
        print("cancel")
        # return render(request, 'layout.html')\
        return redirect('/')
    else:
        # return render(request, 'layout.html')
        print("else")
        return redirect('/')

def login_form(request):
    return render(request, 'login.html')

def login(request):
    logging_in['username'] = request.POST['login_email']
    logging_in['password'] = request.POST['login_password']
    # login process
    user = auth.authenticate(username=logging_in['username'], password=logging_in['password'])
    if user is not None:
        auth.login(request, user)
        # return render(request, 'layout.html')
        return redirect('/')
    else:
        messages.info(request, 'ไม่พบข้อมูล')
        return redirect('/login_form')

def logout(request):
    auth.logout(request)
    # print(logging_in['username'])
    # print(logging_in['password'])
    logging_in['username'] = ''
    logging_in['password'] = ''
    return redirect('/')

def signup(request):
    return render(request, 'signup.html')

def signup_form(request):
    firstname = request.POST['firstname']
    surename = request.POST['surename']
    e_mail = request.POST['e_mail']
    password = request.POST['password']
    repassword = request.POST['repassword']
    # add user on user auth 
    if password == repassword:
        if User.objects.filter(username=e_mail).exists():
            # print("มีคนใช้ e-mail นี้แล้ว")
            # return render(request, 'login.html')
            messages.info(request, 'มี Email นี้แล้วในระบบ')
            return redirect('/signup')
        else:
            new_user = User.objects.create_user(
                username= e_mail, 
                password= password, 
                email= e_mail, 
                first_name= firstname, 
                last_name= surename, 
            )
            new_user.save()
    else:
        messages.info(request, 'รหัสผ่านไม่ตรงกัน')
        return redirect('/signup')
    # return render(request, 'layout.html')
    return redirect('/')

def elder_register5(request):
    if "back4" in request.POST :
        return render(request, 'elder_regis4.html',mem)
    elif "next4" in request.POST :
        mem['options'] = request.POST['options']
        return render(request, 'elder_regis5.html',img_data)
    elif "cancel4" in request.POST :
        mem["options"] = ''
        return render(request, 'layout.html')
    else:
        return render(request, 'elder_regis5.html',img_data)

# def save_elder_info(request):
#     if "back5" in request.POST :
#         return render(request, 'elder_regis4.html',mem)
#     elif "next5" in request.POST :
#         img_data['crop_arr'] = request.POST['dataurl']
#         print(len(img_data['crop_arr']))
#         return render(request, 'layout.html',img_data)
#     elif "cancel5" in request.POST :
#         img_data['crop_arr'] = []
#         return render(request, 'layout.html')
#     else:
#         return render(request, 'layout.html',img_data)
