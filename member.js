function skillsMember()
{
    var skill = document.getElementById("skill").value;
    var member = document.getElementById("member").value;
    var skillList = document.getElementById("skillList");
    var memberList = document.getElementById("memberList");
    var skillArray = skillList.innerHTML.split(",");
    var memberArray = memberList.innerHTML.split(",");
    var flag = 0;
    for(var i = 0; i < skillArray.length; i++)
    {
        if(skillArray[i] == skill)
        {
            flag = 1;
            skillArray[i] = "";
        }
    }
    if(flag == 0)
    {
        skillArray.push(skill);
    }
    flag = 0;
    for(var i = 0; i < memberArray.length; i++)
    {
        if(memberArray[i] == member)
        {
            flag = 1;
            memberArray[i] = "";
        }
    }
    if(flag == 0)
    {
        memberArray.push(member);
    }
    skillList.innerHTML = skillArray.join(",");
    memberList.innerHTML = memberArray.join(",");
    document.getElementById("skill").value = "";
    document.getElementById("member").value = "";
    return false;
}