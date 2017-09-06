from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .models import School_photo_gallery
from .models import School_bog_chairperson
from .models import School_pta_chairperson
from .models import School_principal
from .models import School_dp_academics
from .models import School_dp_admin
from .models import School_languages_department
from .models import School_math_department
from .models import School_sciences_department
from .models import School_humanities_department
from .models import School_boarding_department
from .models import School_games_department
from .models import School_guiding_and_counseling_department
from .models import School_drama_club
from .models import School_music_club
from .models import School_sports_club
from .models import School_christian_union_club
from .models import School_muslim_students_club
from .models import School_journalism_club
from .models import School_debate_club
from .models import School_science_engineering_club
from .models import School_history
from .models import School_mission
from .models import School_vision
from .models import School_site_map
from .models import School_library
from .models import School_dining_hall
from .models import School_form_one_classes
from .models import School_form_two_classes
from .models import School_form_three_classes
from .models import School_form_four_classes
from .models import School_transport
from .models import School_physics_lab
from .models import School_chemistry_lab
from .models import School_biology_lab
from .models import School_computer_lab
from .models import School_fence
from .models import School_bakery
from .models import School_forest
from .models import School_car_park
from .models import School_generator
from .models import School_beautification
from .models import School_documents_downloads
from .models import School_general_information
from .models import Form_one_news_portal
from .models import Form_two_news_portal
from .models import Form_three_news_portal
from .models import Form_four_news_portal
from .models import School_alumnae
from .models import School_updates
from .models import School_admission
from .models import School_core_values
from .models import School_rules
from .models import School_anthem
from .models import School_performance
from .models import School_peace_club
from .models import School_technicals_department
# Create your views here.
def index(request):
    # this is your new view
    gallery = School_photo_gallery.objects.all()
    history = School_history.objects.filter()
    mission = School_mission.objects.filter()
    vision = School_vision.objects.filter()
    sitemap = School_site_map.objects.all()
    general = School_general_information.objects.filter()
    return render(request, 'index.html', {'gallery':gallery, 'history':history, 'mission':mission, 'vision':vision, 'sitemap':sitemap, 'general':general})
def management(request):
    # this is your new view
    bogchair = School_bog_chairperson.objects.all()
    ptachair = School_pta_chairperson.objects.filter()
    principal = School_principal.objects.filter()
    dpacademics = School_dp_academics.objects.filter()
    dpadmin = School_dp_admin.objects.all()
    genea = School_general_information.objects.filter()
    return render(request, 'management.html', {'bogchair':bogchair, 'ptachair':ptachair, 'principal':principal, 'dpacademics':dpacademics, 'dpadmin':dpadmin, 'genea':genea})
def languages(request):
        # this is your new view
    english = School_languages_department.objects.all()
    geneb = School_general_information.objects.filter()
    return render(request, 'deplang.html', {'english':english, 'geneb':geneb})
def sciences(request):
        # this is your new view
    chemistry = School_sciences_department.objects.all()
    genec = School_general_information.objects.filter()
    return render(request, 'depscie.html', {'chemistry':chemistry, 'genec':genec})
def boarding(request):
        # this is your new view
    board = School_boarding_department.objects.all()
    gened = School_general_information.objects.filter()
    return render(request, 'depboard.html', {'board':board, 'gened':gened})
def games(request):
        # this is your new view
    game = School_games_department.objects.all()
    genee = School_general_information.objects.filter()
    return render(request, 'depgame.html', {'game':game,'genee':genee})
def guidance(request):
        # this is your new view
    guide = School_guiding_and_counseling_department.objects.all()
    genef = School_general_information.objects.filter()
    return render(request, 'depguide.html', {'guide':guide, 'genef':genef})
def humanities(request):
        # this is your new view
    cre = School_humanities_department.objects.all()
    geneg = School_general_information.objects.filter()
    return render(request, 'dephuman.html', {'cre':cre, 'geneg':geneg})
def mathematics(request):
        # this is your new view
    maths = School_math_department.objects.all()
    geneh = School_general_information.objects.filter()
    return render(request, 'depmath.html', {'maths':maths, 'geneh':geneh})
