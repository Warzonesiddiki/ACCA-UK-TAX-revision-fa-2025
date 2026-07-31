/* ENHANCED QUIZ ENGINE, EXAM TIMER, CONFETTI, STREAKS, BADGES */
const QUIZ_ENGINE = {
  answers: {
    'q15_opt': 'A', 'q35_opt': 'B', 'q38_opt': 'A',
    'q41_opt': 'D', 'q44_opt': 'D', 'q47_opt': 'A', 'q62_opt': 'D',
    'q66_opt': 'C', 'q69_opt': 'A', 'q141_opt': 'B',
    'q181_opt': 'C', 'q192_opt': 'B', 'q224_opt': 'A', 'q236_opt': 'D',
    'q249_opt': 'C', 'q276_opt': 'B', 'q290_opt': 'B', 'sq1_opt': 'B'
  },
  streak: 0, bestStreak: 0, totalCorrect: 0, totalAttempted: 0, badges: new Set(),

  init() {
    const saved = localStorage.getItem('TX_QUIZ_ENGINE_STATE');
    if (saved) { try { const d = JSON.parse(saved); this.streak=d.streak||0; this.bestStreak=d.bestStreak||0; this.totalCorrect=d.totalCorrect||0; this.totalAttempted=d.totalAttempted||0; this.badges=new Set(d.badges||[]); } catch(e){} }
    this.updateStreakDisplay();
    this.attachOptionListeners();
  },
  saveState() { localStorage.setItem('TX_QUIZ_ENGINE_STATE', JSON.stringify({streak:this.streak,bestStreak:this.bestStreak,totalCorrect:this.totalCorrect,totalAttempted:this.totalAttempted,badges:Array.from(this.badges)})); },
  attachOptionListeners() {
    document.querySelectorAll('.options-group').forEach(group => {
      const radios = group.querySelectorAll('input[type="radio"]');
      const name = radios.length > 0 ? radios[0].name : '';
      radios.forEach(radio => { radio.addEventListener('change', () => { this.checkAnswer(name, radio.value); }); });
    });
  },
  checkAnswer(name, selected) {
    const correct = this.answers[name];
    if (!correct) return;
    const radios = document.querySelectorAll('input[name="'+name+'"]');
    radios.forEach(r => {
      const label = r.closest('.option-item');
      if (!label) return;
      if (r.value === correct) label.classList.add('reveal-correct');
      if (r.checked && r.value !== correct) label.classList.add('incorrect');
      if (r.checked && r.value === correct) label.classList.add('correct');
    });
    radios.forEach(r => r.disabled = true);
    this.totalAttempted++;
    if (selected === correct) {
      this.streak++; this.totalCorrect++;
      if (this.streak > this.bestStreak) this.bestStreak = this.streak;
      this.showConfetti();
      if (this.streak >= 5) this.awardBadge('hot_streak');
      if (this.streak >= 10) this.awardBadge('on_fire');
      if (this.totalCorrect >= 20) this.awardBadge('quiz_master');
    } else { this.streak = 0; }
    this.updateStreakDisplay(); this.saveState();
    const drillCard = document.querySelector('input[name="'+name+'"]')?.closest('.drill-card');
    if (drillCard) {
      const solBtn = drillCard.querySelector('.solution-toggle-btn');
      const solContent = drillCard.querySelector('.solution-content');
      if (solBtn && solContent && !solContent.classList.contains('open')) {
        setTimeout(() => { solContent.classList.add('open'); solBtn.innerHTML = '▲ Hide Working & Solution'; }, 600);
      }
    }
  },
  updateStreakDisplay() {
    let badge = document.getElementById('streak-badge');
    if (!badge) { badge = document.createElement('div'); badge.id='streak-badge'; badge.className='streak-badge'; document.body.appendChild(badge); }
    if (this.streak > 0) { badge.innerHTML = '🔥 '+this.streak+' Streak!'; badge.style.display='flex'; badge.className='streak-badge'+(this.streak>=5?' fire':''); }
    else { badge.style.display='none'; }
  },
  awardBadge(id) {
    if (this.badges.has(id)) return; this.badges.add(id);
    const names = {'hot_streak':'🔥 Hot Streak — 5 in a Row!','on_fire':'🌋 On Fire — 10 in a Row!','quiz_master':'🧠 Quiz Master — 20 Correct!','exam_ready':'⏱ Exam Ready — 80%+ Quick Fire!'};
    const notif = document.createElement('div'); notif.className='badge-notification';
    notif.innerHTML='🏅 BADGE UNLOCKED!<br><span style="font-size:1rem">'+(names[id]||id)+'</span>';
    document.body.appendChild(notif); setTimeout(()=>notif.classList.add('show'),100);
    setTimeout(()=>{notif.classList.remove('show');setTimeout(()=>notif.remove(),500);},3000);
    this.saveState();
  },
  showConfetti() {
    const canvas = document.getElementById('confetti-canvas'); if(!canvas) return;
    const ctx = canvas.getContext('2d'); canvas.width=window.innerWidth; canvas.height=window.innerHeight;
    const particles=[], colors=['#0c4a38','#177a5b','#a8790f','#c99a2e','#b3372f','#1e5fa8'];
    for(let i=0;i<60;i++) particles.push({x:Math.random()*canvas.width,y:-10-Math.random()*50,vx:(Math.random()-0.5)*8,vy:Math.random()*4+2,size:Math.random()*8+3,color:colors[Math.floor(Math.random()*colors.length)],rotation:Math.random()*360,rotSpeed:(Math.random()-0.5)*10,life:1});
    let frame=0;
    function animate(){ctx.clearRect(0,0,canvas.width,canvas.height);let alive=false;particles.forEach(p=>{if(p.life<=0)return;alive=true;p.x+=p.vx;p.vy+=0.15;p.y+=p.vy;p.rotation+=p.rotSpeed;p.life-=0.012;ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.rotation*Math.PI/180);ctx.globalAlpha=p.life;ctx.fillStyle=p.color;ctx.fillRect(-p.size/2,-p.size/2,p.size,p.size*0.6);ctx.restore();});frame++;if(alive&&frame<120)requestAnimationFrame(animate);else ctx.clearRect(0,0,canvas.width,canvas.height);}
    animate();
  }
};

