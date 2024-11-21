
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using TMPro;
public class Nivel4ConversationController : MonoBehaviour
{
    [SerializeField] private string nomeDoLevelDoJogo;
    [SerializeField] private GameObject startGame;
    [SerializeField] private GameObject conversation1;
    [SerializeField] private GameObject description1;
    [SerializeField] private GameObject continueConversation;
    [SerializeField] private GameObject continueDescription;
    [SerializeField] private GameObject botaoOpcoes;
    [SerializeField] private GameObject Jotaro;
    [SerializeField] private GameObject Joseph;
    [SerializeField] private GameObject Avdol;
    [SerializeField] private GameObject Polnaref;
    [SerializeField] private GameObject Kakyoin;
    [SerializeField] [TextAreaAttribute] public List<string> dialogos;
    [SerializeField] [TextAreaAttribute] public List<string> narracao;
    [SerializeField] public List<int> personagemFalas;
    [SerializeField] [TextAreaAttribute] public List<string> narracaoOpcao1;
    [SerializeField] [TextAreaAttribute] public List<string> narracaoOpcao2;
    [SerializeField] private GameObject continueOpcoes;

    private int contadorDialogo = 0;
    private int contadorNarracao = 0;
    private int checkpointNarracao1 = 2;
    private int checkpointOpcao = 1;
    private int checkpointDialogo = 1;
    private bool mostrarOpcao1 = false;
    private bool mostrarOpcao2 = false;
    private int contadorNarracaoOpcao1 = 0;
    private int contadorNarracaoOpcao2 = 0;

    public void trocaBakcgroundDialogoNarracao() {
        description1.SetActive(true);
        conversation1.SetActive(false);
    }

    public void trocaBakcgroundNarracaoDialogo() {
        description1.SetActive(false);
        conversation1.SetActive(true);
    }
    public void StartGame() {
        startGame.SetActive(false);
        continueDescription.SetActive(true);
        description1.SetActive(true);
        description1.GetComponentInChildren<TextMeshProUGUI>().text = narracao[0];
        // MostrarPersonagem(contadorDialogo);
    }
    public void StartConversation() {
        conversation1.SetActive(true); 
        continueConversation.SetActive(true);
        continueDescription.SetActive(false);
        continueOpcoes.SetActive(false);
        MostrarPersonagem(contadorDialogo);
        conversation1.GetComponentInChildren<TextMeshProUGUI>().text = dialogos[contadorDialogo]; 
    }
    public void ContinueConversation() {
        contadorDialogo++;
        if (contadorDialogo < dialogos.Count) {
            conversation1.GetComponentInChildren<TextMeshProUGUI>().text = dialogos[contadorDialogo];
            MostrarPersonagem(contadorDialogo);
        } 
        if (contadorDialogo == checkpointDialogo) {
                trocaBakcgroundDialogoNarracao();
                continueDescription.SetActive(true);
                continueConversation.SetActive(false);
                StartDescription();
                EsconderPersonagens();
                return;
            }
        if (contadorDialogo >= dialogos.Count) {
            SceneManager.LoadScene(nomeDoLevelDoJogo);
            mostrarOpcao1 = false;
            return;
        }
    }

    public void StartDescription() { 
        description1.GetComponentInChildren<TextMeshProUGUI>().text = narracao[contadorNarracao]; 
        }
    public void ContinueDescription() {
        contadorNarracao++;
        if (contadorNarracao < narracao.Count) {
            description1.GetComponentInChildren<TextMeshProUGUI>().text = narracao[contadorNarracao];
        } 

        if (contadorNarracao == checkpointNarracao1) {
            trocaBakcgroundNarracaoDialogo();
            continueDescription.SetActive(false);
            continueConversation.SetActive(false);
            StartConversation();
        }

        if (contadorNarracao == narracao.Count) {
            ShowOptions();
        }
    }

    public void ShowOptions() {
        description1.SetActive(false); 
        continueDescription.SetActive(false);
        EsconderPersonagens();
        
        botaoOpcoes.SetActive(true);
    }

   public void ChoiceOpcao1() {
        mostrarOpcao1 = true;
        contadorNarracaoOpcao1 = 0;
        if (VariavelGlobal.instance)VariavelGlobal.instance.addScore(10);
        description1.SetActive(true);
        botaoOpcoes.SetActive(false);
        description1.GetComponentInChildren<TextMeshProUGUI>().text = narracaoOpcao1[contadorNarracaoOpcao1];
        contadorNarracaoOpcao1++;
        continueOpcoes.SetActive(true);
    }

    public void ChoiceOpcao2() {
        mostrarOpcao2 = true;
        contadorNarracaoOpcao2 = 0;
        ContinueDescriptionOpcao2();
    }
    public void ContinueOptions() {
        if (mostrarOpcao1)
        { ContinueDescriptionOpcao1();
        return;
        } if (mostrarOpcao2) {
        ContinueDescriptionOpcao2();
        return;
        }
    }
    public void ContinueDescriptionOpcao1() {
        if (contadorNarracaoOpcao1 >= narracaoOpcao1.Count) {
            SceneManager.LoadScene(nomeDoLevelDoJogo);
            mostrarOpcao1 = false;
            return;
        }
        if (contadorNarracaoOpcao1 == checkpointOpcao) {
            description1.SetActive(false);
            continueOpcoes.SetActive(false);
            conversation1.SetActive(true);
            continueConversation.SetActive(true);
            StartConversation();
            return;
        }  
        if (contadorNarracaoOpcao1 < narracaoOpcao1.Count) {
            description1.SetActive(true);
            botaoOpcoes.SetActive(false);
            description1.GetComponentInChildren<TextMeshProUGUI>().text = narracaoOpcao1[contadorNarracaoOpcao1];
            contadorNarracaoOpcao1++;
            continueOpcoes.SetActive(true);         
        }
    }

    public void ContinueDescriptionOpcao2() {
        if (contadorNarracaoOpcao2 < narracaoOpcao2.Count) {
            description1.SetActive(true);
            continueOpcoes.SetActive(true);
            botaoOpcoes.SetActive(false);
            description1.GetComponentInChildren<TextMeshProUGUI>().text = narracaoOpcao2[contadorNarracaoOpcao2];
            contadorNarracaoOpcao2++;
        } else {
            mostrarOpcao2 = false;
            SceneManager.LoadScene(nomeDoLevelDoJogo);
        }
    }

    public void MostrarPersonagem(int index) {
        if (index >= 0 && index < personagemFalas.Count) {
            Jotaro.SetActive(false);
            Joseph.SetActive(false);
            Avdol.SetActive(false);
            Polnaref.SetActive(false);
            Kakyoin.SetActive(false);

            if (personagemFalas[index] == 1) { 
                Jotaro.SetActive(true);
            } else if (personagemFalas[index] == 2) { 
                Joseph.SetActive(true);
            } else if (personagemFalas[index] == 3) {
                Avdol.SetActive(true);
            } else if (personagemFalas[index] == 4) {
                Polnaref.SetActive(true);
            } else if (personagemFalas[index] == 5) {
                Kakyoin.SetActive(true);
            }
        }
    }

    public void EsconderPersonagens() {
        Polnaref.SetActive(false);
        Joseph.SetActive(false);
        Jotaro.SetActive(false);
        Avdol.SetActive(false);
        Kakyoin.SetActive(false);
    }
}