def technicals(request):
        # this is your new view
    tech = School_technicals_department.objects.all()
    genei = School_general_information.objects.filter()
    return render(request, 'deptech.html', {'tech':tech, 'genei':genei})


def bakery(request):
        # this is your new view
    bake = School_bakery.objects.all()
    genej = School_general_information.objects.filter()
    return render(request, 'facbake.html', {'bake':bake, 'genej':genej})
def library(request):
        # this is your new view
    libra = School_library.objects.all()
    genek = School_general_information.objects.filter()
    return render(request, 'faclib.html', {'libra':libra, 'genek':genek})
def laboratories(request):
        # this is your new view
    phylab = School_physics_lab.objects.all()
    chemlab = School_chemistry_lab.objects.filter()
    biolab = School_biology_lab.objects.filter()
    complab = School_computer_lab.objects.filter()
    genel = School_general_information.objects.filter()
    return render(request, 'faclab.html', {'phylab':phylab, 'chemlab':chemlab, 'biolab':biolab, 'complab':complab, 'genel':genel})
def dininghall(request):
        # this is your new view
    dine = School_dining_hall.objects.all()
    genem = School_general_information.objects.filter()
    return render(request, 'facdine.html', {'dine':dine, 'genem':genem})
def classrooms(request):
        # this is your new view
    one = School_form_one_classes.objects.all()
    two = School_form_two_classes.objects.filter()
    three = School_form_three_classes.objects.filter()
    four = School_form_four_classes.objects.filter()
    genen = School_general_information.objects.filter()
    return render(request, 'facclass.html', {'one':one, 'two':two, 'three':three, 'four':four, 'genen':genen})
def transport(request):
        # this is your new view
    trans = School_transport.objects.all()
    geneo = School_general_information.objects.filter()
    return render(request, 'factrans.html', {'trans':trans, 'geneo':geneo})
def schoolfence(request):
        # this is your new view
    fence = School_fence.objects.all()
    genep = School_general_information.objects.filter()
    return render(request, 'facfence.html', {'fence':fence, 'genep':genep})
def forest(request):
        # this is your new view
    forest = School_forest.objects.all()
    geneq = School_general_information.objects.filter()
    return render(request, 'facforest.html', {'forest':forest, 'geneq':geneq})
def carpark(request):
        # this is your new view
    park = School_car_park.objects.all()
    gener = School_general_information.objects.filter()
    return render(request, 'facpark.html', {'park':park, 'gener':gener})
def generator(request):
        # this is your new view
    gene = School_generator.objects.all()
    genes = School_general_information.objects.filter()
    return render(request, 'facgene.html', {'gene':gene, 'genes':genes})
def beautification(request):
        # this is your new view
    beu = School_beautification.objects.all()
    genet = School_general_information.objects.filter()
    return render(request, 'facbeauty.html', {'beu':beu, 'genet':genet})


def scienceengineering(request):
        # this is your new view
    scie = School_science_engineering_club.objects.all()
    genera = School_general_information.objects.filter()
    return render(request, 'scieeng.html', {'scie':scie, 'genera':genera})
def peace(request):
        # this is your new view
    peac = School_peace_club.objects.all()
    generaaa = School_general_information.objects.filter()
    return render(request, 'copeace.html', {'peac':peac, 'generaaa':generaaa})
def christianunion(request):
        # this is your new view
    scu = School_christian_union_club.objects.all()
    generb = School_general_information.objects.filter()
    return render(request, 'cocu.html', {'scu':scu, 'generb':generb})
def muslimstudents(request):
        # this is your new view
    sms = School_muslim_students_club.objects.all()
    generc = School_general_information.objects.filter()
    return render(request, 'coms.html', {'sms':sms, 'generc':generc})
def debate(request):
        # this is your new view
    debate = School_debate_club.objects.all()
    generd = School_general_information.objects.filter()
    return render(request, 'codebate.html', {'debate':debate, 'generd':generd})