const EXAM_TIMER = {
  totalSeconds:0, remainingSeconds:0, interval:null, isRunning:false, currentSection:'',
  start(minutes, section) {
    this.stop(); this.totalSeconds=minutes*60; this.remainingSeconds=this.totalSeconds; this.currentSection=section||'Full Exam'; this.isRunning=true;
    const panel=document.getElementById('exam-timer-panel'); if(panel){panel.classList.add('active');this.updateDisplay();}
    this.interval=setInterval(()=>{if(this.remainingSeconds>0){this.remainingSeconds--;this.updateDisplay();}else{this.stop();this.timeUp();}},1000);
  },
  stop(){this.isRunning=false;if(this.interval)clearInterval(this.interval);this.interval=null;},
  pause(){if(this.interval){clearInterval(this.interval);this.interval=null;}},
  resume(){if(!this.isRunning)return;this.interval=setInterval(()=>{if(this.remainingSeconds>0){this.remainingSeconds--;this.updateDisplay();}else{this.stop();this.timeUp();}},1000);},
  updateDisplay(){
    const display=document.getElementById('timer-display'),section=document.getElementById('timer-section');if(!display)return;
    const mins=Math.floor(this.remainingSeconds/60),secs=this.remainingSeconds%60;
    display.textContent=String(mins).padStart(2,'0')+':'+String(secs).padStart(2,'0');
    display.className='timer-display';if(this.remainingSeconds<=300)display.classList.add('timer-critical');else if(this.remainingSeconds<=600)display.classList.add('timer-warning');
    if(section)section.textContent=this.currentSection;
  },
  timeUp(){
    const display=document.getElementById('timer-display');if(display){display.textContent="TIME'S UP!";display.classList.add('timer-critical');}
    const notif=document.createElement('div');notif.className='badge-notification show';notif.style.background='linear-gradient(135deg,#b3372f,#e74c3c)';
    notif.innerHTML="⏰ TIME'S UP!<br><span style='font-size:0.9rem'>Move to the next section!</span>";
    document.body.appendChild(notif);setTimeout(()=>{notif.classList.remove('show');setTimeout(()=>notif.remove(),500);},3000);
  }
};

