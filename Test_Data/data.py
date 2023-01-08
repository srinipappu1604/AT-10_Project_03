class Orange_Login:
    username = "Admin"
    password = "admin123"
    
class Text_Box:
    admin = "admin"
    ADMIN = "ADMIN"
    pim = "pim"
    PIM = "PIM"
    leave = "leave"
    LEAVE = "LEAVE"
    time = "time"
    TIME = "TIME"
    recruitment = "recruitment"
    RECRUITMENT = "RECRUITMENT"
    myinfo = "my info"
    MYINFO = "MY INFO"
    performance = "performance"
    PERFORMANCE = "PERFORMANCE"
    dashboard = "dashboard"
    DASHBOARD = "DASHBOARD"
    directory = "directory"
    DIRECTORY = "DIRECTORY"
    maintenance = "maintenance"
    MAINTENANCE = "MAINTENANCE"
    buzz = "buzz"
    BUZZ = "BUZZ"
    
class PIM_Add:
    first_name = "Srini"
    last_name = "Pappu"
    username = "srinipappu"
    password = "Srinipappu@pp77."
    confirm_password = "Srinipappu@pp77."
    
class Personal_Details:
    nickname = "pappu"
    otherdetails= "Nil"
    ssn = "123456789"
    sin = "1235458"
    dateofbirth = "1993-04-16"
    militaryservice = "Nil"
    
class Contact_Details:
    street1 = "No.45 Velu Nagar"
    street2 = "Chrompet"
    city ="Chennai"
    state = "Tamilnadu"
    zip = "600045"
    home = "0444256897"
    mobile = "5687563158"
    work = "0444523589"
    workemail = "srini@gmail.com"
    otheremail = "pappu@gmail.com"
    
class emergency_contact:
    name = "Rajendiran"
    relationship = "Father"
    Hometelephone = "04452465853"
    mobile = "9644851265"
    worktelephone = '04425628612'
    
class Dependents_details:
    name = "Rajendiran"
    dateofbirth = "1993-04-16"
    
class Job_Details:
    joineddate = "2022-01-01"
    contractstartdate = "2022-01-01"
    contractenddate = "2023-01-01"
    terminationdate = "2023-01-06"
    notejob = "Nil"
    
class Salary_Details:
    salarycomponent ="10000"
    amountsalary = "50000"
    comments = "Nil"
    accountnumbersalary = "566553255635666"
    routingnumbersalary = "366659"
    amounttotalsalary = "50000"
    
class Tax_Exemptions:
    exemptions = "2"
    exemptionsstateincometax = "4"
    
class Orange_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    
    search_box = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    
    admin_click = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    user_management ='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
    user_role = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    status_disable = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    
    pim_button = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    
    pim = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    leave = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    time = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    recruitment = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    myinfo = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    performance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    directory = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    maintenance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    password_maintenance = '//*[@id="app"]/div[1]/div[1]/form/div[3]/div/div[2]/input'
    confirm_maintenance = '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]'
    buzz = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    
    add_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    
    name_first__box = "firstName"
    
    name_last_box = "lastName"
    
    create_login_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    
    username_login = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    
    status_enable = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    
    password_login = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    
    confirm_password_login = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    
    
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    
    employee_list = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    
    edit_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]'
    
    personal_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
    
    contact_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    
    emergency_contacts = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a'
    
    dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    
    immigration = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a'
    
    job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    
    salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    
    tax_exemptions = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a'
    
    report_to = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a'
    
    qualifications = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a'
    
    membership = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a'
    
    nick_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    
    other_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    
    ssn_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    
    sin_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    
    nationality = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    
    marital_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    
    date_of_birth = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    
    gender_box = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    
    military_service = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    
    contact_details_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    
    street_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    street_2 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    
    city = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    
    state = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    
    zip_code = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    
    country = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    
    home_telephone = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    
    mobile_telephone = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    
    work_telephone = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    
    work_email = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    
    other_email = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    
    save_contact = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    
    add_emergency_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    
    name_emergency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    relationship_emergency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    
    Hometelephone_emergency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    
    mobile_emergency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    
    worktelephone_emergency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    
    save_emergency = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    
    dependents_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    
    add_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    
    name_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    relationship_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    
    dateofbirth_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    
    save_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'
    
    job_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    
    joined_date_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    
    job_title_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    
    job_category_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    
    sub_unit_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]'
    
    location_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    
    employment_status_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]'
    
    include_employment_contract_details_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    
    contract_start_date_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'
    
    contract_end_date_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'
    
    contract_details_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div/div/div/div[2]/div/div[1]'
    
    save_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    
    terminate_employment = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    
    termination_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    
    termination_reason = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]'
    
    note_job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea'
    
    save_job_terminate = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'
    
    activate_employment = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    
    salary_click = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    
    add_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    
    salary_component_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    pay_grade_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    
    pay_frequency_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
    
    currency_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    
    amount_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    
    comments_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea'
    
    direct_deposit_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    
    account_number_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    
    account_type_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    
    routing_number_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    
    amount_total_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    
    save_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'
    
    tax_exemptions = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a'
    
    status_tax_exemptions = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    
    exemptions_tax_exemptions = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    
    state_state_income_tax = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]'
    
    status_state_income_tax = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div'
    
    exemptions_state_income_tax = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    
    unemployment_state_state_income_tax = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]'
    
    work_state_state_income_tax = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]'
    
    save_tax_exemptions = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'
