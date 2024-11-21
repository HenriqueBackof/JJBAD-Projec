
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using TMPro;
public class Nivel1ConversationController : MonoBehaviour
{
    [SerializeField] private string nomeDoLevelDoJogo;
    [SerializeField] private string final1;
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
    [SerializeField] [TextAreaAttribute] public List<string> dialogos;
    [SerializeField] [TextAreaAttribute] public List<string> narracao;
    [SerializeField] public List<int> personagemFalas;

    private int contadorDialogo = 0;
    private int contadorNarracao = 0;
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
    }
    public void StartConversation() {
        conversation1.SetActive(true); 
        continueConversation.SetActive(true);
        continueDescription.SetActive(false);
        MostrarPersonagem(contadorDialogo);
        conversation1.GetComponentInChildren<TextMeshProUGUI>().text = dialogos[0]; 
    }
    public void ContinueConversation() {
        contadorDialogo++;
        if (contadorDialogo < dialogos.Count) {
            conversation1.GetComponentInChildren<TextMeshProUGUI>().text = dialogos[contadorDialogo];
            MostrarPersonagem(contadorDialogo);
        }

        if (contadorDialogo == dialogos.Count) {
            ShowOptions();
        }
    }

    public void ContinueDescription() {
        contadorNarracao++;
        if (contadorNarracao < narracao.Count) {
            description1.GetComponentInChildren<TextMeshProUGUI>().text = narracao[contadorNarracao];
        }

        if (contadorNarracao == narracao.Count) {
            trocaBakcgroundNarracaoDialogo();
            StartConversation();
        }
    }

    public void ShowOptions() {
        conversation1.SetActive(false); 
        continueConversation.SetActive(false);
        Polnaref.SetActive(false);
        botaoOpcoes.SetActive(true);
    }

    public void ChoiceOpcao1() {
        SceneManager.LoadScene(final1);
    }

    public void ChoiceOpcao2() {
        SceneManager.LoadScene(nomeDoLevelDoJogo);
        if (VariavelGlobal.instance)VariavelGlobal.instance.addScore(10);
    }

    public void MostrarPersonagem(int index) { 
        Jotaro.SetActive(false);
        Joseph.SetActive(false);
        Avdol.SetActive(false);
        Polnaref.SetActive(false);

        if (personagemFalas[index] == 1) { 
            Jotaro.SetActive(true);
        } else if (personagemFalas[index] == 2) { 
            Joseph.SetActive(true);
        } else if (personagemFalas[index] == 3) {
            Avdol.SetActive(true);
        } else if (personagemFalas[index] == 4) {
            Polnaref.SetActive(true);
        }
    }
}