const QUICK_FIRE = {
  questions: [
    {q:"What is the Personal Allowance for 2025/26?",opts:["£12,500","£12,570","£11,850","£13,000"],ans:1,topic:"IT"},
    {q:"At what ANI does the PA taper begin?",opts:["£50,000","£100,000","£125,140","£150,000"],ans:1,topic:"IT"},
    {q:"What is the marginal fraction for CT?",opts:["1/200","2/200","3/200","4/200"],ans:2,topic:"CT"},
    {q:"What is the AIA limit for 2025/26?",opts:["£200,000","£500,000","£1,000,000","£2,000,000"],ans:2,topic:"CA"},
    {q:"CGT higher rate for residential property (FA2025)?",opts:["18%","24%","28%","20%"],ans:1,topic:"CGT"},
    {q:"What is the CGT Annual Exempt Amount?",opts:["£6,000","£3,000","£12,300","£1,000"],ans:1,topic:"CGT"},
    {q:"IHT Nil Rate Band amount?",opts:["£250,000","£300,000","£325,000","£350,000"],ans:2,topic:"IHT"},
    {q:"VAT registration threshold?",opts:["£80,000","£85,000","£90,000","£95,000"],ans:2,topic:"VAT"},
    {q:"Class 1 Employee NIC rate £12,571-£50,270?",opts:["10%","8%","12%","6%"],ans:1,topic:"NIC"},
    {q:"Standard Pension Annual Allowance?",opts:["£40,000","£50,000","£60,000","£80,000"],ans:2,topic:"Pension"},
    {q:"Car fuel benefit multiplier (FA2025)?",opts:["£25,300","£27,800","£28,200","£30,000"],ans:2,topic:"IT"},
    {q:"BADR lifetime limit?",opts:["£500,000","£1,000,000","£2,000,000","£10,000,000"],ans:1,topic:"CGT"},
    {q:"RNRB maximum per individual?",opts:["£100,000","£125,000","£175,000","£200,000"],ans:2,topic:"IHT"},
    {q:"CT small profits rate?",opts:["17%","19%","20%","18%"],ans:1,topic:"CT"},
    {q:"Main rate CT for profits over £250,000?",opts:["19%","20%","23%","25%"],ans:3,topic:"CT"},
    {q:"When must online SA return be filed?",opts:["31 Oct","31 Dec","31 Jan","5 April"],ans:2,topic:"Admin"},
    {q:"CGT 60-day property return deadline?",opts:["14 days","30 days","60 days","90 days"],ans:2,topic:"CGT"},
    {q:"VAT standard rate?",opts:["15%","17.5%","20%","25%"],ans:2,topic:"VAT"},
    {q:"Class 4 NIC rate £12,571-£50,270?",opts:["8%","6%","9%","2%"],ans:1,topic:"NIC"},
    {q:"Savings Nil Rate Band for basic rate?",opts:["£0","£500","£1,000","£5,000"],ans:2,topic:"IT"}
  ],
  currentQ:0, score:0, results:[],
  start(){this.questions=[...this.questions].sort(()=>Math.random()-0.5);this.currentQ=0;this.score=0;this.results=[];this.showQuestion();document.getElementById('qf-modal').classList.add('active');},
  close(){document.getElementById('qf-modal').classList.remove('active');},
  showQuestion(){
    const q=this.questions[this.currentQ],total=this.questions.length;
    let dots='<div class="qf-progress">';for(let i=0;i<total;i++){let cls='qf-dot';if(i<this.results.length)cls+=this.results[i]?' correct':' incorrect';else if(i===this.currentQ)cls+=' current';dots+='<div class="'+cls+'"></div>';}dots+='</div>';
    let opts=q.opts.map((o,i)=>'<div class="option-item" onclick="QUICK_FIRE.answer('+i+')" style="cursor:pointer;margin:0.5rem 0"><strong>'+String.fromCharCode(65+i)+'.</strong> '+o+'</div>').join('');
    document.getElementById('qf-content').innerHTML=dots+'<div style="font-family:var(--font-mono);font-size:0.75rem;color:var(--ink-faint);margin-bottom:0.5rem">Question '+(this.currentQ+1)+' of '+total+' • '+q.topic+'</div><h3 style="margin-bottom:1.2rem;color:var(--green-deep)">'+q.q+'</h3><div class="options-group">'+opts+'</div>';
  },
  answer(idx){
    const q=this.questions[this.currentQ],correct=idx===q.ans;this.results.push(correct);
    if(correct){this.score++;QUIZ_ENGINE.streak++;if(QUIZ_ENGINE.streak>QUIZ_ENGINE.bestStreak)QUIZ_ENGINE.bestStreak=QUIZ_ENGINE.streak;QUIZ_ENGINE.showConfetti();}else{QUIZ_ENGINE.streak=0;}
    QUIZ_ENGINE.updateStreakDisplay();QUIZ_ENGINE.saveState();
    const opts=document.querySelectorAll('#qf-content .option-item');opts.forEach((o,i)=>{if(i===q.ans)o.classList.add('correct');if(i===idx&&!correct)o.classList.add('incorrect');o.style.pointerEvents='none';});
    setTimeout(()=>{this.currentQ++;if(this.currentQ<this.questions.length)this.showQuestion();else this.showResults();},1200);
  },
  showResults(){
    const pct=Math.round((this.score/this.questions.length)*100),emoji=pct>=80?'🏆':pct>=60?'👍':pct>=40?'📖':'💪';
    document.getElementById('qf-content').innerHTML='<div style="text-align:center;padding:2rem 0"><div class="qf-score">'+emoji+' '+this.score+'/'+this.questions.length+'</div><p style="font-size:1.2rem;color:var(--ink-soft);margin:1rem 0">'+pct+'% — '+(pct>=80?'Outstanding! Exam ready!':pct>=60?'Good effort! Keep practising!':pct>=40?'Getting there! Review the traps.':'Keep going!')+'</p><div style="display:flex;gap:1rem;justify-content:center;margin-top:1.5rem"><button class="quickfire-btn" onclick="QUICK_FIRE.start()">🔄 Try Again</button><button class="solution-toggle-btn" onclick="QUICK_FIRE.close()">✓ Done</button></div></div>';
    if(pct>=80)QUIZ_ENGINE.awardBadge('exam_ready');
  }
};

const SIDEBAR = {
  isOpen: false,
  toggle(){this.isOpen=!this.isOpen;const s=document.getElementById('topic-sidebar'),t=document.getElementById('sidebar-toggle');if(s)s.classList.toggle('open',this.isOpen);if(t)t.classList.toggle('shifted',this.isOpen);},
  updateCompleted(){const c=GAMIFICATION.completedTasks;document.querySelectorAll('.sidebar-link').forEach(l=>{const p=l.getAttribute('data-part');if(p&&c.has(p))l.classList.add('completed');});}
};

document.addEventListener('keydown',(e)=>{if(e.key==='Escape'){QUICK_FIRE.close();if(SIDEBAR.isOpen)SIDEBAR.toggle();}if(e.key==='['&&e.ctrlKey){e.preventDefault();SIDEBAR.toggle();}});

document.addEventListener('DOMContentLoaded',()=>{QUIZ_ENGINE.init();SIDEBAR.updateCompleted();});