def drama(request):
        # this is your new view
    dram = School_drama_club.objects.all()
    genere = School_general_information.objects.filter()
    return render(request, 'codrama.html', {'dram':dram, 'genere':genere})
def journalism(request):
        # this is your new view
    journ = School_journalism_club.objects.all()
    generf = School_general_information.objects.filter()
    return render(request, 'cojournalism.html', {'journ':journ, 'generf':generf})
def music(request):
        # this is your new view
    mus = School_music_club.objects.all()
    generg = School_general_information.objects.filter()
    return render(request, 'comusic.html', {'mus':mus, 'generg':generg})
def sports(request):
        # this is your new view
    spor = School_sports_club.objects.all()
    generh = School_general_information.objects.filter()
    return render(request, 'cosports.html', {'spor':spor, 'generh':generh})


def performance(request):
        # this is your new view
    perform = School_performance.objects.filter()
    generi = School_general_information.objects.filter()
    return render(request, 'acperformance.html', {'perform':perform, 'generi':generi})


def admission(request):
        # this is your new view
    admi = School_admission.objects.all()
    generj = School_general_information.objects.filter()
    return render(request, 'stadmission.html', {'admi':admi, 'generj':generj})
def downloads(request):
        # this is your new view
    down = School_documents_downloads.objects.all()
    generk = School_general_information.objects.filter()
    return render(request, 'stdownloads.html', {'down':down, 'generk':generk})
def portal(request):
        # this is your new view
    pone = Form_one_news_portal.objects.all()
    ptwo = Form_two_news_portal.objects.all()
    pthree = Form_three_news_portal.objects.all()
    pfour = Form_four_news_portal.objects.all()
    generl = School_general_information.objects.filter()
    return render(request, 'stportal.html', {'pone':pone, 'ptwo':ptwo, 'pthree':pthree, 'pfour':pfour, 'generl':generl})
def updates(request):
        # this is your new view
    update = School_updates.objects.all()
    genern = School_general_information.objects.filter()
    return render(request, 'stupdates.html', {'update':update, 'genern':genern})
def alumnae(request):
        # this is your new view
    alum = School_alumnae.objects.all()
    genero = School_general_information.objects.filter()
    return render(request, 'alumnae.html', {'alum':alum, 'genero':genero})


def rules(request):
        # this is your new view
    rulers = School_rules.objects.filter()
    generm = School_general_information.objects.filter()
    return render(request, 'strules.html', {'rulers':rulers, 'generm':generm})
def anthem(request):
        # this is your new view
    anth = School_anthem.objects.filter()
    ant = School_general_information.objects.all()
    return render(request, 'anthem.html', {'anth':anth, 'ant':ant})
def contact(request):
        # this is your new view
    con = School_general_information.objects.all()
    return render(request, 'contact.html', {'con':con})
def corevalues(request):
        # this is your new view
    cores = School_core_values.objects.filter()
    core = School_general_information.objects.all()
    return render(request, 'corevalues.html', {'cores':cores, 'core':core})

def search(request):
         # this is your new view
 if 'q' in request.GET and request.GET['q']:
     q = request.GET['q']
     scorer = School_general_information.objects.filter()
     updated = School_updates.objects.filter(news_title__icontains=q)
     admnews = School_admission.objects.filter(news_title__icontains=q)
     ponenews = Form_one_news_portal.objects.filter(news_title__icontains=q)
     ptwonews = Form_two_news_portal.objects.filter(news_title__icontains=q)
     pthreenews = Form_three_news_portal.objects.filter(news_title__icontains=q)
     pfournews = Form_four_news_portal.objects.filter(news_title__icontains=q)
     alumnews = School_alumnae.objects.filter(name__icontains=q)
     return render(request, 'search_results.html', {'alumnews':alumnews, 'ponenews':ponenews, 'ptwonews':ptwonews, 'pthreenews':pthreenews, 'pfournews':pfournews, 'admnews':admnews, 'scorer':scorer, 'updated':updated, 'query':q})

 else:
     return HttpResponse('Please submit a search term.')
