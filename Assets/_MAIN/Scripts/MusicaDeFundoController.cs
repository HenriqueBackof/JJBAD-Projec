using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MusicaDeFundoController : MonoBehaviour
{
    [SerializeField] private AudioSource fundoMusical;

    [SerializeField] private Sprite somLigadoSprite;
    [SerializeField] private Sprite somDesligadoSprite;

    private bool estadoDoSom = true;

    [SerializeField] private Image muteImage;

    public void ligarDesligarSom() {
        estadoDoSom = !estadoDoSom;
        fundoMusical.enabled = estadoDoSom;

        if (estadoDoSom) {
            muteImage.sprite = somLigadoSprite;
        } else {
            muteImage.sprite = somDesligadoSprite;
        }
    }
   public void volumeDoSom(float value) {
    fundoMusical.volume = value;
   }

}
