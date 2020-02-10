using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using sa_webapp.Models;
using sa_webapp.Services;

namespace sa_webapp.Controllers
{
    [Produces("application/json")]
    [Route("chatbot/[controller]")]
    [ApiController]
    [EnableCors("ReactPolicy")]
    public class MessageController : Controller
    {
        private readonly MessageService msgService;
        public MessageController(MessageService msgService)
        {
            this.msgService = msgService;
        }

        public Message Get()
        {
            Console.WriteLine("No defined http get method.");
            return new Message();
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Message msg)
        {
            return CreatedAtAction("Get", msg.question, msgService.ask(msg));
        }
        
    }
}